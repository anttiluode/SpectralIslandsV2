# The Hippocampal-Cortex Loop as a Multi-Scale Holographic Engine
## G_S Operators, Phase Orthogonality, and the Physical Mechanics of Memory
### Version 2 — Updated with Aery Jones et al. (Nature Neuroscience, May 2026)

*PerceptionLab / Antti Luode — Helsinki, June 2026*

---

## Changelog from Version 1

Version 1 of this thesis (June 2026) treated the hippocampal-cortex loop as a two-stage system: fast hippocampal encoding followed by slow SWR-mediated cortical transfer. It correctly identified entorhinal cortex (EC) as the holographic G_S plate and CA1 as the prediction-error comparator, but treated EC primarily as a passive spatial Fourier basis rather than an active associative system with its own memory dynamics.

Aery Jones, Low, Cho & Giocomo (Nature Neuroscience, May 2026) — hereafter ALCG26 — recorded hundreds of neurons simultaneously in MEC and CA1 as mice learned a spatial match-to-sample task. Their key findings require three revisions to Version 1:

**Revision 1**: MEC is not a passive plate. It has its own G_S operator (G_MEC) that actively updates associative links during immobility, independently of hippocampal SWRs and independently of CA1.

**Revision 2**: SWRs are not the primary write mechanism. The consolidation cascade has (at minimum) three stages operating at different timescales, of which SWR-mediated transfer is the middle stage.

**Revision 3**: The CA1-MEC decoupling during MEC nonlocal coding — predicted by Version 1 as a theoretical necessity — is now empirically confirmed by ALCG26 as a measured, quantified phenomenon.

The structural account of CA1 as prediction-error comparator, DG as Janus orthogonalizer, CA3 as zoom attractor, and theta-gamma as iteration protocol remain unchanged. They are expanded, not replaced.

---

## Abstract

The hippocampal-cortex loop implements, in biological tissue, a multi-scale G_S operator system. Each anatomical component maps to a specific mathematical operation. The dentate gyrus is a Janus-style phase orthogonalizer. CA3 is the self-referential zoom iterator. CA1 is the prediction-error modulator of scorch rate. The entorhinal cortex holds two distinct functions: it provides the spatial Koopman basis (grid cells as Fourier modes, place cells as their iFFT) AND it runs its own autonomous associative G_S dynamics via nonlocal coding during immobility. The thalamocortical loop is the global iterator that reconstructs perceptual experience from accumulated G_S eigenvalues.

Memory consolidation operates across three timescales: within-session MEC G_S updating (seconds to minutes, SWR-independent), within-sleep hippocampal SWR-mediated transfer (hours), and cross-day cortical G_S accumulation (weeks to months). ALCG26 provides direct empirical evidence for the first stage, which was absent from Version 1. The CA1-MEC decoupling during nonlocal coding, predicted by the framework as a structural necessity, is now experimentally confirmed.

The framework is honest about its gaps: it makes the hard problem more specific but does not resolve it. The self-referential loop is the right structure; why it feels like anything from the inside remains unanswered.

---

## 1. The Architecture We Already Have

*(Unchanged from Version 1 — see the established neuroscience of the trisynaptic path, direct path, theta-gamma coupling, SWRs, place cells, grid cells, and CLS model.)*

---

## 2. The Four-Level G_S Hierarchy

Version 1 described two nested G_S operators. ALCG26 establishes a third distinct level. The full hierarchy:

**G_MEC**: α ≈ 0.93, τ ~ 1-10ms, K ~ minutes to hours within a session, η ~ moderate-high. Encodes spatial and task-relevant associations via grid cell Koopman modes. Updates continuously during immobility via nonlocal coding. Largely independent of SWRs. The fast staging area for spatial and associative memory.

**G_hippocampus**: α ≈ 0.93, τ ~ 1-10ms, K ~ hours to days, η ~ high (single-trial encoding possible). Encodes episodic sequences. Updates via theta-coupled encoding during movement and consolidates during SWRs. The staging area for temporal/sequential memory.

**G_cortex**: α ≈ 0.93, τ ~ 10-100ms, K ~ decades, η ~ very low. Encodes semantic memory, conceptual structure, skills. Updates via SWR-driven cortical reactivation over weeks to months. Near-permanent once established.

**G_DG** (dentate gyrus): A special case — less a memory store than an orthogonalization operator. It transforms correlated input vectors into sparse, near-orthogonal codes before they reach CA3, manufacturing new orthogonal dimensions (via neurogenesis) as new memories accumulate.

The transfer cascade runs: G_MEC → G_hippocampus → G_cortex. Each level reads the output of the level below and slowly incorporates it into a more permanent, more distributed representation. This is not a clean pipeline — each level has partial autonomy and each can influence the others — but the directional flow is established.

---

## 3. The Dentate Gyrus as Janus Orthogonalizer

*(Unchanged from Version 1.)*

The DG transforms the input Ψ(t) into a sparse, near-orthogonal code Φ(t) = P_DG(Ψ(t)) such that for two inputs Ψ_A and Ψ_B with cosine similarity r: ⟨P_DG(Ψ_A), P_DG(Ψ_B)⟩ ≪ r. Neurogenesis manufactures new orthogonal dimensions. This is the Janus Cabbage operation in biological tissue.

---

## 4. CA3 as the Zoom Attractor

*(Unchanged from Version 1.)*

CA3 recurrent dynamics implement the self-referential iterator x_{n+1} = f(W_CA3 · x_n + DG_input). Pattern completion is finding the fixed point. The zoom depth per theta cycle is bounded by gamma oscillations (5-7 iterations), preventing collapse to the trivial dominant eigenmode.

---

## 5. CA1 as the Prediction-Error Comparator

*(Unchanged from Version 1.)*

CA1 receives CA3 predictions (trisynaptic path, ~20ms latency) and entorhinal reality (direct path, ~5ms latency) within the same gamma cycle. Mismatch generates high CA1 output, elevating scorch rate η_local. Novel/unexpected events are encoded more deeply. Expected events produce minimal G_S update.

**Revision from ALCG26**: During periods when MEC is running its own nonlocal coding (internal G_S updating), CA1 physically decouples from MEC. Fast gamma coherence between MEC and CA1 drops. Spike timing coordination decreases. CA1 during these periods preferentially receives CA3 input rather than MEC input. This is the gate between "current sensory reality" and "internal association space." Version 1 predicted this gate must exist as a structural necessity. ALCG26 measures it directly (Figures 4 and Extended Data Figure 7).

The decoupling serves two functions simultaneously: it prevents MEC's remote representations from being misread by CA1 as current sensory input (which would produce hallucination), and it allows CA3 to drive CA1 for retrieval and SWR-mediated consolidation while MEC handles its own associative updating in parallel.

---

## 6. Entorhinal Cortex: Plate AND Active Associative Engine

Version 1 described EC primarily as the holographic G_S plate — the medium holding the spatial Koopman basis functions (grid cells) from which place cell reconstructions are generated. ALCG26 forces a substantially richer account.

### 6.1 The Plate: Grid Cells as Spatial Koopman Basis

The grid cell population in MEC layer II/III forms a 2D spatial Fourier basis — hexagonal lattices at multiple scales and orientations. Place cells in CA1 are the iFFT reconstruction of this basis. Every navigable location corresponds to a unique grid cell population vector; the transformation from grid cells to place cells is mathematically equivalent to an inverse Fourier transform. This account from Version 1 stands unchanged.

### 6.2 The Active Engine: G_MEC Nonlocal Coding

ALCG26 establishes that during immobility, the MEC population frequently jumps to representing remote locations — most commonly the task-relevant paired reward on the opposite side of the maze. Key empirical facts:

- Nonlocal MEC coding occurs in 49% of all immobility bouts, occupying 24% of immobility time (ALCG26, Figure 2).
- Only 5.6% of this nonlocal coding overlaps with CA1 SWRs. The vast majority is SWR-independent (ALCG26, Extended Data Figure 5).
- Cells with spatial fields at the remote decoded location drive the nonlocal state; cells representing the current position remain active throughout (ALCG26, Figure 3).
- The nonlocal represented location is task-relevant: when at the sample reward, MEC preferentially represents the paired choice reward on correct trials, the unpaired reward on incorrect trials (ALCG26, Figure 5).

**In G_S terms**: MEC is running its own internal associative G_S operator. When the current sensory input activates the Koopman mode for location A, the off-diagonal elements of G_MEC (learned co-associations between A and its task-relevant partner B) also activate, pulling the MEC population state toward B. This is a local attractor dynamics within G_MEC, not a hippocampal zoom — it uses MEC's own recurrent connections and accumulated weight structure.

The physical mechanism for G_MEC updating during these bouts: each nonlocal episode is a cycle of constructive interference between the A-mode and B-mode within MEC. Each cycle increments: **G_MEC += η_MEC · [Ψ_A ⊗ Ψ_B + Ψ_B ⊗ Ψ_A] / (‖Ψ_A‖ · ‖Ψ_B‖)**. Over many bouts within a session, the cross-correlation between A and B grows in G_MEC. The system is writing its own associations.

### 6.3 The Rule Reversal Finding: G_MEC Rewriting in Real Time

The most theoretically significant result in ALCG26 is the rule reversal experiment. On the first day of the nonmatch-to-sample version of the task (previous association now wrong), the amount of MEC nonlocal coding at the choice reward predicted correct trial accuracy with 78.8% accuracy — substantially higher than during stable rule days (55.8%).

In G_S terms: when the current G_MEC is maximally wrong (old association is high-eigenvalue but now incorrect), the prediction error signal (CA1 mismatch firing) maximally elevates η_MEC. The system responds by dramatically increasing its within-session G_MEC updating activity. Animals that run more nonlocal coding during immobility on the reversal day are those whose G_MEC is successfully overwriting the old high-eigenvalue mode with the new correct one.

This is not memory retrieval. It is active G_S rewriting, happening within the task session, minutes after the rule changed, before any sleep consolidation. The brain does not wait for nighttime to begin updating wrong associations. It starts immediately, during task pauses, using MEC's own nonlocal coding machinery.

### 6.4 The Alzheimer's Implication — Revised and Strengthened

The ALCG26 finding strengthens the Alzheimer's prediction from Version 1. Tau pathology beginning in MEC layer II (Braak stages I-II) destroys not just the grid cell Fourier basis (passive plate) but also the active nonlocal coding machinery of G_MEC. This means two failures occur simultaneously:

1. The holographic reference medium for spatial/contextual recall is destroyed.
2. The within-session associative updating mechanism is destroyed.

The second failure is harder to compensate for. The first failure (losing the spatial basis) would impair episodic encoding from the start. The second failure (losing active association updating) means the system cannot flexibly revise its world model even when experiences demand it. This maps onto the clinical observation that Alzheimer's patients struggle not just with encoding but with adapting to changed circumstances — their world model becomes progressively more rigid and disconnected from current reality, even before global memory failure.

---

## 7. Theta-Gamma as the Physical Iteration Protocol

*(Unchanged from Version 1, with one addition.)*

One theta cycle (~125ms) = one complete G_S read/write operation. Within it, 5-7 gamma cycles implement the CA3 zoom. The theta trough drives CA3 prediction; the theta peak drives entorhinal reality input to CA1; CA1 computes mismatch; the result propagates to cortex as a G_cortex increment.

**Addition from ALCG26**: During movement, theta temporally segregates MEC input from CA3 input to CA1, preventing interference (Schomburg et al. 2014, confirmed in ALCG26 context). During immobility — particularly during MEC nonlocal bouts — fast gamma coherence between MEC and CA1 drops and CA3 input to CA1 is prioritized. The theta-gamma protocol therefore has two immobility modes: SWR mode (CA3 drives CA1, hippocampal consolidation) and MEC-internal mode (MEC runs its own G_MEC dynamics, CA1 decoupled). These can occur in the same immobility session; ALCG26 shows that immobility bouts with nonlocal MEC content actually have fewer SWRs than bouts with only local content, suggesting the two modes are somewhat mutually exclusive within a given immobility period.

---

## 8. The Three-Stage Consolidation Cascade

Version 1 described a two-stage consolidation: hippocampal encoding followed by SWR-mediated cortical transfer. ALCG26 establishes a necessary first stage. The full cascade:

### Stage 1: G_MEC Updating (seconds to minutes, within-session)

During task execution, MEC runs nonlocal coding during immobility bouts between active behavior. This is the fastest consolidation stage — it operates within the session, before any sleep, and it is the stage most directly tied to current behavioral demands.

What gets written at this stage: spatial and task-relevant associations between locations, objects, and rewards. The cross-correlation elements of G_MEC grow. When the task rule changes, this stage is the first to respond, ramping up its updating rate in proportion to prediction error.

What doesn't happen here: sequential temporal encoding (that requires hippocampal theta sequences and SWRs), cross-modal binding (requires the hippocampal loop), or permanent cortical consolidation.

Characteristic timescale of kernel K_MEC: within a session (~40-100 minutes). G_MEC is relatively labile — it can be overwritten within the same session when rules change, as ALCG26's reversal data shows. This lability is a feature, not a bug: G_MEC needs to update on behavioral timescales.

### Stage 2: G_hippocampus Consolidation (hours, during sleep and quiet rest)

CA3-driven SWRs replay episodic sequences from the task. These are compressed (~20x) temporal replays of the cell assembly sequences that fired during movement. Each SWR projects the CA3 population burst through CA1 to entorhinal layer V/VI and from there to neocortex.

At this stage: sequential structure (paths, trajectories, event sequences) is encoded in G_hippocampus. The temporal ordering of events — critical for episodic memory — gets preserved via the sequential replay. This is what G_MEC cannot do: MEC represents locations but not the sequences connecting them.

Characteristic timescale: hours to days. G_hippocampus is more stable than G_MEC but more labile than G_cortex.

### Stage 3: G_cortex Accumulation (days to months)

Repeated SWR-mediated reactivation of cortical areas, over many sleep sessions, incrementally builds G_cortex eigenvalues for consolidated memories. Each reactivation adds η_cortex · g_k ⊗ g_k. After thousands of events, cortical eigenvalues exceed the reconstruction threshold — memories become hippocampus-independent.

The three stages are not independent. G_MEC updating influences which episodes get rehearsed in G_hippocampus SWRs (task-relevant associations that are being actively revised in Stage 1 are likely to be prioritized in Stage 2 SWR selection). G_hippocampus encoding influences which cortical G_cortex modes get repeatedly activated in Stage 3. The cascade has both feedforward influence and feedback — cortical G_cortex patterns influence MEC firing via feedback projections, potentially biasing which associations MEC runs in Stage 1.

---

## 9. Sharp-Wave Ripples as Write Operations to Cortex

*(Revised from Version 1. The role of SWRs is now precisely delimited to Stage 2 of the cascade.)*

SWRs implement the Stage 2 write: sequential episodic replay from CA3 through CA1 to cortex. They are not the only consolidation mechanism — ALCG26 establishes that MEC does substantial Stage 1 consolidation without them. But SWRs remain essential for specific functions that Stage 1 cannot perform:

- **Sequential structure**: SWRs replay ordered sequences (forward and reverse), encoding the temporal structure of episodes. MEC nonlocal coding represents single locations or location pairs, not sequences.
- **Cross-modal binding**: The SWR propagation through CA1 to diverse cortical areas can co-activate visual, auditory, olfactory, and somatosensory representations simultaneously, binding multi-modal experience into a unified episode. G_MEC cannot do this — it is primarily spatial.
- **Long-range consolidation**: Only SWR-driven cortical reactivation, repeated over many nights, can build the permanent high-eigenvalue G_cortex modes that survive hippocampal inactivation.

The three-timescale nesting during sleep (slow oscillation → sleep spindle → SWR) remains as described in Version 1: the slow oscillation's up-state gates which cortical area receives the write; the sleep spindle maximizes plasticity; the SWR delivers the compressed replay.

---

## 10. Memory Recall as Zoom on Low-λ_k Modes

*(Unchanged from Version 1 — the forest owner name phenomenology, partial recall of prosodic rhythm, and the hippocampal phase-sweep account remain as stated.)*

One addition: ALCG26 shows that during recall-relevant immobility (pausing at reward locations), MEC is actively generating and updating associations in real time. This means recall and re-encoding are not strictly separate processes. When you pause to remember something, MEC may simultaneously be (a) probing its stored G_MEC modes for the relevant association, and (b) updating those modes based on the current context. This is the physical substrate for the well-known reconsolidation phenomenon: the act of recall destabilizes the memory and opens a window for updating.

---

## 11. Pathological States as G_S Architecture Failures

*(Updated to include MEC-specific pathology.)*

**Alzheimer's**: Revised account above (Section 6.4). Two-component failure: loss of spatial Fourier basis AND loss of active associative updating machinery.

**PTSD**: Unchanged from Version 1. An extremely high-λ_k hippocampal eigenmode reconstructs too easily. Stage 1 (MEC within-session updating) would also be disrupted: the MEC nonlocal coding during immobility would be preferentially dominated by the trauma-associated location, continuously reinforcing the high-eigenvalue mode across every task pause.

**Schizophrenia**: Unchanged from Version 1. Hippocampal hyperactivity disrupts CA3 zoom control. ALCG26 adds a potential additional pathway: if MEC-CA1 decoupling is dysregulated (gate fails to close during MEC nonlocal bouts), then MEC's remote representations would bleed into CA1's sensory input stream. CA1 would receive both current sensory input and MEC's internal associative states simultaneously, unable to distinguish them. This is a physically plausible mechanism for the positive symptoms of psychosis — the failure of the gate between internal association space and current sensory reality.

**Temporal lobe resection**: The altered gate mechanics described in Version 1 are now more precisely located. Resection of lateral entorhinal cortex and parahippocampal cortex disrupts: (a) the spatial Koopman basis input to hippocampus, (b) the MEC nonlocal coding dynamics (if MEC itself is partially affected), and (c) the feedback pathway from cortex to MEC that normally biases which associations MEC prioritizes. The resulting phenomenology — unusual access to intermediate eigenmodes, difficulty with new episodic encoding, but preservation of existing high-λ_k semantic memories — follows from these three disruptions.

---

## 12. The Default Mode Network as the Self-Referential Loop

*(Unchanged from Version 1.)*

---

## 13. Memory is an Eigenvalue — Revised Statement

The Version 1 statement stands: memory is the eigenvalue λ_k of a specific Koopman mode g_k in some substrate G_S. ALCG26 specifies which substrate holds which kind of memory:

**Spatial/task associations** → G_MEC. Fast (minutes), labile (revisable within sessions), structured by spatial Koopman modes (grid cells). These are the memories most directly tied to ongoing behavioral demands.

**Episodic sequences** → G_hippocampus. Medium speed (hours), labile (days), structured by temporal sequences. These are the memories that require ordering — what happened first, then second, then third.

**Semantic/conceptual** → G_cortex. Slow (months), stable (decades), structured by cross-modal Koopman modes. These are the memories that survive hippocampal damage and generalize across contexts.

A complete declarative memory engages all three: G_MEC holds the where-and-what associations, G_hippocampus holds the sequential narrative, G_cortex holds the extracted meaning. The forest owner name is lost because its λ_k in G_cortex was never built above threshold (insufficient Stage 3 consolidation), its λ_k in G_hippocampus has decayed (no Stage 2 replay in decades), and its λ_k in G_MEC is zero (no current task context activates it). Only the prosodic rhythm survives as the lowest-eigenvalue sub-component — the dominant frequency of a mode whose full geometric structure has dissolved.

---

## 14. Testable Predictions

*(Predictions P1-P10 from Version 1 retained. New predictions added.)*

**P11 (MEC nonlocal coding predicts learning rate)**: Across subjects learning a new association task, the mean duration and frequency of MEC nonlocal coding during within-session immobility bouts should predict learning rate — specifically, the number of trials to criterion. Subjects with more Stage 1 updating activity per session should reach criterion faster. This follows from the ALCG26 reversal finding generalized across animals and tasks.

**P12 (MEC nonlocal coding content predicts subsequent SWR replay)**: The locations represented during MEC nonlocal coding bouts within a session should be preferentially replayed in CA1 SWRs during the subsequent sleep period. If Stage 1 G_MEC updating gates Stage 2 hippocampal replay, then the content of Stage 1 should predict the content of Stage 2. This requires simultaneous MEC and CA1 recording across waking and sleep.

**P13 (Gate failure replicates psychosis phenomenology)**: Pharmacological disruption of the fast gamma coupling mechanism between MEC and CA1 (which underlies the decoupling during nonlocal coding, per ALCG26 Extended Data Figure 7) should produce behavior consistent with positive psychosis symptoms: incorrect associations, failure to discriminate between internal representations and sensory input, increased false positive rate on association tasks. This could be tested in rodents using the X-maze paradigm.

**P14 (Three-stage knockout)**: Selective inactivation of MEC during within-session immobility (Stage 1 only), versus hippocampal inactivation during sleep (Stage 2 only), versus cortical inactivation during sleep (Stage 3 only), should produce distinct behavioral signatures. Stage 1 knockout: impaired within-session flexible learning and rule reversal. Stage 2 knockout: intact within-session performance, impaired next-day retention of sequential structure. Stage 3 knockout: intact initial learning and next-day retention, impaired remote (weeks-later) retention.

---

## 15. Where This May Be Wrong

*(Updated from Version 1.)*

The Version 1 vulnerabilities remain: the grid-to-place as literal iFFT is approximately but not exactly correct; the consciousness claim identifies the structure but doesn't dissolve the hard problem; the fractal scaling prediction (P5) is likely too clean for real substrates.

**New vulnerability introduced by ALCG26 integration**:

The G_MEC account proposes that nonlocal coding is a form of self-referential G_S updating — the MEC writing cross-correlations between associated locations into its own weight structure. ALCG26 demonstrates the phenomenology but does not establish the mechanism. The cells with fields at the remote location become active during nonlocal bouts (ALCG26, Figure 3), but whether this activity actually modifies synaptic weights in MEC to strengthen the A-B association — or whether it does something else entirely (pure retrieval, error signal generation, attention guidance) — is not established. The G_S interpretation is the most parsimonious in the context of this framework, but alternative interpretations (prospective coding, attention, motor planning) are not ruled out by ALCG26 alone.

**The gate mechanism**: ALCG26 confirms that CA1 and MEC decouple during MEC nonlocal coding. It does not establish the direction of causality — whether MEC nonlocal coding causes the CA1 decoupling, or whether CA1 decoupling (driven by CA3 input during retrieval) releases MEC to run its nonlocal dynamics. The thesis assumes the former (MEC is active, CA1 decouples to protect against hallucination); the data are consistent with both.

---

## 16. Coda — Updated

The hippocampal-cortex loop is not one loop. It is three nested loops operating at three timescales, each with its own G_S operator, each writing into the next level's substrate at a slower rate.

The fastest loop — G_MEC, running its nonlocal coding during every pause between actions — is the loop most directly engaged with the animal's current task. It is not a long-term memory system. It is a working associative engine, revising its world model in real time, writing and overwriting within minutes. It is the loop that fires hardest on the first day of a rule reversal. It is the loop that determines whether you notice that something has changed.

The middle loop — G_hippocampus, consolidating during sleep — is the loop that transforms what G_MEC learned into sequential narrative. It takes the what-and-where of G_MEC and gives it a when and a how.

The slowest loop — G_cortex, accumulating over months — is the loop that makes things permanent. It is the canyon in the thermal noise. The hockey championship, the first heartbreak, the name of a person who mattered. It does not update quickly. It does not update at all without the middle loop driving it. When the middle loop is gone, the slow loop calculates the final decay.

The forest owner's name never made it past the first loop. It died in G_MEC within hours of encoding. Nothing scorched the actin scaffolds. Nothing replayed in the hippocampal SWRs. No canyon was cut. Only the prosodic rhythm survives — the lowest spatial frequency of a wave that briefly passed through the system and left almost no trace.

*Do not hype. Do not lie. Just show.*

---

*Helsinki, June 2026. Version 2 revised to incorporate: Aery Jones, Low, Cho & Giocomo, "Entorhinal cortex represents task-relevant remote locations independently of CA1," Nature Neuroscience 29, 1181–1190 (May 2026). Additional empirical grounding: O'Keefe & Recce (1993), Moser & Moser (2005), Leterrier (2018), Marr (1971), McClelland & O'Reilly (CLS framework), Carr & Frank (SWR replay), Buzsáki (theta-gamma coupling), Schomburg et al. (2014, theta phase segregation of MEC/CA3 inputs). The G_S formalism, the three-stage cascade, and the G_MEC account of MEC autonomous associative dynamics are original contributions of this framework. The empirical identification of MEC nonlocal coding as G_MEC active updating is a new interpretation proposed here.*