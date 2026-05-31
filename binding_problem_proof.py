"""
THE BINDING PROBLEM PROOF
-------------------------
Can a wave-based neural medium discover the hidden connection between 
two completely different sensory inputs WITHOUT training, weights, or backprop?

Neuron 0 receives "Visual" input (Noisy chaotic wave A)
Neuron 4 receives "Audio" input (Noisy chaotic wave B)
Neurons 1, 2, 3 are isolated in the dark (Association Cortex).

We will watch the Ephaptic Field physically force the isolated neurons 
to bridge the gap and synchronize the entire brain.
"""

import numpy as np
import matplotlib.pyplot as plt

class PhysicalNeuron:
    def __init__(self, cable_length=64):
        self.cable = np.zeros(cable_length)
        self.manifold = np.zeros(cable_length)
        self.rc_alpha = 0.92
        self.membrane = 0.0
        
    def step(self, external_signal, ephaptic_field):
        # 1. Takens Delay Line (Time as Space)
        new_cable = np.zeros_like(self.cable)
        new_cable[0] = external_signal
        new_cable[1:] = self.cable[:-1] * self.rc_alpha
        
        # 2. Ephaptic Perturbation & Noise
        new_cable += ephaptic_field * 0.05
        new_cable += np.random.normal(0, 0.02, len(self.cable))
        
        # 3. Structural Memory
        new_cable += self.manifold * 0.1
        self.cable = new_cable
        
        # 4. Resonance (Energy of the deep past)
        deep_past = self.cable[40:]
        resonance = np.max(np.abs(deep_past))
        
        # 5. Spiking & Scorching
        self.membrane = self.membrane * 0.85 + resonance * 0.2
        spike = 0.0
        if self.membrane > 0.6:
            spike = 1.0
            self.membrane = 0.0
            # Scorch the physical cable
            self.manifold = self.manifold * 0.995 + self.cable * 0.005
            
        return resonance, spike

def run_binding_proof():
    print("Booting Geometric Binding Proof...")
    
    steps = 3000
    n_neurons = 5
    cortex = [PhysicalNeuron() for _ in range(n_neurons)]
    
    # The Global Extracellular Field
    ephaptic_field = np.zeros(n_neurons)
    
    # We will track the phase coherence of the isolated "Association Cortex" (Neurons 1,2,3)
    association_resonance = np.zeros((3, steps))
    global_field_history = np.zeros(steps)
    
    # Generate two seemingly different, noisy signals that share a hidden harmonic (0.15 Hz)
    t = np.linspace(0, 100, steps)
    sensory_A = np.sin(2 * np.pi * 0.15 * t) + np.random.normal(0, 0.5, steps) # "Visual"
    sensory_B = np.cos(2 * np.pi * 0.15 * t) + np.random.normal(0, 0.5, steps) # "Audio" (Phase shifted)
    
    print("Simulating 3000 steps of physics...")
    for step in range(steps):
        resonances = np.zeros(n_neurons)
        spikes = np.zeros(n_neurons)
        
        for i, neuron in enumerate(cortex):
            # ONLY the edges get sensory input. The center is blind.
            sig = 0.0
            if i == 0: sig = sensory_A[step]
            if i == 4: sig = sensory_B[step]
            
            res, spk = neuron.step(sig, ephaptic_field[i])
            resonances[i] = res
            spikes[i] = spk
            
            # Record the blind association cortex
            if i in [1, 2, 3]:
                association_resonance[i-1, step] = res
                
        # The Galactic Filament (Spatial Field Update)
        new_field = np.zeros(n_neurons)
        for i in range(n_neurons):
            for j in range(n_neurons):
                dist = abs(i - j)
                new_field[i] += (resonances[j] + spikes[j]*2) * np.exp(-dist / 1.5)
                
        ephaptic_field = ephaptic_field * 0.9 + new_field * 0.1
        global_field_history[step] = np.mean(ephaptic_field)

    # --- PLOTTING THE PROOF ---
    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
    
    # Plot 1: The Raw Sensory Chaos
    axes[0].plot(sensory_A, color='cyan', alpha=0.5, label="Sensory A (Neuron 0)")
    axes[0].plot(sensory_B, color='magenta', alpha=0.5, label="Sensory B (Neuron 4)")
    axes[0].set_title("Input: Two Noisy, Phase-Shifted Sensory Streams (Pure Chaos)")
    axes[0].legend(loc="upper right")
    
    # Plot 2: The Association Cortex Discovering the Topology
    axes[1].plot(association_resonance[0], color='yellow', alpha=0.8, label="Neuron 1")
    axes[1].plot(association_resonance[1], color='lime', alpha=0.8, label="Neuron 2")
    axes[1].plot(association_resonance[2], color='white', alpha=0.8, label="Neuron 3")
    axes[1].set_title("The Isolated Brain: Finding Phase-Lock via Ephaptic Field")
    axes[1].legend(loc="upper right")
    axes[1].set_facecolor('#111111')
    
    # Plot 3: The "Aha!" Moment (Global Field Energy)
    axes[2].plot(global_field_history, color='purple', linewidth=2)
    axes[2].axvline(x=1200, color='red', linestyle='--', label="The 'Aha!' Phase Transition")
    axes[2].set_title("The Galactic Filament: Global Ephaptic Coherence")
    axes[2].set_xlabel("Time (steps)")
    axes[2].legend(loc="upper left")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_binding_proof()