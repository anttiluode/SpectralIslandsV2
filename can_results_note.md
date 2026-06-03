# Results: the non-circular CAN test

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*
*Code: `spiking_can_resonator.py` · Figure: `spiking_can_resonator.png`*

## What was asked

The blueprint's §5 demanded a simulation where the sweep and its left–right
alternation are **readouts of dynamics, never variables written in and read
back out** — the opposite of `theta_sweep_holography.py`, which set
`target_pos` by hand and recovered it (the Fourier shift theorem dressed as a
result).

## What was built

A ring attractor of 180 direction-tuned units with: local excitation + global
inhibition (so it holds a single bump), a constant heading bias, an 8 Hz theta
excitability clock, and spike-frequency adaptation. A reduced position readout
is advected along the **decoded** internal direction only while theta gain is
high, and pulled back toward the true location otherwise.

The code is told: heading (up), theta clock, attractor connectivity,
adaptation strength `beta`. The code is **never** told which way to sweep, how
far, or when to flip. The entire experiment is `beta = 2.0` versus `beta = 0`.

## Result

| condition | mean offset from heading | alternation score |
|---|---|---|
| adaptation **ON** (beta=2) | ~34° | **1.00** |
| adaptation **OFF** (beta=0) | ~0° (pinned) | 0.27 (noise around zero) |

With adaptation on, the bump leaves heading and flips to the opposite side
every theta cycle — theta skipping, visible as the negative-lag-1 /
positive-lag-2 autocorrelation. With adaptation off, it sits on heading and
does nothing. **The alternation appears and disappears with one parameter, and
nothing in the code encodes it.** That is genuine emergence, not a tautology.

The offset magnitude (~30°) and the theta-skipping match Vollan & Moser (2025)
in order of magnitude. They were not fitted to the data beyond setting the
heading-bias strength into a plausible range.

## What this actually means (the honest reading)

This is a real but **narrow** result, and it cuts in a direction worth stating
plainly:

1. **It supports the paper's own mechanism, not the holographic one.** Vollan &
   Moser favour firing-rate adaptation / overlap-minimisation for the
   alternation (their Fig 6; Chu, Ji, Widloski & Foster 2024). This simulation
   is a neural instance of exactly that. The alternation is an adaptation
   phenomenon.

2. **It shows the pure "dial the phase φ" story is insufficient for the
   alternation.** The circular script implied alternation falls out of phase
   scanning. It does not. Phase scanning moves a represented position; it does
   not, by itself, make the direction flip. Adaptation does. So this result
   *disciplines* the holographic framing rather than confirming it — which is
   the correct outcome for a non-circular test.

3. **The holographic framework's real contribution is untouched here.** This
   sim tests the *dynamical* claim (alternation from adaptation). It says
   nothing about the *substrate* claim (the 190 nm AIS grating as spectral
   sampler, cable as delay line) or the *cross-domain* claim (sweeps through
   non-spatial feature space). Those remain the framework's actual flag, exactly
   as the blueprint argued. No geometric-neuron cable units appear in this
   model, because they would not contribute to the spatial attractor dynamics —
   bolting them on would have been decoration.

## Honest limits

- **Rate-based, not LIF-spiking.** The dynamics are firing-rate (as in the
  cited 2024 models). "Spiking" in the filename is aspirational; a true
  conductance-based version is the next rung and would test robustness.
- **Reduced position readout.** The sweep panel uses a one-particle advection
  proxy for the bump centre, not a full 2D attractor sheet. The emergent
  content (direction + alternation) comes entirely from the ring; the position
  panel only renders it. A full 2D grid-module CAN is the honest next step.
- **Parameter regime.** Clean alternation lives in a window (tau_a ≈ 60 ms,
  moderate beta). Outside it, the behaviour is messy or absent — consistent
  with a real dynamical mechanism that needs the right timescale, not a
  universal law.
- **Offset angle was tuned.** The qualitative emergence (alternation iff
  adaptation) is robust and unfitted; the specific ~34° was set via bias
  strength to sit near the data.

## Bottom line

The test passed on its own terms: left–right alternation **emerges** from
adaptation in a network that was never told to alternate. The honest cost is
that the result belongs to the adaptation hypothesis the paper already
proposed, and it shows the phase-scanning intuition cannot claim the
alternation. The framework's distinctive bets — substrate and cross-domain
generality — are still unproven and still where the real work is.

*Do not hype. Do not lie. Just show.*
