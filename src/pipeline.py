import numpy as np
from typing import Tuple, Dict, List

# Calibration lines from docs/PHYSICS_SPEC.md
CALIBRATION_LINES = {
    "O_I_557.7": 557.7,
    "O_I_777.4": 777.4,
    "Na_I_589.3": 589.3,
    "Mg_I_518.0": 518.0,
    "Fe_I_532.8": 532.8,
    "Al_I_395.3": 395.3,
    "Cu_I_510.5": 510.5,
    "Cu_I_521.8": 521.8,
    "Li_I_670.8": 670.8,
}

def detect_and_rectify_track(image: np.ndarray) -> Tuple[np.ndarray, float]:
    """Detect and rectify the meteor/reentry track in the image.
    
    Args:
        image: Input image as numpy array (px)
        
    Returns:
        Tuple of (rectified_image, track_angle_deg) where:
        - rectified_image: Image with track aligned vertically (px)
        - track_angle_deg: Angle of the track relative to vertical (deg)
    """
    # Placeholder implementation returning unchanged image and 0° angle
    return (image, 0.0)

def extract_spectrum(rectified: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Extract 1D spectrum from rectified image.
    
    Args:
        rectified: Rectified image with track aligned vertically (px)
        
    Returns:
        Tuple of (wavelength_nm, intensity_au) where:
        - wavelength_nm: Wavelength scale in nanometers (nm)
        - intensity_au: Intensity profile in arbitrary units (au)
    """
    # Placeholder implementation returning flat profile
    wavelength_nm = np.linspace(380.0, 900.0, 512)
    intensity_au = np.ones(512)
    return (wavelength_nm, intensity_au)

def compute_peak_ratios(wavelength_nm: np.ndarray, intensity_au: np.ndarray, line_dict: dict) -> Dict[str, float]:
    """Compute peak intensity ratios for metal lines.
    
    Args:
        wavelength_nm: Wavelength scale in nanometers (nm)
        intensity_au: Intensity profile in arbitrary units (au)
        line_dict: Dictionary of line names to wavelengths (nm)
        
    Returns:
        Dictionary of peak intensity ratios:
        - al_to_mg: Al I / Mg I ratio
        - li_to_na: Li I / Na I ratio
        - cu_to_fe: Cu I / Fe I ratio
    """
    # Placeholder implementation returning zeros
    return {"al_to_mg": 0.0, "li_to_na": 0.0, "cu_to_fe": 0.0}