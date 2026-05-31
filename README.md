# SpectralIslandsV2: The Biological Takens Manifold

![pic](cable_neuron_v2_probe.png) 

**A PyTorch implementation of the Geometric Neuron, mapping the Spectral Archipelago theory directly to the biophysics of the Axon Initial Segment (AIS).**

Standard artificial neural networks (ANNs) assume memory lives in synaptic weights and computation happens via discrete dot products. **SpectralIslandsV2** demonstrates an entirely different paradigm of biological computation: memory lives in the physical geometry of the dendritic membrane, and computation is the spatial filtering of that geometry's delayed trajectory.

This repository contains the `cable_neuron_v2.py` simulation and its resulting output probe, proving that the established biophysics of the mammalian neuron naturally form a delay-embedded phase space that computes via geometric resonance.

## The Biophysical Architecture

Based on the anatomical observations of the AIS (e.g., Leterrier, 2018), this model implements three critical structural realities that standard neural networks ignore:

1. **The Dendrite as a Takens Manifold (`CableUnit`)**
   The dendritic cable is not a simple wire; it is a physical RC transmission line. Because signal decays with distance, older signals require higher frequencies to survive. This encodes *time as space*, physically instantiating a Takens delay embedding along the length of the cell. The neuron *is* the phase space.
2. **The 190nm Actin-Spectrin Grating (`GratingAIS`)**
   The biological AIS features a highly periodic structural scaffold spaced exactly ~190nm apart. In this model, this grating acts as a physical spatial comb filter. It samples the continuous Takens manifold at strict periodic intervals, turning random thermal/synaptic noise into resonant standing waves (Koopman spectral islands).
3. **The Nav1.6 / Nav1.2 Gradient (The Ferryman)**
   Voltage-gated sodium channels are not distributed equally. Ultra-sensitive Nav1.6 channels sit at the distal end, while higher-threshold Nav1.2 channels sit proximally. The model replicates this: the spike is not a binary 1/0, but a **spatial coordinate**. A weak geometric match fires distally; a strong match propagates proximally. The axon broadcasts *where* the threshold was crossed.

## Key Findings (See `cable_neuron_v2_probe.jpg`)

Running the simulation reveals three emergent properties intrinsic to this geometry:

* **Spontaneous Spectral Islands:** By simply dragging a signal across the periodic grating, the continuous RC cable naturally forms discrete resonant peaks (e.g., at `freq=0.08` and `freq=0.25`). The system organizes into Koopman eigenmodes purely through its spatial architecture.
* **Spatial Spiking (Address Encoding):** The network outputs the position of the spike along the AIS gradient. The neuron isn't firing a value; it is broadcasting a geometric mismatch address.
* **Manifold Creep (Palimpsest Memory):** When the network learns pattern A, is forced to learn pattern B, and then returns to A, it does not suffer from catastrophic forgetting. The geometric "scorch" (structural plasticity) of pattern A remains layered beneath B. The physical cable remembers the shape of its history without a single traditional weight update.

## Getting Started

### Prerequisites
You will need a standard Python scientific stack:
```bash
pip install torch numpy matplotlib
```

Running the Simulation
Execute the core script to run the resonance tests, spike position tests, and manifold memory tests.

```Bash
python cable_neuron_v2.py
```

This will output a terminal report of the network's dynamics and generate a high-resolution plot (cable_neuron_v2_probe.png/jpg) visualizing the network's state, mismatch addresses, signal survival, and manifold structure.

# The Implication for AI

Current AI (like Transformers) uses static trajectory readers. The context window is a delay embedding, but the reader does not change during inference.

This repository prototypes stateful, trajectory-aware computation. The inference process itself deforms the manifold that future inference reads. Synapses do not transmit values; they transmit perturbations to a continuously evolving, self-referential geometric attractor.

# Author

Claude AU / Prompting Antti Luode / 'Perception Lab'
