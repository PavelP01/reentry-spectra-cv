# Reentry & Meteor Spectral Classifier

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Problem

Space debris reentry events and natural meteor showers produce distinctive spectral signatures that can be used to distinguish between anthropogenic and natural sources. The presence of metallic elements like aluminum (Al), lithium (Li), and copper (Cu) in reentry debris leads to characteristic emission lines that differ from those produced by natural meteor ablation. Understanding these spectral differences is crucial for monitoring space debris and assessing potential atmospheric impacts from metallic oxide formation (e.g., Al₂O₃, LiO, CuO), which can contribute to ozone depletion.

This project implements a deterministic computer vision and physics-based pipeline to classify space debris reentry events from natural meteor showers using spectral line ratios.

## Pipeline

```
┌──────────┐   ┌──────────────┐   ┌───────────┐   ┌────────────┐   ┌──────────────┐
│ Raw      │   │ Track        │   │ Spectrum  │   │ Peak       │   │ Interpretable│
│ Frame    │ → │ Detection &  │ → │ Extraction│ → │ Ratios     │ → │ Classifier   │
│ (FITS/png)│   │ Rectification│   │ (1D profile)│   │ (Al/Mg, etc)│   │ (Iteration 2)│
└──────────┘   └──────────────┘   └───────────┘   └────────────┘   └──────────────┘
```

## Spectral Lines Reference

| Label | λ (nm) | Origin |
|-------|--------|--------|
| Al I  | 395.3  | Space debris |
| Li I  | 670.8  | Space debris |
| Cu I  | 510.5 / 521.8 | Space debris |
| Mg I  | 518.0  | Natural meteor |
| Fe I  | 532.8  | Natural meteor |
| Na I  | 589.3  | Natural meteor |
| O I   | 557.7 / 777.4 | Atmosphere (calib) |

## Quick Start

```bash
git clone ...
cd reentry-spectra-cv
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v
```

## Current Status

Iteration 1 — Image Ingestion, Track Alignment & Metal Line Extraction (deterministic CV pipeline)

## References

- docs/PHYSICS_SPEC.md
- docs/DATA_COLLECTION_PROTOCOL.md

## License

MIT