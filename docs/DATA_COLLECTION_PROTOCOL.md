# Data Collection Protocol for Reentry & Meteor Spectral Classification

## 1. Sources of Raw Diffraction Images

### 1.1 Global Meteor Network (GMN) — Spectral Cameras
- Archive structure: `FF_*.fits` files + `platepar` calibration files
- How to identify spectral vs regular cameras
- Download procedure (URLs, rsync, wget)
- Expected file naming conventions

### 1.2 Scientific Repositories
- **Zenodo:** search keys `meteor emission spectroscopy diffraction image`, `space debris reentry spectroscopy`
- **NASA All Sky Fireball Network:** data access
- **European Fireball Network:** data access
- Expected metadata: observation time, station ID, calibration parameters

## 2. Reference Line Catalog (NIST Atomic Spectra Database)
- Table of all target lines (Mg I, Fe I, Na I / Al I, Cu I, Li I / O I) with air wavelengths
- Band-pass integration windows (±4 nm around each line center)
- Instructions for updating catalog from NIST ASD

## 3. Sample Requirements by Iteration

### Iteration 1 (Development & Validation)
- 3–5 real files in `data/sample/` OR synthetic frames from `tests/test_physics.py`

### Iteration 2 (ML Training)
- Minimum 30–50 events across multiple stations/nights
- GroupKFold split by station-night to prevent camera calibration leakage
- Labeling protocol: "anthropogenic" vs "natural" based on known reentry events vs meteor shower catalog cross-reference