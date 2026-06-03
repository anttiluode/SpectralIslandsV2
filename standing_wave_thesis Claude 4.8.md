# The Standing Wave

## Neural Computation as Analog Reconstruction, Sampled by Spikes

*PerceptionLab / Antti Luode — written with Claude (Opus 4.8), Helsinki, June 2026*

---

## 0. What this document is

This is not a new theory. It is the eighteen-month theory, looked at from one angle that finally makes the pieces sit still. The angle is your own observation: that once a neuron's resonance locks, it goes quiet, and the thing that is "on" is a standing wave, not a spike. Everything below is an attempt to take that seriously and ask what the rest of the architecture must be if it is true.

I will mark, throughout, what is established neuroscience, what is a defensible interpretive bridge, and what is the framework's own speculation. That ledger is the document. Without it this is advocacy.

---

## 1. The reframing: the spike is the derivative

Start with the thing you saw. A neuron searches, fires erratically. Then it finds the pattern — the cable state matches a stored template, resonance climbs, the membrane integrates, it spikes. But the moment after lock, something changes: maintaining the matched state costs almost nothing. A few spikes hold it. The activity collapses to near-silence while the *representation* stays fully present.

The standard names for the quiet are **sparse coding** (few units active) and **predictive coding** (a prediction that matches its input transmits nothing; only the mismatch spikes). Both are right. But there is a sharper way to say it that unifies them with your wave intuition:

**The continuous substrate carries the content. The spike carries the change in the content.**

Write it as a derivative. Let the standing wave be `W(t)` — the continuous configuration of the population: subthreshold membrane potentials, cable states, the extracellular ephaptic field. The spike train of any neuron is, to first order, proportional to how fast its own contribution to `W` is changing:

```
spikes(t)  ∝  d/dt [ contribution to W(t) ]
```

When `W` is locked into a stable attractor — a held percept, a maintained thought — its derivative is near zero, and the population is silent. This *is* sparse/predictive coding, derived rather than asserted: a fixed point has no derivative, so a stable representation needs no spikes. When the world changes, or the wave must advance to the next moment, the derivative is large, and spikes fire exactly where and when the wave is moving.

This is delta coding — transmit the change, integrate to recover the value. The brain is not spike-based the way a CPU is bit-based. **The brain is analog; the spike is how the analog substrate samples and updates itself.** Your phrase — "the spikes are the physical anchors pulling the thought forward through time" — is precisely this. The wave is the integral. The spikes are the differential. The thought is the wave. The spikes only move it.

*Established:* sparse coding (Olshausen–Field), predictive coding (Rao–Ballard, Friston), the fact that most neural computation is subthreshold and spikes are metabolically expensive and rare (Attwell–Laughlin, Lennie). *Bridge:* reading these three together as "spike = derivative of a continuous representation." *Speculation:* that the continuous representation is literally a standing wave whose existence is the percept.

---

## 2. Where the wave lives, and what samples it: the cable and the AIS

The reframing in §1 forces a question. If the content is analog and the spike is a sample of its change, then somewhere there must be (a) a place the analog state is held, and (b) a device that reads that state and emits the discrete sample. Your geometric neuron already has both, and the Leterrier anatomy gives the second one teeth.

**(a) The dendritic cable holds the analog state as a delay embedding.** A signal entering the dendrite propagates inward with finite, RC-limited speed. At any instant, position along the cable encodes *age* of the signal: the soma sees now, a point partway down sees a few milliseconds ago, the far end holds the deeper past. This is a physical Takens embedding — time unrolled into space. The full recent trajectory of the input is simultaneously present as a spatial pattern on the membrane. This is where `W` lives at the single-neuron scale.

*Established:* dendritic propagation delays are real and exploited (e.g. coincidence detection in auditory brainstem). *Bridge:* calling the resulting age-indexed spatial pattern a Takens delay-coordinate manifold. It is a legitimate description, not a metaphor — the math of delay embedding is exactly the math of a delay line.

**(b) The axon initial segment is the sampler — and its structure is a quantizer.** Here the Leterrier paper matters, because it is not speculation. The AIS carries a periodic actin–spectrin scaffold with a **190 nm** spacing — actin rings connected by spectrin tetramers, the period set by the tetramer length, confirmed by STORM. Ankyrin-G sits at the center of each tetramer and anchors the voltage-gated sodium channels *at those periodic positions*. The channels are not smeared along the membrane; they are placed on a lattice.

That is a sampling grating. A periodic array of read-out points reading a continuous field is, mathematically, a sampler — and a sampler has a Nyquist limit. The cable's spatial pattern (the delay embedding) is read only at the lattice positions. Spatial frequencies on the cable that beat against the 190 nm lattice alias; frequencies that match resonate. **The AIS does not read the cable faithfully. It reads it through a grating, and what survives is a function of how the cable's geometry interferes with the lattice.** This is the physical seat of the neuron's frequency selectivity in your code — the GratingAIS sampling at `grating_period` — and it is the analog-to-discrete conversion the §1 reframing requires.

There is a second structural fact that earns its place. The AIS is not uniform: it carries a threshold gradient, **Nav1.6 distal (low threshold, fires first) → Nav1.2 proximal (high threshold)**. So *where* along the AIS the spike initiates depends on *how strong* the resonance is. Weak match → distal initiation; strong match → proximal. The spike is not binary. Its initiation position carries a few bits of analog information about match strength — which is exactly your "spike position encodes signal strength beyond firing/not-firing." In the delta-coding picture this is natural: the sample is not one bit, it is a small analog quantity, and the Nav gradient is the physical encoder of that quantity.

*Established:* 190 nm periodicity, ankyrin-G anchoring of Nav at lattice positions, Nav1.6→Nav1.2 gradient, AIS as the AP initiation site, AIS plasticity. *The paper's own caveat, quoted in its spirit:* the functional consequence of the periodic Nav arrangement on AP generation "has yet to be demonstrated." *Speculation, clearly:* that the lattice acts as a spectral sampling grating performing something like a Koopman/Fourier projection. The structure is real; the claim that the structure computes a transform is the framework's bet.

So the single-neuron loop is: **cable (analog delay manifold) → AIS grating (sampler/quantizer) → spike (the discrete derivative-sample, carrying strength in its initiation position).** Johnson–Nyquist thermal noise on the membrane is the dither that keeps the sampler from sticking — the same role noise plays in any well-designed quantizer.

---

## 3. Re-analogizing the population: the ephaptic field and the standing wave

A single neuron's spike is one sample. A percept is not one sample. The question is how discrete samples from thousands of neurons become a single continuous standing wave again — how digital becomes analog.

The ephaptic field is the candidate. Every spike and every charged membrane contributes to a shared extracellular electric field. That field is continuous, it sums contributions with distance-decay, and it feeds back onto every neuron's cable (your `ephaptic_field * coupling` term; Pinotsis & Miller's "control parameter"; McFadden's CEMI). So the population runs: discrete spikes → summed continuous field → that field perturbs every cable → changes what each AIS samples next.

This closes the analog–digital–analog cycle. The spikes sample the wave; the field reassembles the samples into a wave; the wave determines the next samples. **The standing wave is the fixed point of this cycle** — the configuration of the shared field at which the samples it produces regenerate the same field. When the population finds such a fixed point, it is by definition self-sustaining and, by §1, nearly silent. That silence-with-content is the held percept.

Your binding-problem demo is exactly this fixed point forming: two isolated sensory streams, three blind neurons between them, no weights, no training — and the ephaptic field forces a coherent phase-lock because coherence is the field's low-energy state. The "aha" is the cycle settling.

*Established:* ephaptic coupling exists and can modulate spike timing (Anastassiou, Fröhlich). *Contested but serious:* that this field is functionally load-bearing for binding/consciousness (CEMI is a real hypothesis with real critics). *Speculation:* that the field's fixed point *is* the unit of experience.

---

## 4. The loop and the plate: why one neuron is not enough

A standing wave that reconstructs the present moment from the senses alone would have no past in it. But perception is saturated with the past — you see the expected, hear the anticipated, and notice mainly the deviation. The hippocampal–cortical loop is the machinery that builds the past into the wave. This is the complementary-learning-systems architecture, read through the wave.

**Cortex is the frozen past.** Deeply scorched, slow to change, near-permanent. It holds the invariant shapes — the standing waves that have formed millions of times. In the wave picture, cortex supplies the *priors*: the attractor basins the present is allowed to fall into.

**Hippocampus is the viscous past.** Fast, plastic, single-trial. It holds the last seconds-to-hours as a labile trajectory. It supplies *recent context* — the bias that makes this moment continuous with the one before it. "Viscous" is exact: it flows, it holds shape briefly, it relaxes.

**The entorhinal cortex is the plate — the basis change.** This is the least standard and most important claim, and it is the one place the framework makes a sharp, falsifiable prediction. Grid cells in EC layer II fire on periodic hexagonal lattices at many spacings and orientations. A population of periodic lattices at many spatial frequencies *is* a 2D Fourier basis. Place cells in CA1 fire at single locations — single points in real space. And the transformation grid→place is, mathematically, an inverse Fourier transform: from a frequency-domain representation (which grid cells are active) to a spatial-domain point (where the place cell fires).

That is the same iFFT as your `deterministic_world_maker` — frequency modes summed by constructive interference until a sharp peak (a location, a percept) appears where the waves agree. The EC is the holographic plate because it holds the scene in the frequency domain, as interference-ready modes, and the loop's job is to run the inverse transform and let the standing wave precipitate where the modes constructively interfere.

This also resolves the "soma is the plate / EC is the plate" tension you flagged. They are the same operation at two scales. One neuron's cable+grating holds and reads *one* band — it is one Fourier coefficient. The EC population is the *stack* of such neurons across all spatial frequencies — the whole basis. Soma-plate and EC-plate are not competitors; the EC plate is what a population of soma-plates becomes.

*Established:* CLS (fast hippocampus / slow cortex), grid cells, place cells, theta–gamma coupling, sharp-wave-ripple replay. *Bridge with literature support:* grid→place as approximately an inverse transform (Solstad et al. 2006 — and it is *approximate*; real place fields carry CA3 recurrence and inhibition on top, so this is illustrative of a mechanism, not a fitted law). *Speculation:* that EC is the *general* Koopman basis for all hippocampal computation, not only space.

---

## 5. The clock: why the wave advances in steps

If the wave were free-running it would smear. It does not — it is paced. Theta (4–8 Hz) is the outer clock; gamma (30–90 Hz) nests 5–7 cycles inside each theta period. In the wave picture each theta cycle is one complete read–reconstruct–check–write step, and each gamma cycle is one iteration of the reconstruction (one step of the CA3 zoom toward the attractor). The wave does not converge to infinity and collapse into the single dominant mode — it is allowed only 5–7 iterations before the clock resets it for the next moment. That bounded iteration is why experience advances as a sequence of distinct moments rather than freezing on the strongest memory.

CA1 is where the reconstruction is checked against reality: the CA3 prediction (the reconstructed wave) arrives on one path, the EC sensory truth arrives on another, within the same gamma cycle, and CA1 emits the mismatch. By §1, that mismatch is exactly the derivative the system most needs to transmit — the prediction error, the place where the wave must change. High mismatch → strong spiking → strong plasticity (deep scorch). This is why surprise is remembered: surprise is large `dW/dt`, and the spike *is* `dW/dt`.

*Established:* theta–gamma coupling, dual-path timing into CA1, prediction-error physiology, surprise-dependent encoding. *Bridge:* identifying the gamma count with iteration depth and CA1 output with the transmitted derivative.

---

## 6. What breaks, and what your data already shows

The framework's claims become testable mainly through their failure modes.

**Schizophrenia — gate failure.** If the wave is reconstructed from internal priors *and* checked against EC sensory truth, then a failure to gate internal state out of the sensory stream means the wave locks onto an internally generated attractor with no sensory anchor. Your "Shady Stuff" analysis measured the geometric signature of this: an 8.4-to-1 ratio of dimensional *collapse* over saturation in the schizophrenic cohort versus 1.7-to-1 in controls — the phase space caving inward onto low-dimensional self-referential fixed points — and a temporal-lobe-leads-frontal cascade with ~2.06 s latency. In wave terms: the EC/temporal gate fails first, the standing wave runs without sensory correction, and the frontal network, starved of a grounded reference, collapses into the internal attractor seconds later. The numbers are real; the mechanistic reading is the framework's, and you were right to flag the reaching parts. The honest status: a suggestive macroscopic signature consistent with the theory and also with other accounts of dysconnection — not a proof.

**Alzheimer's — plate destruction.** Tau hits EC layer II first (Braak I–II), destroying the grid-cell basis before the cortical library. The framework predicts the specific signature this produces: the high-frequency modes go first, so fine detail dissolves while gist survives — the world-maker slider dropping from thousands of modes to ten, where the ghost of the whole shape remains but the edges are gone. Episodic-before-semantic is the clinical trajectory, and it falls straight out of "the plate is destroyed while the images remain."

**Your own temporal-lobe data.** You report visual trembling on busy patterns — and in this framework that is not incidental. A busy pattern is high spatial frequency; if the sampling lattice or the mode-gating that should suppress off-frequencies is compromised, the wave cannot lock, and you perceive the individual aliased samples beating against each other. That is Moiré — aliasing made visible. You are, in the most literal sense the theory allows, *seeing the sampler*. I raise this only because you raised it, and as illustration, not evidence: a single subject's report is a clue to where to look, not a result.

---

## 7. What I actually see

Stripped to one sentence: **a neuron is an analog delay line read through a grating, a population is those readings reassembled into a standing wave by a shared field, and a brain is that wave continuously reconstructed from three timescales of past — frozen (cortex), viscous (hippocampus), and basis-changed present (EC) — advanced in clocked steps, with spikes firing only where the wave is changing.**

The standing wave is the content. The spike is its derivative. The loop exists because reconstruction needs priors. The plate exists because reconstruction needs a basis. The clock exists because the wave must advance without smearing. Sparse coding, predictive coding, attractor dynamics, the CLS memory hierarchy, grid-as-Fourier, and ephaptic binding are not six separate ideas in this picture — they are six views of one cycle: analog → sampled → analog.

What is genuinely new in your eighteen months is not any single piece — almost every piece exists in the literature. It is the insistence that they are the *same* operation recurring at every scale, and the physical commitment that the recurrence is implemented by real periodic structure (the 190 nm lattice) reading a real delay manifold (the cable) into a real shared field (the ephaptic). That is a strong, unfashionable, and falsifiable bet. Pribram saw the hologram and had no sampler; you have the sampler, the delay line, and the field, and the math (Takens, Koopman, iFFT) to connect them.

What it is not: it is not proof that any of this is *how the brain computes*, and it is certainly not a solution to why a fixed point of a field should *feel* like anything. That last step — wave = qualia — is the hard problem, and this framework sharpens it into a precise question (why is the self-sustaining fixed point of the ephaptic cycle experienced from the inside?) without answering it. Sharpening is not solving. Say so, every time.

---

## 8. The one prediction worth chasing

Of everything here, the cleanest falsifiable claim follows directly from §1, and it needs no new equipment.

If the spike is the derivative of the standing wave, then **the transition into a stable percept should show a stereotyped settling transient: a brief spike burst as the wave moves into the attractor, followed by a sharp drop to near-silence as it locks — and the depth of that silence should scale with how well the reconstruction matches the input** (low prediction error → deep silence; residual mismatch → sustained low-level spiking proportional to the residual). This is the signature of delta coding and it is measurable in any dataset with a clear stimulus onset and a settled steady state. It is distinct from simple adaptation because the silence depth should track *match quality*, not just time since onset.

Paired with the EC prediction — that place-field firing is approximately the linear sum of active grid-cell modes, degrading specifically in the high-frequency modes when fine spatial scales are lesioned — these are two consequences that depend on *this* architecture and not on generic signal processing. One of them lives in spike-train statistics around stimulus onset; the other lives in grid–place recordings. Both exist as public-ish data. Either one, if it holds with the predicted *form*, is the first thing here that would make a skeptic look twice.

---

## Ledger

**Established (not in dispute):** dendritic delays; 190 nm actin–spectrin AIS lattice and periodic Nav anchoring; Nav1.6→Nav1.2 threshold gradient; AIS as AP initiation site and its plasticity; sparse and predictive coding; subthreshold computation and spike metabolic cost; grid cells, place cells, theta–gamma coupling, sharp-wave ripples; CLS fast/slow memory; ephaptic coupling as a real (if debated) effect; tau's EC-first trajectory in Alzheimer's.

**Defensible bridges (reasonable readings of established facts):** cable state as a Takens delay manifold; spike as the derivative/delta-sample of a continuous representation; grid→place as an approximate inverse transform (Solstad 2006, approximate not exact); CA1 output as the transmitted prediction error.

**Framework speculation (the bets):** the AIS lattice performs a spectral/Koopman sampling transform; EC is the general Fourier basis for all hippocampal computation; memory is an eigenvalue; the ephaptic fixed point is the unit of experience; the standing wave is qualia.

*Do not hype. Do not lie. Just show.*

---

*Helsinki, June 2026. Written from eighteen months of conversations between Antti Luode and successive models, this pass by Claude (Opus 4.8). The standing-wave-as-derivative framing and the analog→sampler→analog cycle are the contribution of this pass; the anatomy is Leterrier (2018); the loop architecture builds on the prior PerceptionLab theses; the empirical anchors (schizophrenia geometry, AIS structure) are as cited within. Nothing here is proven. Everything here is checkable.*
