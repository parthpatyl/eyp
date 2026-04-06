"""
aerodynamics.py — Reduced-Order Aerodynamic Model

Computes lift and drag using analytical and empirical relations.
Supports multiple CL/CD models: constant, linear with stall, and lookup tables.

Lift: L = 0.5 * ρ * V² * S * CL
Drag: D = 0.5 * ρ * V² * S * CD

Optional surrogate model integration for ML-based coefficients.
"""

import numpy as np
from dataclasses import dataclass
from typing import Union, Optional, Callable, List, Tuple
from scipy.interpolate import interp1d


@dataclass
class AerodynamicCoefficients:
    """Container for aerodynamic coefficients."""
    CL: float
    CD: float
    CL_max: Optional[float] = None
    alpha_deg: Optional[float] = None


@dataclass
class AircraftGeometry:
    """Aircraft geometric parameters."""
    wing_area_m2: float
    wing_span_m: Optional[float] = None
    mass_kg: Optional[float] = None
    aspect_ratio: Optional[float] = None

    def __post_init__(self):
        if self.wing_span_m and self.wing_area_m2:
            self.aspect_ratio = self.wing_span_m ** 2 / self.wing_area_m2


def compute_lift(
    density: float,
    velocity_ms: float,
    wing_area: float,
    CL: float
) -> float:
    """
    Compute lift force.

    L = 0.5 * ρ * V² * S * CL

    Parameters:
        density: Air density (kg/m³)
        velocity_ms: True air speed (m/s)
        wing_area: Wing area (m²)
        CL: Lift coefficient

    Returns:
        Lift force in Newtons
    """
    return 0.5 * density * velocity_ms ** 2 * wing_area * CL


def compute_drag(
    density: float,
    velocity_ms: float,
    wing_area: float,
    CD: float
) -> float:
    """
    Compute drag force.

    D = 0.5 * ρ * V² * S * CD

    Parameters:
        density: Air density (kg/m³)
        velocity_ms: True air speed (m/s)
        wing_area: Wing area (m²)
        CD: Drag coefficient

    Returns:
        Drag force in Newtons
    """
    return 0.5 * density * velocity_ms ** 2 * wing_area * CD


def compute_lift_coefficient_linear(
    aoa_deg: float,
    CL0: float = 0.0,
    CL_alpha: float = 2 * np.pi,  # Thin airfoil theory
    alpha_stall: float = 15.0,
    CL_max: float = 1.5
) -> AerodynamicCoefficients:
    """
    Compute CL using linear model with stall.

    CL = CL0 + CL_alpha * α (linear region)
    CL = CL_max (post-stall, clamped)

    Parameters:
        aoa_deg: Angle of attack in degrees
        CL0: Zero-lift coefficient (aircraft offset)
        CL_alpha: Lift curve slope (per radian)
        alpha_stall: Stall angle of attack (degrees)
        CL_max: Maximum lift coefficient

    Returns:
        AerodynamicCoefficients with CL, CD
    """
    alpha_rad = np.radians(aoa_deg)
    alpha_stall_rad = np.radians(alpha_stall)

    if abs(aoa_deg) <= alpha_stall:
        # Linear region
        CL = CL0 + CL_alpha * alpha_rad
    else:
        # Post-stall (simplified: CL drops off)
        stall_factor = max(0.2, 1.0 - 0.05 * (abs(aoa_deg) - alpha_stall))
        CL = np.sign(aoa_deg) * CL_max * stall_factor

    # Clamp CL
    CL = np.clip(CL, -CL_max, CL_max)

    return AerodynamicCoefficients(CL=CL, CD=0.0, CL_max=CL_max, alpha_deg=aoa_deg)


def compute_cd_polar(
    CL: float,
    CD0: float = 0.02,
    K: float = 0.04,
    CD_max: float = 0.5
) -> float:
    """
    Compute drag coefficient using drag polar.

    CD = CD0 + K * CL² (parabolic drag polar)

    Parameters:
        CL: Lift coefficient
        CD0: Zero-lift drag coefficient
        K: Induced drag factor (1/(π*e*AR))
        CD_max: Maximum drag coefficient (clamping)

    Returns:
        Drag coefficient
    """
    CD = CD0 + K * CL ** 2
    return min(CD, CD_max)


def compute_lift_drag_at_aoa(
    aoa_deg: float,
    density: float,
    velocity_ms: float,
    wing_area: float,
    CL0: float = 0.0,
    CL_alpha: float = 5.0,  # ~2π per radian adjusted for finite wing
    alpha_stall: float = 15.0,
    CL_max: float = 1.5,
    CD0: float = 0.02,
    K: float = 0.04
) -> Tuple[float, float]:
    """
    Compute lift and drag at given angle of attack.

    Parameters:
        aoa_deg: Angle of attack (degrees)
        density: Air density (kg/m³)
        velocity_ms: True air speed (m/s)
        wing_area: Wing area (m²)
        CL0: Zero-lift coefficient
        CL_alpha: Lift curve slope (per radian)
        alpha_stall: Stall angle (degrees)
        CL_max: Maximum CL
        CD0: Zero-lift drag
        K: Induced drag factor

    Returns:
        (Lift, Drag) in Newtons
    """
    # Compute CL
    aero = compute_lift_coefficient_linear(
        aoa_deg, CL0, CL_alpha, alpha_stall, CL_max
    )
    CL = aero.CL

    # Compute CD
    CD = compute_cd_polar(CL, CD0, K)

    # Compute forces
    L = compute_lift(density, velocity_ms, wing_area, CL)
    D = compute_drag(density, velocity_ms, wing_area, CD)

    return L, D


def compute_cruise_cl(
    mass_kg: float,
    density: float,
    velocity_ms: float,
    wing_area: float
) -> float:
    """
    Compute required CL for steady cruise (L = W).

    CL_required = 2 * m * g / (ρ * V² * S)

    Parameters:
        mass_kg: Aircraft mass (kg)
        density: Air density (kg/m³)
        velocity_ms: Cruise speed (m/s)
        wing_area: Wing area (m²)

    Returns:
        Required lift coefficient
    """
    g = 9.80665
    weight = mass_kg * g
    return 2 * weight / (density * velocity_ms ** 2 * wing_area)


def compute_cruise_cd(
    CL: float,
    CD0: float = 0.02,
    K: float = 0.04
) -> float:
    """
    Compute CD at cruise condition.

    Parameters:
        CL: Cruise lift coefficient
        CD0: Zero-lift drag
        K: Induced drag factor

    Returns:
        Drag coefficient
    """
    return compute_cd_polar(CL, CD0, K)


def compute_power_required(
    mass_kg: float,
    density: float,
    velocity_ms: float,
    wing_area: float,
    CD0: float = 0.02,
    K: float = 0.04,
    propeller_efficiency: float = 0.75
) -> float:
    """
    Compute power required for steady cruise.

    P_required = D * V / η_prop

    Parameters:
        mass_kg: Aircraft mass (kg)
        density: Air density (kg/m³)
        velocity_ms: Cruise speed (m/s)
        wing_area: Wing area (m²)
        CD0: Zero-lift drag
        K: Induced drag factor
        propeller_efficiency: Propeller efficiency

    Returns:
        Power required in Watts
    """
    # Required CL
    CL = compute_cruise_cl(mass_kg, density, velocity_ms, wing_area)

    # CD at this CL
    CD = compute_cruise_cd(CL, CD0, K)

    # Drag
    D = compute_drag(density, velocity_ms, wing_area, CD)

    # Power (with propeller efficiency)
    if propeller_efficiency > 0:
        P = D * velocity_ms / propeller_efficiency
    else:
        P = D * velocity_ms

    return P


# =============================================================================
# Surrogate Model Integration Point
# =============================================================================

class AerodynamicSurrogate:
    """
    Surrogate model for aerodynamic coefficients.

    Can use precomputed data (XFOIL, CFD, or literature)
    and fit with polynomial regression or ML.
    """

    def __init__(
        self,
        aoa_range: np.ndarray,
        CL_data: np.ndarray,
        CD_data: np.ndarray
    ):
        """
        Initialize with lookup table data.

        Parameters:
            aoa_range: Array of AoA values (degrees)
            CL_data: Corresponding CL values
            CD_data: Corresponding CD values
        """
        self.aoa_range = aoa_range
        self.CL_interp = interp1d(aoa_range, CL_data, kind='linear', fill_value='extrapolate')
        self.CD_interp = interp1d(aoa_range, CD_data, kind='linear', fill_value='extrapolate')

    def get_coefficients(self, aoa_deg: float) -> AerodynamicCoefficients:
        """Get CL, CD at given AoA."""
        CL = float(self.CL_interp(aoa_deg))
        CD = float(self.CD_interp(aoa_deg))
        return AerodynamicCoefficients(CL=CL, CD=CD, alpha_deg=aoa_deg)


# =============================================================================
# Example: Fit surrogate from theoretical model
# =============================================================================

def create_theoretical_surrogate(
    CL0: float = 0.0,
    CL_alpha: float = 5.0,
    alpha_stall: float = 15.0,
    CL_max: float = 1.5,
    CD0: float = 0.02,
    K: float = 0.04,
    aoa_range: Optional[np.ndarray] = None
) -> AerodynamicSurrogate:
    """
    Create surrogate from theoretical model.

    Parameters:
        CL0: Zero-lift coefficient
        CL_alpha: Lift curve slope
        alpha_stall: Stall angle
        CL_max: Max CL
        CD0: Zero-lift drag
        K: Induced drag factor
        aoa_range: AoA range for interpolation

    Returns:
        AerodynamicSurrogate object
    """
    if aoa_range is None:
        aoa_range = np.linspace(-20, 25, 91)

    CL_data = np.zeros_like(aoa_range)
    CD_data = np.zeros_like(aoa_range)

    for i, aoa in enumerate(aoa_range):
        aero = compute_lift_coefficient_linear(
            aoa, CL0, CL_alpha, alpha_stall, CL_max
        )
        CL_data[i] = aero.CL
        CD_data[i] = compute_cd_polar(aero.CL, CD0, K)

    return AerodynamicSurrogate(aoa_range, CL_data, CD_data)


# Test function
if __name__ == "__main__":
    print("=== Aerodynamic Model Test ===\n")

    # Test parameters
    mass = 25.0  # kg
    wing_area = 10.0  # m²
    velocity = 25.0  # m/s
    altitude = 20000  # m

    # Get density from atmosphere module
    from atmosphere import isa_properties
    props = isa_properties(altitude)
    rho = props.density_kgm3

    print(f"Aircraft: {mass} kg, S = {wing_area} m²")
    print(f"Altitude: {altitude} m, ρ = {rho:.4f} kg/m³")
    print(f"Cruise speed: {velocity} m/s\n")

    # Compute cruise CL
    CL_cruise = compute_cruise_cl(mass, rho, velocity, wing_area)
    CD_cruise = compute_cruise_cd(CL_cruise, CD0=0.02, K=0.04)
    L = compute_lift(rho, velocity, wing_area, CL_cruise)
    D = compute_drag(rho, velocity, wing_area, CD_cruise)

    print(f"Required CL for cruise: {CL_cruise:.3f}")
    print(f"Drag coefficient: {CD_cruise:.4f}")
    print(f"Lift: {L:.1f} N (weight: {mass * 9.81:.1f} N)")
    print(f"Drag: {D:.1f} N")

    # Power required
    P_req = compute_power_required(mass, rho, velocity, wing_area)
    print(f"\nPower required: {P_req:.1f} W")
    print(f"Power required per kg: {P_req / mass:.1f} W/kg")