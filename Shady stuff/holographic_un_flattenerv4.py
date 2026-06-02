import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import butter, filtfilt, hilbert
import mne
import json
import os
import glob

# Suppress excessive MNE terminal output
mne.set_log_level('WARNING')

# --- MATHEMATICAL CORE (G_S Framework) ---

def butter_bandpass(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    safe_highcut = min(highcut, nyq - 0.1)
    safe_lowcut = max(lowcut, 0.1)
    
    if safe_lowcut >= safe_highcut:
        raise ValueError(f"Your sampling rate ({fs}Hz) is too low to look for frequencies up to {highcut}Hz.")
        
    b, a = butter(order, [safe_lowcut / nyq, safe_highcut / nyq], btype='band')
    return filtfilt(b, a, data)

def takens_embedding(data, delay, dimension=3):
    """Embeds 1D signal into higher-dimensional state space (The Geometric Orbit)."""
    embedded = np.zeros((len(data) - (dimension - 1) * delay, dimension))
    for i in range(dimension):
        embedded[:, i] = data[i * delay : len(data) - (dimension - 1 - i) * delay]
    return embedded

def sliding_window_dimensionality(embedded_data, window_size=100):
    """Calculates SVD Entropy (The Topological Shadow of the CA1-MEC Gate)."""
    entropies = []
    for i in range(len(embedded_data) - window_size):
        window = embedded_data[i : i + window_size]
        window = window - np.mean(window, axis=0) # Mean center
        _, S, _ = np.linalg.svd(window)           # Extract principal axes
        p = (S**2) / np.sum(S**2)                 # Normalize to probability
        entropy = -np.sum(p * np.log(p + 1e-10))  # Shannon entropy
        entropies.append(entropy)
        
    pad_front = window_size // 2
    pad_back = len(embedded_data) - len(entropies) - pad_front
    return np.pad(entropies, (pad_front, pad_back), mode='edge')

def detect_topological_lock_in(entropy, times, val_threshold_low=0.88, val_threshold_high=1.05, flatline_variance=1e-6, window=20):
    """
    Dual-Boundary Scanner for Geometric Dysrhythmia.
    Looks for variance dropping to zero at either the mathematical floor (Collapse) or ceiling (Saturation).
    """
    for i in range(len(entropy) - window):
        segment = entropy[i : i+window]
        variance = np.var(segment)
        mean_val = np.mean(segment)
        
        if variance < flatline_variance:
            if mean_val < val_threshold_low:
                return times[i], "collapse"
            elif mean_val > val_threshold_high:
                return times[i], "saturation"
    return None, None

# --- THE DESKTOP GUI ---

class EDFHolographicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical EDF Holographic Tracker (G_S Architecture) v4 - Latency Mapping")
        self.root.geometry("1400x950")
        
        self.raw_edf = None
        self.fs = None
        self.export_data = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # LEFT PANEL: Controls
        control_frame = tk.Frame(self.root, width=320, padx=20, pady=20, bg="#1e272e")
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(control_frame, text="EDF Holographic Pipeline", fg="white", bg="#1e272e", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Alert Label (Dynamic)
        self.alert_label = tk.Label(control_frame, text="System Standby", fg="#d2dae2", bg="#1e272e", font=("Arial", 11, "bold"))
        self.alert_label.pack(pady=5, fill=tk.X)

        # Data Loading
        self.load_btn = tk.Button(control_frame, text="Load .EDF File", command=self.load_edf, font=("Arial", 12), bg="#0fb9b1", fg="white")
        self.load_btn.pack(fill=tk.X, pady=10)
        
        self.status_label = tk.Label(control_frame, text="Status: Awaiting EDF...", fg="#d2dae2", bg="#1e272e", font=("Arial", 10, "italic"), wraplength=280)
        self.status_label.pack(pady=5)
        
        tk.Frame(control_frame, height=2, bg="#808e9b").pack(fill=tk.X, pady=15)
        
        # Channel Selection
        tk.Label(control_frame, text="1. Select Target Channel", fg="white", bg="#1e272e", font=("Arial", 12, "bold")).pack(anchor="w")
        self.channel_combo = ttk.Combobox(control_frame, state="disabled")
        self.channel_combo.pack(fill=tk.X, pady=5)
        
        tk.Frame(control_frame, height=2, bg="#808e9b").pack(fill=tk.X, pady=15)
        
        # Time Window Selection
        tk.Label(control_frame, text="2. Analysis Window", fg="white", bg="#1e272e", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(control_frame, text="Start Time (seconds):", fg="white", bg="#1e272e").pack(anchor="w")
        self.start_var = tk.StringVar(value="0")
        tk.Entry(control_frame, textvariable=self.start_var).pack(fill=tk.X, pady=5)
        
        tk.Label(control_frame, text="Duration (seconds):", fg="white", bg="#1e272e").pack(anchor="w")
        self.dur_var = tk.StringVar(value="10")
        tk.Entry(control_frame, textvariable=self.dur_var).pack(fill=tk.X, pady=5)
        
        tk.Frame(control_frame, height=2, bg="#808e9b").pack(fill=tk.X, pady=15)

        # Mathematical Parameters
        tk.Label(control_frame, text="3. Operator Tuning", fg="white", bg="#1e272e", font=("Arial", 12, "bold")).pack(anchor="w")
        
        tk.Label(control_frame, text="Takens Delay (tau samples):", fg="white", bg="#1e272e").pack(anchor="w")
        self.tau_var = tk.StringVar(value="4")
        tk.Entry(control_frame, textvariable=self.tau_var).pack(fill=tk.X, pady=5)
        
        tk.Label(control_frame, text="SVD Window Size (samples):", fg="white", bg="#1e272e").pack(anchor="w")
        self.win_var = tk.StringVar(value="100")
        tk.Entry(control_frame, textvariable=self.win_var).pack(fill=tk.X, pady=5)
        
        tk.Frame(control_frame, height=2, bg="#808e9b").pack(fill=tk.X, pady=15)
        
        # Process & Export Buttons
        self.process_btn = tk.Button(control_frame, text="Extract Topological Shadow", command=self.process_data, font=("Arial", 12, "bold"), bg="#eb3b5a", fg="white", state=tk.DISABLED)
        self.process_btn.pack(fill=tk.X, pady=5)

        self.export_btn = tk.Button(control_frame, text="Export Trace to JSON", command=self.export_json, font=("Arial", 12, "bold"), bg="#3867d6", fg="white", state=tk.DISABLED)
        self.export_btn.pack(fill=tk.X, pady=5)

        tk.Frame(control_frame, height=2, bg="#808e9b").pack(fill=tk.X, pady=15)

        # Batch Processing
        tk.Label(control_frame, text="4. Population Causal Mapping", fg="white", bg="#1e272e", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(control_frame, text="(Generates Latency Propagation Report)", fg="#808e9b", bg="#1e272e", font=("Arial", 9)).pack(anchor="w", pady=(0, 5))
        
        self.batch_btn = tk.Button(control_frame, text="Bulk Process Folder", command=self.bulk_process_folder, font=("Arial", 12, "bold"), bg="#8e44ad", fg="white")
        self.batch_btn.pack(fill=tk.X, pady=5)

        # RIGHT PANEL: Plotting Area
        self.plot_frame = tk.Frame(self.root, bg="#f1f2f6")
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        plt.style.use('dark_background')
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(10, 8), dpi=100)
        self.fig.tight_layout(pad=4.0)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def load_edf(self):
        filepath = filedialog.askopenfilename(title="Select Clinical EDF", filetypes=[("EDF Files", "*.edf")])
        if not filepath: return
        
        try:
            self.raw_edf = mne.io.read_raw_edf(filepath, preload=True)
            self.fs = int(self.raw_edf.info['sfreq'])
            channels = self.raw_edf.ch_names
            
            self.channel_combo.config(state="readonly", values=channels)
            if len(channels) > 0: self.channel_combo.current(0)
                
            self.status_label.config(text=f"Loaded. fs = {self.fs}Hz | Channels = {len(channels)}")
            self.process_btn.config(state=tk.NORMAL)
            self.alert_label.config(text="System Standby", fg="#d2dae2")
            
        except Exception as e:
            messagebox.showerror("EDF Loading Error", f"Could not read EDF:\n{str(e)}")

    def process_data(self):
        if self.raw_edf is None: return
        
        try:
            channel_name = self.channel_combo.get()
            start_sec = float(self.start_var.get())
            dur_sec = float(self.dur_var.get())
            
            start_idx = int(start_sec * self.fs)
            end_idx = int((start_sec + dur_sec) * self.fs)
            
            data_slice, times = self.raw_edf.copy().pick_channels([channel_name]).get_data(start=start_idx, stop=end_idx, return_times=True)
            raw_signal = data_slice[0] * 1e6 
            
            clean_signal = butter_bandpass(raw_signal, 1, 100, self.fs)
            theta_band = butter_bandpass(clean_signal, 4, 8, self.fs)
            gamma_band = butter_bandpass(clean_signal, 60, 90, self.fs)
            gamma_env = np.abs(hilbert(gamma_band))
            
            tau = int(self.tau_var.get())
            window = int(self.win_var.get())
            
            embedded_eeg = takens_embedding(clean_signal, delay=tau, dimension=3)
            t_embedded = times[:len(embedded_eeg)]
            local_dim = sliding_window_dimensionality(embedded_eeg, window_size=window)

            # --- THE CLINICAL TRIGGER ---
            lock_in_time, lock_in_type = detect_topological_lock_in(local_dim, t_embedded)

            self.export_data = {
                "metadata": {"channel": channel_name, "fs_hz": self.fs, "start_sec": start_sec, "duration_sec": dur_sec},
                "times": times.tolist(),
                "clean_signal_uv": clean_signal.tolist(),
                "theta_band_4_8_hz": theta_band.tolist(),
                "gamma_env_60_90_hz": gamma_env.tolist(),
                "t_embedded": t_embedded.tolist(),
                "svd_entropy": local_dim.tolist(),
                "dysrhythmia_onset_sec": float(lock_in_time) if lock_in_time else None,
                "dysrhythmia_type": lock_in_type
            }
            self.export_btn.config(state=tk.NORMAL) 
            
            # --- PLOTTING ---
            self.ax1.clear(); self.ax2.clear(); self.ax3.clear()
            
            self.ax1.plot(times, clean_signal, color='cyan', linewidth=0.8)
            self.ax1.set_title(f"Cleaned EEG ({channel_name})")
            
            self.ax2.plot(times, theta_band, color='#a29bfe', label='Theta Phase (4-8 Hz)', alpha=0.8)
            self.ax2.plot(times, gamma_env, color='#fdcb6e', label='Gamma Zoom (60-90 Hz)', linewidth=1.5)
            self.ax2.set_title("Carrier Extraction: Phase-Amplitude Coupling")
            self.ax2.legend(loc="upper right")
            
            self.ax3.plot(t_embedded, local_dim, color='#ff7675', linewidth=2)
            self.ax3.set_title("Topological Shadow: Instantaneous Orbit Dimensionality")
            self.ax3.set_ylabel("SVD Entropy")
            
            # Draw the trigger lines if dysrhythmia is detected
            if lock_in_type == "collapse":
                color_code = '#ff4757'
                alert_text = f"⚠ DIMENSIONAL COLLAPSE AT {lock_in_time:.3f}s"
            elif lock_in_type == "saturation":
                color_code = '#ffa502'
                alert_text = f"⚠ SATURATION/DECOUPLING AT {lock_in_time:.3f}s"
            else:
                color_code = None
                
            if lock_in_time is not None:
                self.ax3.axvline(x=lock_in_time, color=color_code, linestyle='--', linewidth=2.5, label='Lock-in Onset')
                self.ax3.legend(loc="upper right")
                self.ax2.axvline(x=lock_in_time, color=color_code, linestyle='--', linewidth=1.5, alpha=0.7)
                self.ax1.axvline(x=lock_in_time, color=color_code, linestyle='--', linewidth=1.5, alpha=0.7)
                
                self.alert_label.config(text=alert_text, fg=color_code)
            else:
                self.alert_label.config(text="✓ Baseline Topology Normal", fg="#2ed573")

            self.fig.tight_layout(pad=4.0)
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("Processing Error", f"Math or Data Error:\n{str(e)}")

    def export_json(self):
        if self.export_data is None: return
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if not filepath: return
        try:
            with open(filepath, 'w') as f: json.dump(self.export_data, f, indent=2)
            messagebox.showinfo("Export", f"Data saved to:\n{filepath}")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))

    def bulk_process_folder(self):
        """Scans an entire directory of EDF files and computes channel-by-channel SVD pathology + Propagation Latency"""
        folder_path = filedialog.askdirectory(title="Select Folder with EDF Files")
        if not folder_path: return

        edf_files = glob.glob(os.path.join(folder_path, "*.edf"))
        if not edf_files:
            messagebox.showwarning("No Files", "No .edf files found in the selected directory.")
            return

        self.alert_label.config(text="BATCH SCAN & CAUSAL MAPPING RUNNING...", fg="#8e44ad")
        self.status_label.config(text=f"Batch processing {len(edf_files)} files. Please wait...")
        self.root.update()

        start_sec = float(self.start_var.get())
        dur_sec = float(self.dur_var.get())
        tau = int(self.tau_var.get())
        window = int(self.win_var.get())

        report = {
            "metadata": {
                "total_files": len(edf_files),
                "analysis_window_start": start_sec,
                "analysis_window_duration": dur_sec,
                "takens_tau": tau,
                "svd_window": window
            },
            "population_summary": {
                "total_channel_collapses": 0,
                "total_channel_saturations": 0,
                "files_with_dysrhythmia": 0,
                "healthy_files": 0,
                "average_temporal_to_frontal_latency_sec": None
            },
            "channel_vulnerability_map": {},
            "file_details": {}
        }
        
        population_latencies = []

        for file_path in edf_files:
            filename = os.path.basename(file_path)
            self.status_label.config(text=f"Scanning: {filename}...")
            self.root.update()
            
            try:
                raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
                fs = int(raw.info['sfreq'])
                channels = raw.ch_names
                
                start_idx = int(start_sec * fs)
                end_idx = int((start_sec + dur_sec) * fs)
                
                file_report = {"channels": {}}
                file_has_pathology = False
                
                for ch in channels:
                    try:
                        # Extract and filter data
                        data_slice, times = raw.copy().pick_channels([ch]).get_data(start=start_idx, stop=end_idx, return_times=True)
                        raw_signal = data_slice[0] * 1e6 
                        clean_signal = butter_bandpass(raw_signal, 1, 100, fs)
                        
                        # Calculate Topology
                        embedded = takens_embedding(clean_signal, delay=tau, dimension=3)
                        local_dim = sliding_window_dimensionality(embedded, window_size=window)
                        
                        # Run Dual-Boundary Scanner
                        lock_in_time, lock_in_type = detect_topological_lock_in(local_dim, times[:len(embedded)])
                        
                        mean_svd = float(np.mean(local_dim))
                        var_svd = float(np.var(local_dim))
                        
                        ch_report = {
                            "baseline_stability_mean": mean_svd,
                            "variance": var_svd,
                            "dysrhythmia_type": lock_in_type,
                            "onset_sec": float(lock_in_time) if lock_in_time else None
                        }
                        file_report["channels"][ch] = ch_report
                        
                        # Populate Global Tally & Channel Map
                        if ch not in report["channel_vulnerability_map"]:
                            report["channel_vulnerability_map"][ch] = {"collapses": 0, "saturations": 0}
                            
                        if lock_in_type == "collapse":
                            report["population_summary"]["total_channel_collapses"] += 1
                            report["channel_vulnerability_map"][ch]["collapses"] += 1
                            file_has_pathology = True
                        elif lock_in_type == "saturation":
                            report["population_summary"]["total_channel_saturations"] += 1
                            report["channel_vulnerability_map"][ch]["saturations"] += 1
                            file_has_pathology = True
                            
                    except Exception as ch_err:
                        file_report["channels"][ch] = {"error": str(ch_err)}

                # --- PROPAGATION REPORT LOGIC (THE FREEZING WAVE) ---
                temporal_channels = ['T3', 'T4', 'T5', 'T6']
                frontal_channels = ['Fp1', 'Fp2', 'Fz', 'F3', 'F4']
                
                temp_onsets = [file_report["channels"][ch]["onset_sec"] for ch in temporal_channels 
                               if ch in file_report["channels"] and file_report["channels"][ch].get("onset_sec") is not None]
                front_onsets = [file_report["channels"][ch]["onset_sec"] for ch in frontal_channels 
                                if ch in file_report["channels"] and file_report["channels"][ch].get("onset_sec") is not None]
                
                if len(temp_onsets) > 0 and len(front_onsets) > 0:
                    t_mean = float(np.mean(temp_onsets))
                    f_mean = float(np.mean(front_onsets))
                    latency = f_mean - t_mean
                    
                    file_report["propagation_analysis"] = {
                        "temporal_mean_onset_sec": t_mean,
                        "frontal_mean_onset_sec": f_mean,
                        "latency_front_minus_temp_sec": latency,
                        "causal_direction": "Temporal -> Frontal" if latency > 0 else "Frontal -> Temporal"
                    }
                    population_latencies.append(latency)
                else:
                    file_report["propagation_analysis"] = "Insufficient lock-ins to calculate latency cascade."
                
                report["file_details"][filename] = file_report
                
                if file_has_pathology:
                    report["population_summary"]["files_with_dysrhythmia"] += 1
                else:
                    report["population_summary"]["healthy_files"] += 1

            except Exception as file_err:
                report["file_details"][filename] = {"error": str(file_err)}

        # Aggregate the final latency statistic
        if population_latencies:
            report["population_summary"]["average_temporal_to_frontal_latency_sec"] = float(np.mean(population_latencies))

        # Finish up
        self.alert_label.config(text="✓ BATCH & LATENCY SCAN COMPLETE", fg="#2ed573")
        self.status_label.config(text="Status: Generating Population Report...")
        
        save_path = filedialog.asksaveasfilename(
            title="Save Population Dysrhythmia Report",
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")], 
            initialfile="Causal_Propagation_Report.json"
        )
        
        if save_path:
            try:
                with open(save_path, 'w') as f:
                    json.dump(report, f, indent=2)
                messagebox.showinfo("Batch Complete", f"Scanned {len(edf_files)} files.\nReport saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to save JSON:\n{str(e)}")
                
        self.status_label.config(text="Status: Ready.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EDFHolographicApp(root)
    root.mainloop()