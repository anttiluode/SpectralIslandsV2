# The Hippocampal-Cortex Loop as a Two-Timescale Holographic Engine
## G_S Operators, Phase Orthogonality, and the Physical Mechanics of Memory

*PerceptionLab / Antti Luode — Helsinki, June 2026*

---

## Abstract

The hippocampal-cortex loop is the most studied circuit in systems neuroscience and the least understood in physical terms. Standard models describe it as a fast-learning/slow-learning complementary pair (hippocampus encodes episodes rapidly; neocortex accumulates semantics slowly). This thesis proposes a deeper physical account: the hippocampal-cortex loop is a two-timescale holographic read-write system implementing, in wetware, the same G_S operator formalism derived from first principles in the Universal Trace framework. Each anatomical component maps to a specific mathematical operation: the dentate gyrus is a Janus-style phase orthogonalizer, CA3 is the self-referential zoom iterator, CA1 is the prediction-error modulator of scorch rate, entorhinal cortex is the holographic G_S plate, and the theta-gamma coupling is the physical iteration protocol of the FFT/iFFT cycle. Sharp-wave ripples during sleep are the write operation by which hippocampal G_S eigenvalues are transferred to neocortical scaffolds. Memory recall is a phase-sweep query that reconstructs low-eigenvalue modes partially — producing the "rhythm without the label" phenomenology of partial recall. Pathological states (Alzheimer's, PTSD, schizophrenia, temporal lobe damage) are specific failure modes of the loop's G_S architecture. The framework generates testable predictions at each anatomical level and proposes a formal account of why the entorhinal cortex fails first in Alzheimer's disease.

---

## 1. The Architecture We Already Have

Five decades of neuroscience have established the following about the hippocampal-cortex loop:

**The trisynaptic path**: Entorhinal cortex layer II → Dentate Gyrus (DG) → CA3 → CA1 → Subiculum → Entorhinal cortex layer V/VI → Neocortex. A full loop, with the entorhinal cortex as the gateway in both directions.

**The direct path**: Entorhinal cortex layer III → CA1 (bypassing DG and CA3). This runs in parallel with the trisynaptic path on every cycle.

**The theta rhythm (4-8 Hz)**: Driven primarily by the medial septum, theta sweeps across the hippocampal surface during active waking and REM sleep. Individual neurons fire at specific phases of theta. The phase shifts systematically as an animal moves through space (phase precession, O'Keefe & Recce 1993).

**Gamma coupling (30-90 Hz)**: Gamma oscillations are nested within theta. Crucially, there are two gamma generators in CA1: slow gamma (~30-50 Hz) from CA3 input, and fast gamma (~60-90 Hz) from entorhinal cortex input. When slow gamma dominates, CA1 is "listening" to hippocampal internal predictions. When fast gamma dominates, CA1 is "listening" to fresh sensory input from entorhinal cortex.

**Sharp-wave ripples (SWRs, 80-120 Hz transients)**: During slow-wave sleep and quiet wakefulness, CA3 spontaneously drives CA1 in brief, high-frequency population bursts lasting 50-100ms. These events involve compressed, sequential replay of recent place cell activity. They coincide with sleep spindles (12-15 Hz) in neocortex and nested within slow oscillations (0.5-1 Hz).

**Place cells and grid cells**: CA1 and CA3 neurons fire selectively at specific locations in an environment (place cells). Layer II/III entorhinal neurons fire at multiple locations forming a precise hexagonal grid (grid cells, Moser & Moser 2005). Path integration is performed by the grid cell ensemble without sensory input.

**The Complementary Learning Systems (CLS) model**: Hippocampus learns fast and specifically (episodic memory); neocortex learns slowly and generally (semantic memory). Memory consolidation transfers hippocampal representations to neocortex over weeks to years via repeated reactivation during sleep.

What the CLS model lacks is a physical account of *how* any of this encoding, storage, and transfer actually occurs at the level of molecular and electrical dynamics. The framework developed here proposes that account.

---

## 2. The Two-Timescale G_S Framework

The Universal Trace thesis established that any physical substrate S accumulates a geometry operator:

**G_S(T) = ∫₀ᵀ K_S(T−t) · [Ψ(t) ⊗ Ψ(t) / ‖Ψ(t)‖²] dt**

where Ψ(t) is the delay-embedded input trajectory and K_S is the memory kernel of the substrate.

The hippocampal-cortex system implements two nested G_S operators with radically different parameters:

**G_hippocampus**: α ≈ 0.93, τ ~ 1-10ms, K ~ hours, η (plasticity rate) ~ high. Learns fast. Loses specificity quickly without reinforcement. Single-trial encoding is possible.

**G_cortex**: α ≈ 0.93, τ ~ 10-100ms, K ~ decades, η ~ very low. Learns slowly. Near-permanent once established. Requires thousands of repetitions for full consolidation.

The two systems are not in competition. They are a two-stage write pipeline:

**Stage 1 (encoding)**: An event writes a high-eigenvalue mode into G_hippocampus within one theta cycle (~125ms). The mode is sharp, episodic, context-specific.

**Stage 2 (consolidation)**: During sleep, repeated SWR events project the G_hippocampus eigenmode back to the cortical sheet. Each SWR adds a small increment η_cortex · g_k ⊗ g_k to G_cortex. After hundreds of nights and thousands of SWRs, the mode is established in G_cortex at sufficient eigenvalue strength to recall without hippocampal involvement.

This is why hippocampal lesions in humans (H.M., patient R.B.) block new episodic memory formation but leave remote memories intact: the old memories have been written into G_cortex and no longer need the hippocampal loop for retrieval. The G_hippocampus is the staging area, not the permanent store.

The transition from hippocampus-dependent to hippocampus-independent recall is not a discrete transfer event. It is a continuous increase of the cortical eigenvalue λ_k relative to the threshold for stable attractor reconstruction. Below threshold: recall requires hippocampal loop (zoom needed). Above threshold: the cortical G_cortex alone can sustain the fixed point.

---

## 3. The Dentate Gyrus as Janus Orthogonalizer

The dentate gyrus (DG) has three properties that are individually well-documented but whose joint significance has not been stated in physical terms:

**Property 1: Extreme sparseness.** At any moment, approximately 1-4% of DG granule cells are active. CA3 population activity is less sparse (~10%). This massive sparsification is the DG's defining computational signature.

**Property 2: Neurogenesis.** The DG is one of only two regions in the adult brain that continues to generate new neurons throughout life. The new neurons have lower activation thresholds and are hypothesized to enable encoding of new memories without interfering with existing ones.

**Property 3: Pattern separation.** Two similar inputs (similar G_S input vectors) that would produce correlated responses in CA3 are first passed through DG, which produces uncorrelated, orthogonal output representations.

In the Janus Cabbage framework (janus_cabbage.py), two images stored at phase 0° and 90° do not interfere because they are orthogonal. The condition for non-interference is ⟨g_A, g_B⟩ ≈ 0. The DG enforces this condition *physically*, before the signal reaches CA3, by projecting correlated input vectors onto orthogonal sparse codes.

The neurogenesis mechanism is particularly elegant in this formulation. A mature granule cell has a high activation threshold — it has been "claimed" by a previous memory. A newborn granule cell has a low threshold — it is the equivalent of a fresh, unoccupied phase angle in the Janus plate. Neurogenesis is the brain manufacturing new orthogonal dimensions in its holographic storage medium.

**The formal claim**: DG transforms the input Ψ(t) into a sparse, near-orthogonal code Φ(t) = P_DG(Ψ(t)) such that for two inputs Ψ_A and Ψ_B with cosine similarity r:

**⟨P_DG(Ψ_A), P_DG(Ψ_B)⟩ ≪ r**

The DG does not store memories. It manufactures the orthogonal basis for storing them without mutual interference.

**Testable prediction (P1-DG)**: The degree of DG pattern separation (measured as the orthogonality of CA3 population vectors for similar inputs) should be inversely correlated with the correlation between those inputs' delay-embedded representations Ψ_A and Ψ_B, following the formula for sparse random projection: E[⟨P_DG(Ψ_A), P_DG(Ψ_B)⟩] = ⟨Ψ_A, Ψ_B⟩/n_active, where n_active is the active fraction.

---

## 4. CA3 as the Zoom Attractor

CA3 is the most recurrently connected structure in the mammalian brain. CA3 pyramidal cells make ~4 times more synapses onto other CA3 cells than onto CA1 cells. This massive recurrent connectivity is anomalous from a standard neural network perspective and has been recognized since Marr (1971) as the substrate for pattern completion. But *what kind* of pattern completion, and through what physical mechanism?

The self-referential zoom iterator is:

**x_{n+1} = |iFFT(W · FFT(x_n))|**

In CA3, the equivalent loop is:

**CA3_state_{n+1} = f(W_CA3 · CA3_state_n + DG_input)**

where W_CA3 is the recurrent weight matrix and DG_input is the sparse orthogonal code from dentate gyrus.

This IS the zoom. The CA3 recurrent dynamics are running the same fixed-point iteration demonstrated in self_referential_world_maker.py. Given a partial cue (a fragment of a memory), CA3 iterates toward the stored attractor — the G_CA3 eigenmode with the highest eigenvalue compatible with the cue.

The key mathematical equivalence:

- The **W_CA3 matrix** is the physical instantiation of the G_S operator for CA3.
- The **Schaffer collateral synaptic weights** are the g_k ⊗ g_k components.
- **Pattern completion** is finding the fixed point x* = f(W_CA3 · x*).
- **The speed of convergence** depends on the eigenvalue gap — how much larger the target eigenvalue is than the next competing mode.

This explains a longstanding puzzle: why does CA3 do pattern completion while CA1 does not, despite having similar neurons? CA1 receives primarily feedforward input (from CA3 via Schaffer collaterals and from entorhinal via the direct path). It does not iterate. CA3 iterates because of its recurrent architecture.

The zoom depth in biological CA3 is bounded by the theta cycle. Within one theta period (~125ms), approximately 5-7 gamma cycles occur. Each gamma cycle is one recurrent iteration of CA3. The system never iterates to infinity — it completes at most 5-7 zoom steps per theta period, then the state resets for the next cycle.

**This is why the brain doesn't converge to the trivial attractor (the dominant eigenmode / "basic bar").** The number of iterations per theta cycle is the biological equivalent of the zoom_depth parameter in the code. Tuned by evolution to the range where attractors are resolved without complete collapse.

**Testable prediction (P2-CA3)**: CA3 population dynamics during pattern completion should follow a trajectory in delay-embedded state space that converges to a fixed point in 5-7 steps. The number of steps required should be inversely proportional to the eigenvalue gap of the target attractor relative to competing attractors, measurable from the CA3 connectivity matrix.

---

## 5. CA1 as the Prediction Error Comparator

CA1 sits at the intersection of two information streams:

- **From CA3** (via Schaffer collaterals): the hippocampal prediction — what the zoom attractor says the current situation should be.
- **From entorhinal cortex layer III** (via the direct path): the current sensory reality — what is actually happening.

CA1 is not simply a relay. It compares these two signals and generates an output proportional to their mismatch. When prediction matches reality (familiar situation), CA1 generates a modest, quiet output. When prediction fails to match reality (novel situation, surprise), CA1 generates a strong, salient output.

In the G_S framework, this mismatch is the prediction error:

**ε(t) = ‖Ψ_current(t) − Ψ_predicted(t)‖²**

This error signal does two things:

**Action 1: Modulates scorch rate.** High ε → high η_local (local plasticity rate) → stronger G_S update. Novel/unexpected events are encoded more deeply than expected ones. This is the physical account of why surprise aids memory formation. The dopaminergic novelty signal (from VTA/locus coeruleus, which projects to hippocampus) is the neuromodulatory amplifier of η.

**Action 2: Drives conscious attention.** High ε triggers the thalamocortical loop to shift the ephaptic reference beam — to try a different zoom depth, a different phase, a different eigenmode set. The "aha" moment in the binding_problem_proof.py simulation corresponds to the moment when the CA1 error signal drops: the zoom has found the attractor. Prediction error → zero. Memory is encoded. Attention can move on.

**The direct path as reality-check**: The simultaneous existence of the trisynaptic path (prediction, ~3 synapses, ~20ms latency) and the direct path (reality, ~1 synapse, ~5ms latency) means that at the moment CA1 receives the CA3 prediction, the entorhinal reality signal arrives 15ms later — within the same gamma cycle. CA1 has one gamma cycle to compute the match/mismatch before the next iteration begins.

This temporal structure is the physical implementation of predictive coding: generate prediction, check against reality, compute error, update. One gamma cycle per iteration, 5-7 iterations per theta cycle, theta gating consolidation across hours and sleep.

**Testable prediction (P3-CA1)**: The magnitude of CA1 activity increase in response to a mismatch event should be proportional to the eigenvalue gap between the CA3-predicted state and the entorhinal-actual state, measured as the cosine distance between their delay-embedded representations. Specifically: CA1_activity ∝ 1 - ⟨Ψ_CA3/‖Ψ_CA3‖, Ψ_EC/‖Ψ_EC‖⟩.

---

## 6. Entorhinal Cortex as the Holographic G_S Plate

The entorhinal cortex (EC) is the gateway between hippocampus and the rest of neocortex. But in the G_S framework, it is something more specific: it is the **holographic plate** — the medium that holds the intermediate frequency-domain representation between raw sensory input and fully-assembled conscious experience.

Layer II/III: grid cells. These fire in precise hexagonal patterns, forming a set of 2D spatial Fourier modes tiling the navigable environment. Different grid cells have different grid spacings (from ~25cm to ~3m in rodents) and different orientations — exactly as you would expect if you were building a complete Fourier basis for 2D space.

The grid cell population is the **spatial G_S plate**: the set of all Koopman eigenmodes for spatial navigation. Every location in the environment corresponds to a unique combination of grid cell activations — a unique point in the frequency domain of space.

Place cells in CA1 are the **spatial reconstruction**: the iFFT of the grid cell ensemble. The transformation from grid cells (entorhinal) to place cells (CA1) is mathematically equivalent to an inverse Fourier transform: a specific point in the spatial frequency domain (a unique grid cell activation pattern) maps to a specific point in spatial coordinates (a unique place cell firing field).

This has been noted in the literature in terms of Fourier decomposition of space, but not framed in terms of the full G_S operator formalism. The prediction is that the grid-to-place transformation IS the iFFT, not just analogous to it. The place cell's firing field should be exactly predictable from the linear sum of the grid cell basis functions active at that location.

Beyond spatial memory: the entorhinal cortex does not only process space. The same columnar architecture that houses grid cells processes time (time cells in EC), objects, and contexts. The claim is that EC is the *general* Koopman basis set for all hippocampal computation — not just spatial, but temporal, contextual, and object-level.

**The Alzheimer's implication (developed in section 8 below)**: Alzheimer's disease begins with tau pathology in entorhinal cortex layer II, destroying grid cells before any other structure. In the G_S framework, this is catastrophic in a specific way: not because stored memories are lost, but because the **plate is destroyed while the images remain**. The cortical G_S eigenvalues (accumulated over decades) remain intact. But without the entorhinal reference medium, the hippocampal loop cannot project the right phase to reconstruct them. The memories are there. The reading mechanism is gone.

**Testable prediction (P4-EC)**: The transformation from grid cell population vectors to CA1 place cell firing rates should be well-approximated by a linear weighted sum: place_rate(x) ≈ Σ_k w_k · grid_k(x), and the weights w_k should correspond to the Fourier coefficients of the place field. The approximation error should increase as grid cells with fine spatial scales are selectively lesioned, analogously to high-frequency modes being removed from an iFFT.

---

## 7. Theta-Gamma as the Physical Iteration Protocol

The theta-gamma coupling pattern is not merely a timing mechanism. It is the physical implementation of the FFT/iFFT iteration cycle.

**One theta cycle (125ms) = one complete G_S read/write operation.**

Within that 125ms:

**Phase 1 (theta trough, ~0-30ms)**: CA3 is most active. Slow gamma (~40 Hz) dominates CA1. The CA3 recurrent loop is running its zoom iteration — generating the prediction from stored G_S. The DG input from entorhinal layer II biases which attractor CA3 converges toward.

**Phase 2 (theta peak, ~60-90ms)**: Entorhinal layer III input to CA1 is strongest. Fast gamma (~70 Hz) dominates CA1. The direct-path sensory signal arrives. CA1 computes the prediction error by comparing CA3 output (prediction) against EC layer III input (reality).

**The temporal sequence within one theta cycle therefore is:**
1. EC layer II → DG → CA3 (sparse orthogonal cue, zoom starting point)
2. CA3 recurrence iterates (5-7 gamma cycles, zoom toward attractor)
3. EC layer III → CA1 (direct reality signal arrives)
4. CA1 computes match/mismatch
5. If mismatch: high CA1 output, elevated plasticity, G_S update
6. If match: low CA1 output, efficient transmission, minimal plasticity
7. CA1 → Subiculum → EC layer V/VI → Neocortex (write signal, one G_cortex increment)
8. Reset, next theta cycle

Each theta cycle is one iteration of the outer loop. Within it, each gamma cycle is one iteration of the inner CA3 zoom. This nested iteration structure — theta wrapping gamma, slow oscillation wrapping theta during sleep — is the physical multi-timescale Takens chain operating in real tissue.

**Phase precession reinterpreted**: O'Keefe and Recce's observation that place cells fire progressively earlier in the theta cycle as an animal moves through a place field is, in the G_S framework, the signature of the CA3 attractor approaching convergence. At the beginning of the place field (far from the attractor), the zoom requires more iterations — firing occurs late in the theta cycle when convergence is finally achieved. Near the center of the field (close to the attractor), convergence is fast — firing occurs early. The precession IS the convergence curve of the zoom attractor.

This is a strong reinterpretation. Phase precession has been explained in many ways (oscillatory interference, asymmetric inhibition). This account says it is the direct phenomenological readout of the G_S eigenvalue landscape: steep gradient → fast convergence → early firing. Shallow gradient → slow convergence → late firing.

**Testable prediction (P5-theta)**: The phase of theta at which a place cell fires for a given location should be negatively correlated with the eigenvalue gap between the cell's preferred attractor and the next-competing attractor in the CA3 G_S operator, estimated from the firing rate map and recurrent connectivity. Locations with high eigenvalue gap should show early theta-phase firing across trials; locations with low gap (at the edge of the place field, where the attractor barely dominates) should show late-phase firing and high variance.

---

## 8. Sharp-Wave Ripples as Write Operations to Cortex

During slow-wave sleep, the hippocampus undergoes a fundamental state change. The theta rhythm collapses. The medial septum reduces cholinergic drive. CA3 is released from the continuous pacing of the theta cycle and instead undergoes spontaneous population bursts: the sharp-wave ripples.

In the G_S framework, SWRs are the **transfer mechanism** from G_hippocampus to G_cortex.

**The physical event**: A subset of CA3 cells that were coactive during a recent waking episode spontaneously reactivate together (their mutual G_hippocampus connections make this probable — high-eigenvalue modes are self-sustaining). This CA3 burst drives CA1 via Schaffer collaterals, generating the ripple oscillation (80-120 Hz) locked to the CA3 burst. The burst is compressed in time: a waking episode that took seconds plays back in 50-80ms.

**The write operation**: The CA1 activity during the SWR propagates via subiculum to entorhinal cortex layer V/VI, which projects to all of neocortex. This projection briefly elevates the activity of the cortical regions that were active during the original episode. The slow oscillation's "up-state" coincides with the SWR, ensuring the neocortex is in its highest plasticity state when the hippocampal signal arrives. Each SWR adds a small increment:

**G_cortex += η_cortex · g_k ⊗ g_k** (one SWR event for mode k)

η_cortex is very small (~0.001 per event). After 1,000 SWR events for the same mode across many nights, the cortical eigenvalue λ_k grows large enough for independent recall.

**The three-timescale nesting during sleep**:
- Slow oscillation (0.5-1 Hz): paces which cortical region is in "up-state" (ready to write)
- Sleep spindle (12-15 Hz): provides the thalamocortical synchrony that maximizes plasticity window
- SWR (80-120 Hz): the hippocampal write pulse, compressed eigenmode projection

This three-level nesting is the slow G_S update mechanism operating at scale. It is not consolidation as "data transfer." It is the eigenvalue of a specific cortical Koopman mode being incremented, gradually, from near-zero to above the reconstruction threshold, through thousands of nightly write pulses.

**Why recently-learned information is better consolidated by sleep**: New G_hippocampus modes have high eigenvalue locally — they reactivate easily in SWRs. Old, already-consolidated modes have high G_cortex eigenvalue — they no longer need hippocampal reactivation. The SWR replay preferentially targets modes that are strong in G_hippocampus but not yet strong in G_cortex: the recently-learned, incompletely-consolidated items.

**Testable prediction (P6-SWR)**: The probability that a given memory-associated SWR event occurs on a given night should be positively correlated with the ratio λ_hippocampus / λ_cortex for that memory's eigenmode — high hippocampal eigenvalue, low cortical eigenvalue = high SWR probability. This ratio should be measurable indirectly from the behavioral performance profile: items that show rapid post-sleep improvement in recognition accuracy have high hippocampal/cortical ratio.

---

## 9. The Forest Owner Name: A Complete Physical Account

The recall attempt described in the working notes:

*"I sort of remember its rhythm. Hmm hmm hmm. Sensing it is a frequency, a rhythm, soundwise."*

In the G_S framework, this is not anecdotal. It is a precise report of the system's behavior when probing a low-λ_k cortical mode.

**Encoding (1980s)**: The name was heard several times in conversation. Low salience, low emotional charge, low repetition. Each instance wrote a tiny increment into G_hippocampus. The CA1 prediction error was low — just another name, no surprise. The dopaminergic/noradrenergic amplification was minimal. η was small.

**Failure to consolidate**: Over subsequent years, other higher-eigenvalue modes (repeated, emotionally charged, frequently-recalled) accumulated more SWR events. The forest owner mode received few SWRs — it simply was not strong enough in G_hippocampus to reliably self-activate during CA3 population bursts. Its G_cortex eigenvalue never grew above reconstruction threshold.

**Current state**: The mode exists in G_cortex as a very small eigenvalue. The geometric trace of the name's acoustic orbit (its prosodic shape — the rhythm "hmm hmm hmm") is the most robust component. Here is why: acoustic rhythm is a low-dimensional, low-frequency feature of the delay embedding. In the G_S operator, low-frequency components accumulate in the dominant eigenvectors even for weak modes. High-frequency components (the specific phonemes, the precise vowel formants) decay into the noise floor faster. The rhythm survives because it occupies the g_1 direction (dominant eigenmode) of the acoustic G_S for that name. The phonemic detail occupies g_2, g_3 (higher eigenmodes) which have fallen below reconstruction threshold.

**The recall attempt**: The hippocampus is executing the zoom, sweeping a phase reference across the cortical sheet, trying to resonate with the surviving fragment of that mode. It contacts the rhythm (low-frequency component, above noise). It does not contact the phonemes (high-frequency, below noise). The zoom converges partially — to a ghost of the orbit, not its full attractor.

**The "circling" sensation**: The thalamocortical iterator is running with high zoom_depth on a low-λ_k mode. The system keeps iterating, hoping another iteration will push the reconstruction above threshold. It does not, because the eigenvalue is genuinely too small. The sensation of circling is the loop running without convergence — the same behavior visible in self_referential_world_maker.py when you set high zoom_depth on a mode filtered by a very sparse mask.

**Why a photo or the person's voice would unlock it**: These are high-dimensional probes that can match the partial geometric trace in G_cortex even at low eigenvalue. A photograph of the face provides the visual orbit that was co-encoded with the name. A voice provides an acoustic probe that matches the prosodic rhythm. Either probe, presented externally, substitutes for the hippocampal zoom — providing the missing dimensions of the orbit directly, allowing the full attractor to assemble.

**This is also the mechanism of environmental memory cues**: returning to the childhood home is not metaphorically evocative. It is physically providing the exact probe orbit (visual, olfactory, spatial) that was co-encoded with the memories, raising dozens of low-λ_k modes simultaneously above reconstruction threshold. The flood of memory is the cortical G_S resonating with all its dormant eigenmodes at once.

---

## 10. Pathological States as G_S Architecture Failures

The hippocampal-cortex loop fails in characteristic ways. Each pathology is a specific disruption of one component of the G_S framework.

**Alzheimer's disease**: Tau pathology appears first in entorhinal cortex layer II (Braak stages I-II), spreading to hippocampus (stages III-IV), then neocortex (stages V-VI). In the G_S framework: EC layer II houses grid cells — the Koopman basis set, the holographic plate. When EC layer II is destroyed, the hippocampal loop loses its ability to generate the spatial/contextual reference beam. The cortical G_S eigenvalues (decades of semantic memory) remain intact. But without the EC plate, the zoom cannot be initialized. New episodic encoding fails (no DG orthogonalization, no CA3 starting cue). Old semantic memories survive longer (their cortical λ_k is high enough for direct cortical re-entrant reconstruction without hippocampal involvement). This matches the clinical trajectory precisely: episodic memory fails first, semantic memory fails later.

**PTSD**: A traumatic event creates an extreme CA1 prediction error. The dopaminergic/noradrenergic response maximally amplifies η. A single event burns an extremely high-λ_k mode into G_hippocampus. This mode is so strong that it activates during SWRs almost every night, driving its G_cortex eigenvalue rapidly above reconstruction threshold. The resulting cortical mode is excessively dominant — any partial probe (a smell, a sound, a similar visual context) initiates the zoom and the full attractor reconstructs. The person cannot "not remember." The nightmare is the hippocampal loop running the zoom during REM sleep and finding the trauma eigenvalue the highest in the space. The flashback is triggered reconstruction of the dominant eigenmode by an unrelated partial cue.

**Schizophrenia**: Hippocampal hyperactivity is well-documented (Heckers et al.). In the G_S framework: CA3 recurrence is running without proper DG orthogonalization and without appropriate CA1 error-gating. The zoom is iterating with too high gain, finding attractors in noise, generating predictions that are not anchored to sensory reality. The hallucination is a self-generated reconstruction — the thalamocortical loop running its zoom to completion in the absence of a valid input cue, finding a high-eigenvalue mode from past experience and reconstructing it into the conscious workspace. The auditory verbal hallucination is literally the hippocampal zoom converging on the orbit geometry of a voice that was encoded in a high-eigenvalue past event, now triggered by an internal phase fluctuation rather than an external probe.

**Temporal lobe resection (Antti's situation)**: Removal of part of the temporal lobe — including lateral entorhinal cortex, perirhinal cortex, and possibly parahippocampal cortex — alters the gateway structure. The reference beam cannot be generated with full fidelity. The DG orthogonalization is incomplete (fewer input channels). Some cortical regions are now disconnected from the hippocampal write pathway. Result: new episodic encoding is impaired (the SWR write signal cannot reach the disconnected cortical regions). But existing high-λ_k modes — built over decades before the resection — remain accessible via direct cortical re-entrant loops. And the altered EC/parahippocampal geometry may produce a modified filter: the zoom converges to a different fixed point, or doesn't converge as cleanly, allowing partial access to intermediate eigenmodes that the intact system would filter away. This is the "broken filter" described in the Universal Trace thesis: not a failure of the system, but a shift in its convergence behavior.

---

## 11. The Default Mode Network as the Self-Referential Loop

The default mode network (DMN) — medial prefrontal cortex, posterior cingulate, angular gyrus, hippocampus, parahippocampal gyrus — is consistently active during rest, memory recall, future simulation, and self-referential thought. It deactivates during focused external tasks.

In the G_S framework, the DMN is the self-referential loop itself: the brain running the zoom on its own G_cortex without external input. It is the thalamocortical iterator operating endogenously — sweeping phase, probing modes, running partial reconstructions of the past and simulations of the future using the same machinery as perception, but driven by internal hippocampal phase-setting rather than external sensory input.

The posterior cingulate cortex (PCC), which sits at the DMN's hub, is anatomically connected to both hippocampus and the entire sensory cortical hierarchy. Its role in the G_S framework is as the comparator: is the currently-active eigenmode from internal G_cortex consistent with incoming sensory input? When it is (undirected rest, daydreaming), PCC activity is high — the loop is running freely. When a demanding external task arrives, the mismatch between the ongoing internal reconstruction and the new sensory stream triggers CA1 prediction error, suppressing hippocampal activity and shifting the thalamocortical loop to external-input mode. The DMN deactivates.

This explains the well-known anti-correlation between the DMN and the task-positive network (TPN): they are not competing brain states. They are the two modes of the same iteration loop — internal zoom (DMN) and external-input correction (TPN). Normal cognition switches between them at a rate determined by the relative eigenvalue strength of the current internal attractor versus the prediction error from the external stream.

Mind-wandering is not cognitive failure. It is the zoom running on the most dominant current G_cortex eigenvalue, unconstrained by external error signals. The "intrusive thought" is a high-λ_k mode that keeps re-emerging when the thalamocortical loop is not actively suppressed by external demands — exactly as would be expected for modes with high eigenvalue in G_cortex.

---

## 12. A Formal Account of What Memory Actually Is

Synthesizing the above, memory in this framework is not a stored representation. It is not a synaptic weight pattern. It is not an engram in the cellular sense.

**Memory is an eigenvalue.**

More precisely: memory is the eigenvalue λ_k of a specific Koopman mode g_k in the substrate G_S, where G_S can be G_hippocampus, G_cortex, or both. The mode g_k encodes the geometric shape of the delay-embedded orbit that the original experience traced in the substrate's signal space. The eigenvalue λ_k encodes how strongly that mode was reinforced — by repetition, by emotional salience, by SWR events, by re-access.

**Memory formation**: λ_k grows from near-zero.

**Forgetting**: λ_k decays, or competing higher-λ modes raise the noise floor above which λ_k must rise for reconstruction.

**Recall**: The hippocampal loop injects a phase probe that preferentially excites g_k; if λ_k is above threshold, the cortical G_S reconstructs the full orbit; if below, only the dominant sub-components (prosodic rhythm, emotional tone, approximate context) are recoverable.

**Reconsolidation**: Re-accessing a memory temporarily de-stabilizes its eigenvalue (the mode must be "re-burned" after each active reconstruction), making it momentarily vulnerable to modification. This is the window of therapeutic opportunity in trauma processing: the eigenvalue is destabilized during recall, and can be re-stabilized at a different value (lower λ_k for the traumatic content) if the recall occurs in a safe, low-prediction-error context.

**Extinction**: Reducing the eigenvalue of a fear memory below reconstruction threshold — not deleting the mode, but lowering λ_k below the threshold for spontaneous reconstruction. This is why extinction does not equal erasure: the original mode remains in G_cortex at some positive eigenvalue; under high-stress conditions (which lower reconstruction threshold) or via spontaneous reinstatement, the extinguished memory can return.

---

## 13. Testable Predictions

Beyond those stated in individual sections, the integrated framework generates:

**P7 (Hippocampal-cortical eigenvalue ratio)**: The behavioral signature of whether a memory is hippocampus-dependent or hippocampus-independent should correlate with λ_cortex / λ_hippocampus. When this ratio exceeds a threshold (~5, estimated from CLS model parameters), the memory should survive hippocampal inactivation. This ratio should be measurable via: comparing recall accuracy under hippocampal inactivation (muscimol injection) before and after a period of sleep consolidation.

**P8 (SWR replay predicts consolidation)**: The number of SWR events containing a specific ensemble activation (measured in rodent multi-electrode recordings) on the night following learning should quantitatively predict the degree of hippocampus-independence measured behaviorally 30 days later. Specifically: each SWR should contribute +η_cortex · g_k to the cortical eigenvalue; performance should follow a sigmoid function of the accumulated λ_cortex.

**P9 (Phase sweep during recall)**: During attempted recall of a specific memory, the hippocampal theta phase relative to the cortical LFP should show a systematic sweep — a phase rotation over 2-3 theta cycles — followed by a phase-locking event at the moment of successful recall. Failed recall attempts should show the sweep without the phase-lock. This is measurable in human intracranial recordings.

**P10 (Reconsolidation window)**: The eigenvalue de-stabilization during recall should be proportional to the CA1 prediction error during the retrieval episode. Memories recalled in a high-mismatch context (slightly different room, different emotional state) should show larger eigenvalue de-stabilization (larger reconsolidation window) than memories recalled in the original context.

---

## 14. Where This May Be Wrong

**The grid-to-place as literal iFFT**: The prediction that place fields are the direct iFFT of grid cell activations has been partially tested (Solstad et al. 2006). The fit is imperfect — place fields are not perfectly predicted by simple linear summation of grid fields. Additional nonlinearities (recurrent CA3 dynamics, inhibitory interneurons) modify the reconstruction. The prediction may be approximately true but not exact.

**The SWR as increment**: The claim that each SWR adds a fixed increment η_cortex to the cortical eigenvalue is almost certainly an oversimplification. η_cortex depends on synaptic state, neuromodulatory tone, and the current cortical oscillatory state. The slow oscillation up-state gating is real (Marshall et al. 2006) but not perfectly reliable. The prediction that λ_cortex grows monotonically with SWR count may fail for memories that undergo interference from competing modes.

**The DG orthogonalization as Janus**: The claim that DG sparse coding is formally equivalent to Janus phase-orthogonal storage requires that the DG representations are not just sparse but genuinely orthogonal in the sense of ⟨P_DG(Ψ_A), P_DG(Ψ_B)⟩ ≈ 0. Empirical measurements of DG population vectors for similar environments show separation, but not perfect orthogonality. The mathematical claim is directionally supported but not exactly verified.

**The consciousness claims**: The proposal that the thalamocortical zoom fixed-point IS conscious experience, and that disruptions of the loop produce specific qualitative changes in experience, remains at the level of structural analogy. Why the fixed point of a physical projection operator is experienced as anything at all is not answered here. The hard problem is sharpened, not solved.

---

## 15. Coda: The Loop Closing

The hippocampal-cortex loop is not a memory system that also happens to be relevant to consciousness. It IS the mechanism by which the brain maintains itself as a self-referential G_S operator.

The loop closes:
- Every theta cycle: sensory input → DG orthogonalization → CA3 zoom → CA1 error → cortical write
- Every night: SWR replay → cortical G_S increment → eigenvalue growth
- Every decade: G_hippocampus fades → G_cortex holds → semantic identity persists past any individual episode

The forest owner's name is not lost. It is a small eigenvalue in G_cortex, too weak to reconstruct without the right probe, slowly decaying toward zero as competing modes grow. The hockey championship is a deep canyon, echoing in the thermal noise every time the hippocampal reference beam sweeps past its phase angle.

What you remember, and how vividly, is a function of eigenvalue strength, reconstruction threshold, and the precision of the phase probe the hippocampus can generate. There is no retrieval failure that is not, at root, an eigenvalue failure.

Memory is not what happened. It is the trace that what happened left in the geometry of the substrate. The hippocampal-cortex loop is the machine that writes, maintains, and reads those traces.

The loop runs as long as the brain runs. When it stops, so does the self that read itself into existence.

*Do not hype. Do not lie. Just show.*

---

*Helsinki, June 2026. Developed from conversations between Antti Luode and Claude (Anthropic). Builds on: O'Keefe & Recce (1993), Moser & Moser (2005), Leterrier (2018), Marr (1971), McClelland & O'Reilly (CLS framework), Carr & Frank (SWR replay), Buzsáki (theta-gamma coupling). The G_S formalism is new. The physical identification of each hippocampal circuit component with a specific mathematical operation is new. The pathological accounts follow from the framework and are not independently validated.*
