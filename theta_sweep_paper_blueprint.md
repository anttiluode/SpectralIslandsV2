# Paper Blueprint: Phase-Addressable Holographic Readout in the Entorhinal Grid System

## A disciplined plan — what can be claimed, what cannot, and the one experiment that would make it real

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

---

## 0. The verdict this blueprint is built on

The Vollan, Gardner, Moser & Moser paper (*Nature*, Feb 2025) is **consistent with and encouraging for** the framework's core structural claim — that the medial entorhinal grid population behaves as a generative, phase-addressable basis that can represent locations the animal has never visited. It is **not** a proof of the framework, and the `theta_sweep_holography.py` script does **not** demonstrate emergence. It demonstrates the Fourier shift theorem (a linear phase ramp = a spatial translation), with the sweep and its left-right alternation both inserted by hand. Any paper must be built on the first sentence and must not repeat the script's error.

This document exists to keep the claim small enough to be true.

---

## 1. The circularity, stated precisely (so it is never repeated)

The script sets each neuron's phase to `φ_i = 2π (k_i · target_pos)` and reconstructs

```
field(r) = Σ_i cos(2π k_i·r − φ_i) = Σ_i cos(2π k_i·(r − target_pos)).
```

This is maximal at `r = target_pos`, where every term equals 1. So the decoded peak equals the imposed `target_pos = rat_pos + sweep_vector`. The output is the input. The alternation is the hard-coded line `direction_sign = ±1` by cycle parity. Nothing emerges; nothing is discovered. It is a correct *illustration* of phase-coded translation and nothing more.

**Rule for the paper:** any quantity claimed as a *result* must be a *readout* of dynamics, never a variable written in and read back out.

---

## 2. What is already known (and must be cited, not re-claimed)

- Grid patterns are sums of three 2D plane waves at 60° — a Fourier description (standard).
- Continuous attractor network (CAN) models already translate the grid bump via a direction input routed through conjunctive cells (Burak & Fiete 2009; McNaughton et al. 2006). **"Phase shift moves the represented position" is mainstream and twenty years old.**
- The grid→place transform is approximately an inverse transform (Solstad et al. 2006), *approximately, not exactly*.
- Theta-paced look-ahead sweeps in place cells were known (Johnson & Redish 2007; Kay et al. 2020).
- The Vollan/Moser paper adds: sweeps in *grid* cells, into *unvisited* space, *left-right alternating*, driven by parasubiculum internal-direction cells via conjunctive grid cells, with sweep length ∝ grid spacing, persisting in REM.

A paper that claims any of the above as novel will be rejected. The framework owns none of it.

---

## 3. What the framework can legitimately claim

The novel territory is the **substrate** and the **generalization**, not the bump dynamics.

**Claim A — Substrate (the framework's real ground).** The CAN literature describes the dynamics abstractly. It does not commit to a physical implementation of the spectral basis. The framework does: the dendritic cable as a Takens delay-embedding line; the 190 nm AIS actin-spectrin lattice (Leterrier 2018) as the periodic sampler that reads it; the Nav1.6→Nav1.2 gradient as a strength encoder; Johnson-Nyquist noise as dither. This is a falsifiable, structural hypothesis about *where the Fourier sampling physically happens*. It is the part no one else is claiming.

**Claim B — Holographic readout.** Push Solstad harder and quantitatively: the place-cell representation is the inverse transform of the active grid basis, and a *coherent phase offset applied across modules* steers the reconstructed peak. The paper's Fig 1g datum — sweep length ≈ 20% of spacing in *every* module — means a **constant phase offset across modules** (Δφ ≈ 72°), i.e. a manifold-referenced phase steer rather than a fixed real-world distance. This is the clean, correct, framework-relevant reading of the data, and it is the strongest single quantitative point of contact.

**Claim C — Cross-domain generalization (the actual contribution).** If MEC is a *general* phase-addressable basis and not merely a spatial one, the same theta-phase steer should produce "sweeps" through **non-spatial** feature spaces — abstract task variables, conceptual maps, the structure underlying non-spatial entorhinal coding. This prediction goes beyond the Moser paper and is the thing worth publishing.

**Claim D — Coding principle.** Bursty layer-II grid cells carry the sweep and fire on the *outgoing* (moving) phase. This is the modest, supported version of "spikes track the changing part of the standing wave" — present it as consistent with, not proven by, the data.

---

## 4. The competing explanation that must be addressed, not dismissed

The paper's preferred account of the *alternation* is **firing-rate adaptation / spatial-overlap minimization** (Fig 6; Chu et al. 2024; Ji et al. 2024; Widloski & Foster 2024): the just-swept direction is fatigued, so the next sweep goes the other way. This is simpler than "holographic scanning" and is a genuine rival. The framework does not get to ignore it.

Honest position: adaptation may well *be* the alternation mechanism. The holographic/phase-steer account is about *what the basis is and how a represented position is moved*, which is compatible with adaptation choosing *which way* to move it. State this explicitly. Do not claim the alternation as evidence for holography.

---

## 5. The non-circular experiment (this is the heart of any real paper)

Replace the hand-set `target_pos` with a network where position is a **readout, never an input**.

1. Build a CAN-style population of resonator units (the geometric-neuron cable+grating units), arranged so their collective state has a bump on a toroidal manifold.
2. Drive the network **only** with (a) a velocity/direction signal and (b) a theta-rhythmic gain on a conjunctive layer — *nothing else*. Do **not** compute a target location and write it into the phases.
3. Add single-unit firing-rate adaptation (the paper's candidate alternation mechanism).
4. **Read out** the represented position from the population each 10 ms bin (population-vector decode), exactly as the experimentalists do.

Then ask the questions the script could not, because it assumed the answers:

- Do outward sweeps appear in the readout without being inserted? (emergence of look-ahead)
- Does left-right alternation emerge from adaptation alone, with no parity switch coded in? (emergence of alternation)
- Is sweep length ∝ spacing across modules a *consequence*, or must it be imposed?
- **The discriminating test:** perturb the direction-signal layer. Under a steerable phase-beam account, sweep *direction* should shift while sweeps persist. Under pure independent per-module adaptation, direction is set by which cells are fatigued and should be harder to steer coherently. The paper's connectivity (ID → conjunctive → pure grid, with cross-module co-alignment r ≈ 0.60) leans toward steerable, but the multi-module simulation (Ext. Data Fig. 12i) shows per-module alternation is also possible. The question is open — which is exactly why measuring it is worth a paper.

If sweeps and alternation **emerge** from this network, that is a real result. If they must be imposed, the framework learns where its account is incomplete. Either outcome is progress; the current script gives neither.

---

## 6. Proposed paper structure

1. **Background.** Grid cells as Fourier basis; CAN bump-steering (full credit); the Vollan/Moser sweep findings. State plainly what is established.
2. **Hypothesis.** The grid system is a *physically implemented*, phase-addressable holographic basis (Claim A substrate + Claim B readout), of which spatial sweeps are one instance of a general phase-steer operation (Claim C).
3. **Model.** The non-circular network of §5. Specify it fully; release the code.
4. **Results.** Whether/how sweeps, alternation, and length∝spacing emerge from dynamics + adaptation, not insertion. The steerability perturbation test.
5. **The substrate prediction.** Tie the abstract phase steer to the AIS-grating/cable mechanism; state what anatomy or physiology would confirm or refute it.
6. **The cross-domain prediction.** Theta sweeps through a non-spatial feature space — the falsifiable claim that distinguishes this from a purely spatial story.
7. **Honest ledger** (§7 below), included as a section, not an appendix.

---

## 7. Where this could be wrong (the section that makes it science)

- **The substrate claim (A)** rests on the AIS lattice acting as a spectral sampler — a hypothesis layered on real structure whose functional role on the action potential is, in Leterrier's own words, *not yet demonstrated*. It may be structurally real and computationally irrelevant.
- **The readout claim (B)** uses grid→place as a transform that is only approximate; recurrent CA3 and inhibition modify it.
- **Alternation** may be wholly adaptation, contributing nothing specifically holographic.
- **The cross-domain claim (C)** is the riskiest and the most valuable: if theta sweeps do *not* appear in non-spatial entorhinal coding, the "general basis" claim is wounded.
- The phase-steer account adds, over CAN models, a substrate and a generalization — **not** a new dynamical mechanism. Claiming otherwise is the failure mode to avoid.

---

## 8. The single sentence the paper has to earn

*The entorhinal grid system is a physically implemented, phase-addressable basis whose theta-paced spatial sweeps are one spatial instance of a general phase-steer readout; we give a substrate-level mechanism for the basis and a non-spatial prediction that distinguishes it from a purely spatial attractor account.*

Everything in §5 exists to test whether that sentence survives contact with a network that is not allowed to assume it.

*Do not hype. Do not lie. Just show.*
