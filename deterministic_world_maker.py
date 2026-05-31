"""
DETERMINISTIC WORLD MAKER v2 (The True Koopman Interference)
------------------------------------------------------------
Uses Masked Inverse-FFT to instantaneously sum thousands 
of Moiré lattices without floating-point degradation.

Starts at 1 field (base wave) and scales up to 5,000 fields.
"""

import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                             QHBoxLayout, QWidget, QPushButton, QSlider, QFileDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap

class MoireWorldMakerV2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deterministic World Maker v2 (Holographic Interference)")
        self.setGeometry(100, 100, 1100, 500)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")

        # Internal State
        self.img_size = 256
        self.F_shift = None
        self.magnitude = None
        self.sorted_magnitudes = None
        
        # --- THE REQUESTED LIMITS ---
        self.max_lattices = 5000  # Cap the slider at 5000 fields
        self.current_lattices = 1   # Start exactly at 1 field

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # --- Controls ---
        control_layout = QHBoxLayout()
        
        self.btn_load = QPushButton("Load Target World (Image)")
        self.btn_load.setStyleSheet("background-color: #b8956a; color: black; padding: 10px; font-weight: bold;")
        self.btn_load.clicked.connect(self.load_image)
        control_layout.addWidget(self.btn_load)

        self.lbl_slider = QLabel(f"Active Lattices (Koopman Modes): {self.current_lattices} / {self.max_lattices}")
        self.lbl_slider.setStyleSheet("font-size: 16px; font-weight: bold;")
        control_layout.addWidget(self.lbl_slider)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(self.max_lattices)
        self.slider.setValue(self.current_lattices)
        self.slider.valueChanged.connect(self.on_slider_change)
        control_layout.addWidget(self.slider)

        layout.addLayout(control_layout)

        # --- Visualizers ---
        vis_layout = QHBoxLayout()

        # 1. Original
        vbox1 = QVBoxLayout()
        vbox1.addWidget(QLabel("1. Target World"))
        self.lbl_original = QLabel()
        self.lbl_original.setFixedSize(self.img_size, self.img_size)
        self.lbl_original.setStyleSheet("border: 1px solid #444;")
        vbox1.addWidget(self.lbl_original)
        vis_layout.addLayout(vbox1)

        # 2. FFT Spectrum (The DNA Mask)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(QLabel("2. Active Genomic Space (Holographic Plate)"))
        self.lbl_fft = QLabel()
        self.lbl_fft.setFixedSize(self.img_size, self.img_size)
        self.lbl_fft.setStyleSheet("border: 1px solid #444;")
        vbox2.addWidget(self.lbl_fft)
        vis_layout.addLayout(vbox2)

        # 3. Reconstruction
        vbox3 = QVBoxLayout()
        vbox3.addWidget(QLabel("3. Moiré Interference Pattern"))
        self.lbl_recon = QLabel()
        self.lbl_recon.setFixedSize(self.img_size, self.img_size)
        self.lbl_recon.setStyleSheet("border: 1px solid #444;")
        vbox3.addWidget(self.lbl_recon)
        vis_layout.addLayout(vbox3)

        layout.addLayout(vis_layout)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (self.img_size, self.img_size))
                self.process_target(img)

    def process_target(self, img):
        self.lbl_original.setPixmap(QPixmap.fromImage(self.np_to_qimage(img)))

        # 1. Perform 2D FFT (Extract the DNA)
        F = np.fft.fft2(img)
        self.F_shift = np.fft.fftshift(F)
        self.magnitude = np.abs(self.F_shift)

        # 2. Sort every single wave by its amplitude
        # This tells us which Moiré lattices are the most important
        self.sorted_magnitudes = np.sort(self.magnitude.ravel())[::-1]

        # Reset slider for new image to 1
        self.slider.setValue(1)
        self.update_reconstruction()

    def on_slider_change(self, value):
        self.current_lattices = value
        self.lbl_slider.setText(f"Active Lattices (Koopman Modes): {self.current_lattices} / {self.max_lattices}")
        self.update_reconstruction()

    def update_reconstruction(self):
        if self.F_shift is None: return

        # 1. Find the amplitude threshold for the Top N lattices
        # Ensure we don't go out of bounds if the image is smaller than expected
        safe_index = min(self.current_lattices, len(self.sorted_magnitudes)) - 1
        threshold = self.sorted_magnitudes[safe_index]

        # 2. Create the Mask (Silence all frequencies below the threshold)
        mask = self.magnitude >= threshold
        F_filtered = self.F_shift * mask

        # --- Render the active Genome Space (Middle Panel) ---
        disp_mag = np.log1p(np.abs(F_filtered))
        max_mag = np.max(disp_mag)
        if max_mag > 0:
            disp_mag = (disp_mag / max_mag * 255).astype(np.uint8)
        else:
            disp_mag = np.zeros_like(disp_mag, dtype=np.uint8)
            
        # Color the active frequencies green so you can see the DNA mask growing
        fft_vis = np.zeros((self.img_size, self.img_size, 3), dtype=np.uint8)
        fft_vis[:, :, 1] = disp_mag 
        self.lbl_fft.setPixmap(QPixmap.fromImage(self.np_to_qimage(fft_vis)))

        # --- Reconstruct the World via iFFT (Right Panel) ---
        # This mathematically sums the active Moiré lattices instantaneously
        img_back = np.abs(np.fft.ifft2(np.fft.ifftshift(F_filtered)))
        
        # Normalize back to image space
        r_min, r_max = img_back.min(), img_back.max()
        if r_max > r_min:
            reconstruction = (img_back - r_min) / (r_max - r_min)
        else:
            reconstruction = np.zeros_like(img_back)
            
        recon_img = (reconstruction * 255).astype(np.uint8)
        self.lbl_recon.setPixmap(QPixmap.fromImage(self.np_to_qimage(recon_img)))

    def np_to_qimage(self, img):
        if img.ndim == 2: # Grayscale
            h, w = img.shape
            return QImage(img.data, w, h, w, QImage.Format.Format_Grayscale8)
        else: # RGB
            h, w, c = img.shape
            return QImage(img.data, w, h, w*c, QImage.Format.Format_RGB888)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MoireWorldMakerV2()
    window.show()
    sys.exit(app.exec())