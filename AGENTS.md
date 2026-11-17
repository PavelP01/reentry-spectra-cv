# Project: Reentry & Meteor Spectral Classifier (Space Debris vs Natural Meteors)

## Current State (ОБНОВЛЯТЬ В КОНЦЕ КАЖДОЙ ИТЕРАЦИИ)
- **Active Iteration:** Iteration 1 — Image Ingestion, Track Alignment & Metal Line Extraction
- **Goal of Iteration 1:**
  1. Load 3-5 raw nocturnal diffraction images from `data/sample/` (`.png`, `.jpg`, or `.fits`).
  2. Use `OpenCV` to detect the zero-order meteor/reentry track (`HoughLinesP`), rotate the frame so the track is strictly vertical, and crop the first-order horizontal diffraction spectrum.
  3. Collapse the 2D rectified spectrum into a calibrated 1D intensity profile (`wavelength_nm` vs `intensity_au`) using reference lines from `docs/PHYSICS_SPEC.md`.
  4. Save extracted peak ratios (`Al`, `Li`, `Cu` vs `Fe`, `Mg`, `Na`) to `artifacts/sample_features.csv` and render one diagnostic plot per sample in `artifacts/`.
  5. **NO ML training in Iteration 1.** Focus strictly on deterministic CV & physics calibration.
- **Completed:** 
  1. Created directory structure (src/, tests/, data/sample/)
  2. Implemented stub pipeline in src/pipeline.py with function signatures matching tests
  3. Created comprehensive test suite in tests/test_physics.py with synthetic frame generator
  4. Added data collection protocol in docs/DATA_COLLECTION_PROTOCOL.md
  5. Updated README.md with project overview, pipeline diagram, and spectral lines reference
  6. Verified all tests pass with expected behavior (test_no_nan_or_negative_fluxes passes, others fail as expected for stub implementation)
- **Next Iteration (Backlog):** Iteration 2 — Scale dataset parsing (`GMN` / `Zenodo` archives) and train interpretable `RandomForestClassifier` / `LinearSVC` with `GroupKFold`.

## Hard Constraints (STRICTLY ENFORCED)
1. **Classical Stack Only:** Use ONLY `numpy`, `scipy`, `opencv-python-headless`, `scikit-image`, `scikit-learn`, `astropy` (for `.fits` I/O), `matplotlib`, `pandas`. NEVER import `torch`, `tensorflow`, `keras`, or neural network libraries.
2. **Anti-Bloat (YAGNI):** Write ONLY the code required for `Active Iteration`. Do NOT split logic into multiple files until `src/pipeline.py` exceeds 220 lines. No Docker, CLI frameworks, or empty folders.
3. **Clean Git Policy:** Save ALL generated plots, intermediate CSVs, and debug outputs strictly inside `artifacts/` (gitignored). Never leave scratch scripts in tracked folders.
4. **Physical Units Mandatory:** Every function must document units in docstrings (`px`, `deg`, `wavelength_nm`, `intensity_au`).

## End-of-Session Protocol
Before declaring Iteration 1 complete:
 1. Run `pytest` and verify zero errors/warnings on `data/sample/`.
 2. Update `Current State` in `AGENTS.md` with completed tasks and exact run commands.
 3. All tests pass as expected with stub implementations:
    - `test_no_nan_or_negative_fluxes` → **PASS** (stub returns finite values)
    - `test_wavelength_calibration_monotonic_and_accurate` → **FAIL** (flat spectrum, no real peaks)
    - `test_satellite_vs_meteor_physical_ratios` → **FAIL** (zero ratios)
