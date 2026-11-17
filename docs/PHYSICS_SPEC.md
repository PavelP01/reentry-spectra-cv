# Physics & Spectroscopy Specification

## 1. Diffraction Geometry (0th & 1st Orders)
- A transmission diffraction grating mounted before the camera lens produces:
  - **0th Order:** Direct bright trajectory of the burning object (meteor or satellite debris).
  - **1st Order:** Dispersed 2D spectral band running parallel to the 0th-order track.
- **Rectification Rule:** Rotate image by `-theta` (where `theta` is track angle from vertical) so the 0th-order track is vertical and dispersion runs horizontally left-to-right (`lambda` increases with distance `dx` from the 0th-order track).
- **Grating Equation (Small-Angle Linear Approximation):**
  $$\lambda \approx k \cdot \Delta x_{\text{px}}$$
  where $\Delta x_{\text{px}}$ is perpendicular pixel distance from the 0th-order track centerline, and $k$ (`nm/px`) is calibrated using known atmospheric/meteoric anchor lines (`O I 557.7 nm`, `Na I 589.0 nm`).

## 2. Target Atomic Emission Lines (NIST Reference, Air Wavelengths)
### Natural Meteoroid Markers (Chondrites / Iron-Magnesium Silicates)
- **Mg I (Magnesium triplet):** `516.7 nm`, `517.3 nm`, `518.4 nm` (blended peak ~`518.0 nm`)
- **Fe I (Iron multiplet):** `526.9 nm`, `532.8 nm`, `537.1 nm` (characteristic cluster `527–540 nm`)
- **Na I (Sodium D-doublet):** `589.0 nm`, `589.6 nm` (strongest volatile marker ~`589.3 nm`)

### Anthropogenic Space Debris Markers (Satellites / Rocket Stages)
- **Al I (Aluminum resonance doublet):** `394.4 nm`, `396.1 nm` (blended peak ~`395.3 nm`)
- **Cu I (Copper lines — wiring/electronics):** `510.5 nm`, `521.8 nm`
- **Li I (Lithium line — batteries/alloys):** `670.8 nm`

### Atmospheric Reference Lines (Calibration Anchors)
- **O I (Auroral/airglow green line):** `557.7 nm`
- **O I (Atmospheric triplet):** `777.4 nm`

## 3. Baseline & Feature Extraction Rules
- Subtract local sky background (median intensity of parallel strip offset outside the spectrum) before measuring line peaks.
- Compute integrated line fluxes within a `±4 nm` window around target wavelengths and form dimensionless physical ratios (`Al_to_Mg`, `Li_to_Na`, `Cu_to_Fe`) invariant to object brightness and distance.
