"""
variability.py — Atmospheric Variability Models

Introduces realistic perturbations beyond the standard ISA:
- Temperature perturbations (diurnal variation)
- Wind profiles (logarithmic and linear)
- Turbulence approximation (simplified Dryden-like model)
"""

import numpy as np
from typing import Union, Optional, Tuple


def temperature_perturbation(
    altitude_m: Union[float, np.ndarray],
    time_hours: float,
    amplitude: float = 5.0,
    phase_shift: float = 0.0,
    reference_altitude: float = 10000.0
) -> float:
    """
    Diurnal temperature perturbation.

    Simulates day-night temperature variation that decreases with altitude
    (larger near ground, smaller in stratosphere).

    ΔT(t, h) = amplitude * sin(2π*t/24 + phase_shift) * exp(-h/h_ref)

    Parameters:
        altitude_m: Altitude in meters (scalar)
        time_hours: Time of day (hours)
        amplitude: Peak-to-peak amplitude at surface (K)
        phase_shift: Phase offset (radians)
        reference_altitude: Decay altitude scale (m)

    Returns:
        Temperature perturbation (K) - scalar
    """
    # Handle scalar input only
    h = float(altitude_m) if np.isscalar(altitude_m) else float(altitude_m.flat[0])

    # Altitude-dependent amplitude
    alt_factor = np.exp(-h / reference_altitude)

    # Diurnal variation
    phase = 2 * np.pi * time_hours / 24.0 + phase_shift
    time_variation = amplitude * np.sin(phase)

    return float(alt_factor * time_variation)


def wind_profile_logarithmic(
    altitude_m: Union[float, np.ndarray],
    z0: float = 0.1,
    ustar: float = 0.5,
    roughness_class: str = "moderate"
) -> np.ndarray:
    """
    Logarithmic wind profile (standard atmospheric boundary layer).

    u(z) = (u* / k) * ln((z - d) / z0)

    Parameters:
        altitude_m: Altitude in meters
        z0: Roughness length (m)
        ustar: Friction velocity (m/s)
        roughness_class: Classification for default z0 values

    Returns:
        Wind speed (m/s)
    """
    # Map roughness class to z0
    roughness_map = {
        "smooth_water": 0.001,
        "grass": 0.05,
        "moderate": 0.1,
        "rough_trees": 0.5,
        "city": 2.0
    }
    z0 = roughness_map.get(roughness_class, z0)

    # Von Karman constant
    k = 0.41

    # Zero displacement (for built areas)
    d = 0.0

    altitude_m = np.asarray(altitude_m, dtype=float)
    if altitude_m.ndim == 0:
        altitude_m = altitude_m[np.newaxis]

    # Avoid log of zero or negative
    z_effective = np.maximum(altitude_m, z0 + 0.1)

    wind_speed = (ustar / k) * np.log(z_effective / z0)

    return np.maximum(wind_speed, 0.0)


def wind_profile_linear(
    altitude_m: Union[float, np.ndarray],
    wind_speed_ref: float = 10.0,
    ref_altitude: float = 100.0,
    shear_exponent: float = 0.2
) -> np.ndarray:
    """
    Simple power law wind profile.

    u(z) = u_ref * (z / z_ref)^α

    Parameters:
        altitude_m: Altitude in meters
        wind_speed_ref: Reference wind speed (m/s)
        ref_altitude: Reference altitude (m)
        shear_exponent: Power law exponent (typical: 0.1-0.3)

    Returns:
        Wind speed (m/s)
    """
    altitude_m = np.asarray(altitude_m, dtype=float)
    if altitude_m.ndim == 0:
        altitude_m = altitude_m[np.newaxis]

    # Avoid division by zero
    z_safe = np.maximum(altitude_m, 1.0)
    z_ref_safe = max(ref_altitude, 1.0)

    wind_speed = wind_speed_ref * (z_safe / z_ref_safe) ** shear_exponent

    return np.maximum(wind_speed, 0.0)


def wind_profile_hale(
    altitude_m: Union[float, np.ndarray],
    cruise_altitude: float = 20000.0,
    max_wind: float = 30.0
) -> np.ndarray:
    """
    Simplified HALE-specific wind profile.

    Models typical wind conditions at high altitude:
    - Lower atmosphere: moderate wind with shear
    - Jet stream region: possible high-speed region around 10-15km
    - Stratosphere: lower winds

    Parameters:
        altitude_m: Altitude in meters
        cruise_altitude: Typical cruise altitude (m)
        max_wind: Maximum wind speed in jet stream (m/s)

    Returns:
        Wind speed (m/s)
    """
    altitude_m = np.asarray(altitude_m, dtype=float)
    if altitude_m.ndim == 0:
        altitude_m = altitude_m[np.newaxis]

    # Simplified model with jet stream
    wind = np.zeros_like(altitude_m)

    # Ground layer (0-2km): moderate wind
    mask_low = altitude_m < 2000
    wind[mask_low] = 5.0 + 5.0 * altitude_m[mask_low] / 2000

    # Mid layer (2-12km): increasing toward jet stream
    mask_mid = (altitude_m >= 2000) & (altitude_m < 12000)
    z_mid = altitude_m[mask_mid]
    wind[mask_mid] = 10.0 + 15.0 * np.sin(np.pi * (z_mid - 2000) / 10000)

    # Jet stream (12-15km): maximum wind
    mask_jet = (altitude_m >= 12000) & (altitude_m < 15000)
    wind[mask_jet] = max_wind * np.exp(-((altitude_m[mask_jet] - 13500) / 3000) ** 2)

    # Stratosphere (>15km): decreasing
    mask_high = altitude_m >= 15000
    wind[mask_high] = 5.0 * (1.0 - (altitude_m[mask_high] - 15000) / 10000)
    wind[mask_high] = np.maximum(wind[mask_high], 2.0)

    return np.maximum(wind, 0.0)


class TurbulenceModel:
    """
    Simplified Dryden-like turbulence model.

    Generates stochastic turbulence components that affect:
    - Airspeed fluctuations
    - Angle of attack variations
    - Body-axis accelerations
    """

    def __init__(
        self,
        intensity_category: str = "moderate",
        scale_length: float = 100.0,
        seed: Optional[int] = None
    ):
        """
        Initialize turbulence model.

        Parameters:
            intensity_category: "light", "moderate", "severe"
            scale_length: Turbulence scale length (m)
            seed: Random seed for reproducibility
        """
        self.scale_length = scale_length
        self.seed = seed

        # Turbulence intensity factors (normalized)
        intensity_map = {
            "light": 0.5,
            "moderate": 1.0,
            "severe": 2.0,
            "extreme": 4.0
        }
        self.intensity_factor = intensity_map.get(intensity_category, 1.0)

    def generate_turbulence(
        self,
        velocity_ms: float,
        altitude_m: float,
        time_duration_s: float,
        dt_s: float = 0.1
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Generate turbulence time series.

        Uses filtered white noise approach (simplified Dryden).

        Parameters:
            velocity_ms: Aircraft velocity (m/s)
            altitude_m: Altitude (m)
            time_duration_s: Total simulation time (s)
            dt_s: Time step (s)

        Returns:
            (u_prime, v_prime, w_prime) - turbulence components (m/s)
        """
        if self.seed is not None:
            np.random.seed(self.seed)

        n_samples = int(time_duration_s / dt_s)
        time = np.arange(n_samples) * dt_s

        # Turbulence intensity scales with velocity and altitude
        # Higher altitude = less turbulence
        alt_factor = np.exp(-altitude_m / 15000.0)

        # Base turbulence intensity (m/s)
        sigma_base = 2.0 * self.intensity_factor * alt_factor

        # Generate white noise
        white_noise = np.random.randn(n_samples, 3)

        # Simple low-pass filter (first-order approximation)
        # Cutoff frequency based on scale length and velocity
        f_c = velocity_ms / (2 * np.pi * self.scale_length)

        # Filter each component (simple RC filter)
        alpha = 2 * np.pi * f_c * dt_s
        alpha = np.clip(alpha, 0.01, 0.99)

        u_prime = np.zeros(n_samples)
        v_prime = np.zeros(n_samples)
        w_prime = np.zeros(n_samples)

        for i in range(1, n_samples):
            u_prime[i] = u_prime[i-1] + alpha * (sigma_base * white_noise[i, 0] - u_prime[i-1])
            v_prime[i] = v_prime[i-1] + alpha * (sigma_base * white_noise[i, 1] - v_prime[i-1])
            w_prime[i] = w_prime[i-1] + alpha * (sigma_base * white_noise[i, 2] - w_prime[i-1])

        return u_prime, v_prime, w_prime

    def compute_equivalent_gust(
        self,
        velocity_ms: float,
        altitude_m: float,
        time_duration_s: float,
        dt_s: float = 0.1
    ) -> np.ndarray:
        """
        Compute equivalent gust velocity for loads analysis.

        Returns:
            Gust velocity magnitude time series (m/s)
        """
        u, v, w = self.generate_turbulence(velocity_ms, altitude_m, time_duration_s, dt_s)
        return np.sqrt(u**2 + v**2 + w**2)


def combined_atmospheric_variability(
    altitude_m: float,
    time_hours: float,
    velocity_ms: float,
    include_turbulence: bool = True
) -> dict:
    """
    Combine all atmospheric variability effects.

    Parameters:
        altitude_m: Flight altitude (m)
        time_hours: Time of day (hours)
        velocity_ms: Aircraft velocity (m/s)
        include_turbulence: Whether to include turbulence

    Returns:
        Dictionary with:
        - delta_T: Temperature perturbation (K)
        - wind_longitudinal: Wind component (m/s)
        - turbulence_components: (u', v', w') if requested
    """
    # Temperature variation
    delta_T = temperature_perturbation(altitude_m, time_hours, amplitude=5.0)

    # Wind (simplified - use Hale profile)
    wind_longitudinal = wind_profile_hale(altitude_m, cruise_altitude=20000)[0]

    # Turbulence (if requested)
    turbulence = None
    if include_turbulence and velocity_ms > 0:
        turb_model = TurbulenceModel(intensity_category="moderate")
        # For a single point, compute static turbulence intensity
        turbulence = 1.0 * np.exp(-altitude_m / 15000.0)

    return {
        "delta_T": float(delta_T) if np.ndim(delta_T) == 0 else delta_T,
        "wind_longitudinal": float(wind_longitudinal),
        "turbulence_intensity": turbulence
    }


# Test function
if __name__ == "__main__":
    print("=== Atmospheric Variability Test ===\n")

    # Test altitude range
    altitudes = np.linspace(0, 25000, 26)

    # Wind profiles
    wind_log = wind_profile_logarithmic(altitudes, z0=0.1, ustar=0.5)
    wind_lin = wind_profile_linear(altitudes, wind_speed_ref=15.0, ref_altitude=100)
    wind_hale = wind_profile_hale(altitudes, cruise_altitude=20000, max_wind=35.0)

    print(f"{'Alt (m)':<10} {'Logarithmic':<12} {'Linear':<12} {'HALE':<12}")
    print("-" * 46)
    for i, alt in enumerate([0, 5000, 10000, 13000, 15000, 18000, 20000, 25000]):
        idx = np.argmin(np.abs(altitudes - alt))
        print(f"{alt:<10.0f} {wind_log[idx]:<12.1f} {wind_lin[idx]:<12.1f} {wind_hale[idx]:<12.1f}")

    # Temperature perturbation
    print("\n=== Temperature Perturbation ===")
    times = [6, 12, 18, 24]
    for t in times:
        delta_T = temperature_perturbation(10000, t, amplitude=5.0)
        print(f"Time {t:02d}:00, alt 10km: ΔT = {delta_T:.2f} K")

    # Turbulence
    print("\n=== Turbulence Test ===")
    turb = TurbulenceModel(intensity_category="moderate", seed=42)
    u, v, w = turb.generate_turbulence(velocity_ms=25, altitude_m=20000,
                                        time_duration_s=60, dt_s=1.0)
    print(f"Turbulence at 20km, V=25m/s:")
    print(f"  RMS u': {np.std(u):.2f} m/s")
    print(f"  RMS v': {np.std(v):.2f} m/s")
    print(f"  RMS w': {np.std(w):.2f} m/s")