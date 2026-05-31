"""
CableNeuron v2 — biological AIS geometry

Signal path:
  x(t) → CableUnit (RC transmission line = physical Takens manifold)
        → GratingAIS (periodic actin-ring sampling + Nav1.6/Nav1.2 gradient)
        → (spike, position, mismatch, resonance)

New biology in v2:
  - The AIS SAMPLES the cable at periodic positions (every grating_period
    compartments) — this is the physical 190nm actin-spectrin scaffold
  - Nav channels sit AT those positions, not everywhere
  - Threshold gradient: Nav1.6 (distal, pos 0, low threshold)
    to Nav1.2 (proximal, pos N, high threshold)
  - Spike POSITION encodes signal strength — weak fires distally,
    strong fires proximally
  - Templates are built by running the same cable on pure tones,
    then sampling at grating positions — physics-consistent
"""

import torch
import torch.nn as nn
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# ─── CableUnit ────────────────────────────────────────────────────────────────

class CableUnit(nn.Module):
    def __init__(self, length=128, rc_alpha=0.93):
        super().__init__()
        self.length = length
        self.register_buffer('rc_alpha', torch.tensor(rc_alpha, dtype=torch.float32))
        self.register_buffer('state',    torch.zeros(length))
        self.register_buffer('manifold', torch.zeros(length))
        self.scorch_rate    = 0.001
        self.manifold_decay = 0.9998

    def forward(self, x_t):
        s     = torch.zeros_like(self.state)
        s[0]  = float(x_t)
        s[1:] = self.state[:-1] * self.rc_alpha
        s     = s + self.manifold * 0.08
        self.state = s
        return self.state

    def scorch(self, strength):
        self.manifold = (self.manifold * self.manifold_decay
                        + self.state   * self.scorch_rate * strength)

    def reset(self):
        self.state = torch.zeros(self.length)


# ─── GratingAIS ───────────────────────────────────────────────────────────────

class GratingAIS(nn.Module):
    """
    The AIS as a periodic sampling structure with channel gradient.

    Sampling: Nav channels sit at actin ring positions every grating_period
    compartments along the cable. The AIS only reads the cable at those
    positions. Johnson-Nyquist noise added before sampling.

    Gradient: threshold increases linearly from distal (Nav1.6, sensitive)
    to proximal (Nav1.2, strong). Spike position = where threshold first
    crossed = encodes signal strength beyond binary spike/no-spike.

    Templates: built by running the same cable on pure tones and sampling
    at grating positions — physically consistent with the reading operation.
    """
    def __init__(self, cable_length=128, rc_alpha=0.93,
                 grating_period=3,
                 freqs=None,
                 noise_sigma=0.03,
                 nav16_threshold=0.25,
                 nav12_threshold=0.70):
        super().__init__()

        self.cable_length   = cable_length
        self.rc_alpha       = rc_alpha
        self.grating_period = grating_period
        self.noise_sigma    = noise_sigma

        # Grating sample positions
        self.register_buffer(
            'grating_idx',
            torch.arange(0, cable_length, grating_period)
        )
        self.n_samples = len(self.grating_idx)

        if freqs is None:
            freqs = np.array([0.04, 0.08, 0.12, 0.18, 0.25, 0.32, 0.40, 0.46])
        self.freqs = list(freqs)

        # Build templates by running cable on pure tones then sampling
        templates = torch.stack([
            self._burn(f) for f in self.freqs
        ])
        self.register_buffer('templates', templates)
        self.register_buffer('template_scorch', torch.zeros(len(self.freqs)))

        # Nav threshold gradient along AIS
        thresholds = torch.linspace(nav16_threshold, nav12_threshold,
                                    self.n_samples)
        self.register_buffer('thresholds', thresholds)

        self.last_resonance = 0.0
        self.last_mismatch  = 1.0
        self.last_best      = 0
        self.last_spike_pos = -1

    def _burn(self, freq, warmup=500):
        """Build template by simulating cable + grating sampling."""
        state = torch.zeros(self.cable_length)
        alpha = torch.tensor(self.rc_alpha, dtype=torch.float32)
        for step in range(warmup):
            x     = np.sin(2 * np.pi * freq * step)
            s     = torch.zeros(self.cable_length)
            s[0]  = x
            s[1:] = state[:-1] * alpha
            state = s
        sampled = state[self.grating_idx]
        n = sampled.norm()
        return sampled / (n + 1e-9)

    def sample(self, cable_state):
        """Sample cable at grating positions with thermal noise."""
        noise  = torch.randn_like(cable_state) * self.noise_sigma
        noisy  = cable_state + noise
        return noisy[self.grating_idx]

    def forward(self, cable_state):
        sampled = self.sample(cable_state)
        sn      = sampled / (sampled.norm() + 1e-9)

        # Template matching
        alignments = (self.templates * sn.unsqueeze(0)).sum(dim=1)
        resonances = alignments ** 2
        weighted   = resonances * (1.0 + self.template_scorch * 0.3)
        best       = weighted.argmax().item()
        res        = resonances[best].item()
        mm         = 1.0 - res

        # Find spike position along Nav gradient
        spike_pos = -1
        for pos in range(self.n_samples):
            if res >= self.thresholds[pos].item():
                spike_pos = pos   # last position that fires = most proximal

        spike = spike_pos >= 0

        self.last_resonance = res
        self.last_mismatch  = mm
        self.last_best      = best
        self.last_spike_pos = spike_pos

        return spike, spike_pos, mm, res

    def burn_template(self, cable_state, idx, strength=0.004):
        sampled = self.sample(cable_state)
        sn = sampled / (sampled.norm() + 1e-9)
        t  = self.templates[idx]
        self.templates[idx] = t * (1 - strength) + sn * strength
        self.templates[idx] /= self.templates[idx].norm() + 1e-9
        self.template_scorch[idx] = torch.clamp(
            self.template_scorch[idx] + 0.002, 0, 1)


# ─── CableNeuron v2 ───────────────────────────────────────────────────────────

class CableNeuronV2(nn.Module):
    def __init__(self, length=128, rc_alpha=0.93,
                 grating_period=3, freqs=None, name=""):
        super().__init__()
        self.name    = name
        self.cable   = CableUnit(length, rc_alpha)
        self.ais     = GratingAIS(length, rc_alpha, grating_period, freqs)

        self.register_buffer('membrane', torch.tensor(0.0))
        self.membrane_leak = 0.88
        self.charge_rate   = 0.14

        self.spike_times     = []
        self.spike_positions = []
        self.resonance_hist  = []
        self.mismatch_hist   = []
        self.t = 0

    def forward(self, x_t, learn=True):
        self.t += 1
        state = self.cable(torch.tensor(float(x_t), dtype=torch.float32))
        spike, pos, mm, res = self.ais(state)

        self.membrane = self.membrane * self.membrane_leak + res * self.charge_rate
        fired = bool(self.membrane > 0.50)
        if fired:
            self.membrane = torch.tensor(0.0)
            self.spike_times.append(self.t)
            self.spike_positions.append(pos)

        if learn and res > 0.35:
            self.cable.scorch(res)
            self.ais.burn_template(state, self.ais.last_best,
                                   strength=0.004 * res)

        self.resonance_hist.append(res)
        self.mismatch_hist.append(mm)
        return {'spike': fired, 'pos': pos, 'resonance': res,
                'mismatch': mm, 'membrane': self.membrane.item()}


# ─── Demo ─────────────────────────────────────────────────────────────────────

def run_demo():
    print("=" * 64)
    print("  CABLE NEURON v2  ·  GratingAIS (190nm) + Nav gradient")
    print("=" * 64)

    torch.manual_seed(42)
    freqs = np.array([0.04, 0.08, 0.12, 0.18, 0.25, 0.32, 0.40, 0.46])

    # ── 1. Frequency selectivity ─────────────────────────────────
    print("\n[1] Frequency selectivity via grating sampling\n")
    results = {}
    for tf in freqs:
        n = CableNeuronV2(length=128, rc_alpha=0.93,
                         grating_period=3, freqs=freqs)
        res_all, mm_all, spikes = [], [], 0
        for step in range(500):
            x   = np.sin(2 * np.pi * tf * step)
            out = n(x, learn=True)
            res_all.append(out['resonance'])
            mm_all.append(out['mismatch'])
            if out['spike']: spikes += 1
        results[tf] = dict(res=np.mean(res_all),
                          late=np.mean(res_all[-100:]),
                          mm=np.mean(mm_all),
                          spikes=spikes,
                          scorch=n.ais.template_scorch.max().item(),
                          pos_hist=n.spike_positions.copy())

    print("  freq   | resonance (early→late) | mismatch | spikes | scorch")
    for tf in freqs:
        r = results[tf]
        print(f"  {tf:.2f}   | {r['res']:.3f} → {r['late']:.3f}         |"
              f"  {r['mm']:.3f}   |  {r['spikes']:4d}  | {r['scorch']:.3f}")

    # ── 2. Spike position encodes strength ───────────────────────
    print("\n[2] Spike position = strength encoding\n")
    print("  amplitude | mean_pos | std_pos | spikes | zone")

    for amp in [0.4, 0.7, 1.0, 1.4]:
        n = CableNeuronV2(128, 0.93, 3, freqs)
        positions, spikes = [], 0
        for step in range(600):
            x = np.sin(2 * np.pi * 0.12 * step) * amp
            out = n(x, learn=False)
            if out['spike']:
                spikes += 1
                positions.append(out['pos'])
        if positions:
            mp = np.mean(positions)
            sp = np.std(positions)
            zone = ("Nav1.6 distal" if mp < 14
                   else "Nav1.2 proximal" if mp > 28
                   else "mixed zone")
        else:
            mp, sp, zone = 0, 0, "subthreshold"
        print(f"  amp={amp:.1f}     |  {mp:5.1f}   |  {sp:4.1f}   |  {spikes:3d}   | {zone}")

    # ── 3. Manifold creep ────────────────────────────────────────
    print("\n[3] Manifold creep (different person at 40)\n")
    n2 = CableNeuronV2(128, 0.93, 3, freqs)
    phase_data = {}
    for label, freq, steps in [("A→ 0.12", 0.12, 400),
                                ("B→ 0.32", 0.32, 400),
                                ("A← 0.12", 0.12, 400)]:
        res_all, mm_all = [], []
        for s in range(steps):
            x   = np.sin(2*np.pi*freq*s)
            out = n2(x, learn=True)
            res_all.append(out['resonance'])
            mm_all.append(out['mismatch'])
        phase_data[label] = (res_all, mm_all)
        print(f"  {label}:  res {np.mean(res_all[:80]):.3f}→{np.mean(res_all[-80:]):.3f}"
              f"   mm {np.mean(mm_all[:80]):.3f}→{np.mean(mm_all[-80:]):.3f}")

    # ── Plot ─────────────────────────────────────────────────────
    fig = plt.figure(figsize=(15, 9))
    fig.patch.set_facecolor('#0a0a0a')
    gs  = GridSpec(3, 3, figure=fig, hspace=0.5, wspace=0.38)
    c   = ['#5b9bd5','#e8734a','#6abf69','#c97dd4','#f0c040','#e05555']

    def ax_(pos):
        ax = fig.add_subplot(pos)
        ax.set_facecolor('#141414')
        for sp in ax.spines.values(): sp.set_color('#2a2a2a')
        ax.tick_params(colors='#888', labelsize=8)
        ax.title.set_color('#ddd')
        ax.xaxis.label.set_color('#888')
        ax.yaxis.label.set_color('#888')
        return ax

    # 0,0: grating sampling illustration
    ax = ax_(gs[0, 0])
    cable_demo = CableUnit(128, 0.93)
    for step in range(300):
        x = np.sin(2*np.pi*0.12*step)
        st = cable_demo(torch.tensor(x, dtype=torch.float32))
    cable_arr = st.detach().numpy()
    gidx = np.arange(0, 128, 3)
    ax.plot(cable_arr, color=c[0], lw=0.9, alpha=0.6, label='cable state')
    ax.scatter(gidx, cable_arr[gidx], color=c[1], s=14, zorder=3,
              label=f'grating samples (period=3)')
    ax.set_title("Grating Sampling of Cable")
    ax.set_xlabel("position (0=now, right=past)")
    ax.legend(fontsize=7, facecolor='#1a1a1a', labelcolor='#ccc')

    # 0,1: Nav threshold gradient
    ax = ax_(gs[0, 1])
    ais_demo = GratingAIS(128, 0.93, grating_period=3, freqs=freqs)
    th = ais_demo.thresholds.numpy()
    ax.fill_between(range(len(th)), th, alpha=0.25, color=c[2])
    ax.plot(th, color=c[2], lw=2)
    ax.axhline(0.25, color=c[1], ls='--', lw=1, alpha=0.7)
    ax.axhline(0.70, color=c[3], ls='--', lw=1, alpha=0.7)
    ax.text(1,  0.22, 'Nav1.6 (distal)', color=c[1], fontsize=8)
    ax.text(25, 0.67, 'Nav1.2 (proximal)', color=c[3], fontsize=8)
    ax.set_title("AIS Threshold Gradient")
    ax.set_xlabel("grating position (0=distal)")

    # 0,2: resonance by frequency
    ax = ax_(gs[0, 2])
    res_vals  = [results[f]['res']  for f in freqs]
    late_vals = [results[f]['late'] for f in freqs]
    xp = np.arange(len(freqs))
    ax.bar(xp-0.2, res_vals,  0.35, color=c[0], alpha=0.8, label='early')
    ax.bar(xp+0.2, late_vals, 0.35, color=c[1], alpha=0.8, label='late (scorched)')
    ax.set_xticks(xp)
    ax.set_xticklabels([f'{f:.2f}' for f in freqs], rotation=45, fontsize=7)
    ax.set_title("Resonance by Frequency")
    ax.legend(fontsize=7, facecolor='#1a1a1a', labelcolor='#ccc')

    # 1,0: spike position distribution
    ax = ax_(gs[1, 0])
    for i, amp in enumerate([0.5, 0.9, 1.3]):
        n = CableNeuronV2(128, 0.93, 3, freqs)
        positions = []
        for step in range(600):
            x = np.sin(2*np.pi*0.12*step)*amp
            out = n(x, learn=False)
            if out['spike']: positions.append(out['pos'])
        if positions:
            ax.hist(positions, bins=range(44), alpha=0.55,
                   color=c[i], label=f'amp={amp}', density=True)
    ax.axvline(14, color='#555', ls=':', lw=1)
    ax.text(1, 0.08, 'Nav1.6\n(weak)', color='#aaa', fontsize=7)
    ax.text(25, 0.08, 'Nav1.2\n(strong)', color='#aaa', fontsize=7)
    ax.set_title("Spike Position = Strength Encoding")
    ax.set_xlabel("spike origin position")
    ax.legend(fontsize=7, facecolor='#1a1a1a', labelcolor='#ccc')

    # 1,1+1,2: manifold creep
    ax = ax_(gs[1, 1:])
    all_res, all_mm = [], []
    bounds = [0]
    for label in ["A→ 0.12", "B→ 0.32", "A← 0.12"]:
        res, mm = phase_data[label]
        all_res.extend(res); all_mm.extend(mm)
        bounds.append(len(all_res))
    ax.plot(all_res, color=c[0], lw=0.8, alpha=0.9, label='resonance')
    ax.plot(all_mm,  color=c[1], lw=0.8, alpha=0.7, label='mismatch')
    for b in bounds[1:-1]:
        ax.axvline(b, color='#444', ls='--', lw=1)
    for i, lbl in enumerate(["A (0.12Hz)", "B (0.32Hz)", "Return A"]):
        ax.text(bounds[i]+20, 0.92, lbl, color='#bbb', fontsize=8)
    ax.set_title("Manifold Creep — GratingAIS v2")
    ax.set_xlabel("timestep"); ax.legend(fontsize=8, facecolor='#1a1a1a', labelcolor='#ccc')

    # 2,0: template scorch map
    ax = ax_(gs[2, 0])
    sc = n2.ais.template_scorch.detach().numpy()
    colors_bar = [c[0] if f in [0.12, 0.32] else '#444' for f in freqs]
    ax.barh(range(len(freqs)), sc, color=colors_bar, alpha=0.85)
    ax.set_yticks(range(len(freqs)))
    ax.set_yticklabels([f'{f:.2f}Hz' for f in freqs], fontsize=7)
    ax.set_title("Template Scorch (A+B trained)")
    ax.set_xlabel("scorch depth")

    # 2,1: spike position over time (one run)
    ax = ax_(gs[2, 1])
    n3 = CableNeuronV2(128, 0.93, 3, freqs)
    sp_t, sp_pos = [], []
    for step in range(800):
        amp = 0.5 + 0.5*np.sin(2*np.pi*0.003*step)   # slowly varying amplitude
        x = np.sin(2*np.pi*0.12*step) * amp
        out = n3(x, learn=False)
        if out['spike']:
            sp_t.append(step)
            sp_pos.append(out['pos'])
    if sp_t:
        sc_ = ax.scatter(sp_t, sp_pos, c=sp_pos, cmap='plasma',
                        s=12, alpha=0.8)
        fig.colorbar(sc_, ax=ax, label='pos', pad=0.02)
    ax.set_title("Spike Position vs Time\n(amplitude-modulated input)")
    ax.set_xlabel("timestep")
    ax.set_ylabel("spike position")

    # 2,2: cable manifold after creep
    ax = ax_(gs[2, 2])
    m = n2.cable.manifold.detach().numpy()
    s = n2.cable.state.detach().numpy()
    g = n2.ais.grating_idx.numpy()
    ax.plot(m, color=c[3], lw=1.5, label='manifold (scorched)')
    ax.plot(s, color=c[0], lw=0.7, alpha=0.6, label='current state')
    ax.scatter(g, m[g], color=c[1], s=10, zorder=3, alpha=0.7,
              label='grating positions')
    ax.set_title("Manifold + Grating Positions")
    ax.set_xlabel("cable position")
    ax.legend(fontsize=7, facecolor='#1a1a1a', labelcolor='#ccc')

    fig.suptitle(
        "CableNeuron v2  ·  190nm GratingAIS  ·  Nav1.6→Nav1.2 gradient  ·"
        "  Spike position = strength encoding",
        color='#ddd', fontsize=10, y=1.01
    )

    out = 'cable_neuron_v2_probe.png'
    plt.savefig(out, dpi=140, bbox_inches='tight', facecolor='#0a0a0a')
    plt.close()
    print(f"\n[4] Plot → {out}")
    print("=" * 64)


if __name__ == "__main__":
    run_demo()
