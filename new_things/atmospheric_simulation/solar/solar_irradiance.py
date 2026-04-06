"""
solar_irradiance.py — Solar Irradiance Integration

Computes solar irradiance for given location, time, and altitude.
Integrates with existing solar_model.py in energy_management/.

Optional: NASA POWER data fetching for real-world validation.
"""

import numpy as np
import sys
from pathlib import Path
from typing import Union, Optional, Tuple

# Try to import the existing solar model
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "energy_management"))
    from solar_model import calculate_solar_irradiance as _calc_irradiance_base
    SOLAR_MODEL_AVAILABLE = True
except ImportError:
    SOLAR_MODEL_AVAILABLE = False
    print("Warning: Could not import solar_model.py, using built-in model")


def calculate_irradiance(
    time_hours: Union[float, np.ndarray],
    day_of_year: int = 172,
    latitude_deg: float = 47.38,
    cloud_cover: Union[float, np.ndarray] = 0.0,
    altitude_m: float = 0.0
) -> np.ndarray:
    """
    Calculate solar irradiance on a horizontal surface.

    Parameters:
        time_hours: Time of day in hours (0 to 24)
        day_of_year: Day of year (1-365)
        latitude_deg: Latitude in degrees (positive = north)
        cloud_cover: Cloud cover fraction (0.0 = clear, 1.0 = overcast)
        altitude_m: Altitude in meters (for altitude correction)

    Returns:
        Solar irradiance in W/m²
    """
    if SOLAR_MODEL_AVAILABLE:
        irradiance = _calc_irradiance_base(time_hours, day_of_year, latitude_deg, cloud_cover)
    else:
        irradiance = _builtin_irradiance(time_hours, day_of_year, latitude_deg, cloud_cover)

    # Apply altitude correction
    if altitude_m > 0:
        irradiance = altitude_correction(irradiance, altitude_m)

    return irradiance


def _builtin_irradiance(
    time_hours: Union[float, np.ndarray],
    day_of_year: int,
    latitude_deg: float,
    cloud_cover: Union[float, np.ndarray]
) -> np.ndarray:
    """
    Built-in solar irradiance calculation (fallback if solar_model.py unavailable).
    Based on simplified geometric solar position model.
    """
    S_0 = 1361.0  # Solar constant (W/m²)
    rho_at = 0.7  # Atmospheric transmittance

    time_hours = np.asarray(time_hours, dtype=float)
    lat_rad = np.radians(latitude_deg)

    # Solar declination angle
    declination_deg = 23.45 * np.sin(np.radians(360.0 / 365.0 * (day_of_year + 284)))
    decl_rad = np.radians(declination_deg)

    # Hour angle (solar noon = 12:00)
    hour_angle_deg = 15.0 * (time_hours - 12.0)
    hour_angle_rad = np.radians(hour_angle_deg)

    # Solar elevation angle
    sin_elev = np.sin(lat_rad) * np.sin(decl_rad) + np.cos(lat_rad) * np.cos(decl_rad) * np.cos(hour_angle_rad)
    elevation_rad = np.arcsin(np.clip(sin_elev, -1.0, 1.0))

    # Initialize output
    irradiance = np.zeros_like(time_hours, dtype=float)

    # Daytime only
    daytime_mask = elevation_rad > 0
    if not np.any(daytime_mask):
        return irradiance

    # Air mass (simple approximation)
    AM = 1.0 / np.sin(elevation_rad[daytime_mask])
    AM = np.clip(AM, 1.0, 20.0)  # Limit air mass

    # Direct normal irradiance
    I_direct = S_0 * (rho_at ** AM)

    # Project to horizontal surface
    irradiance[daytime_mask] = I_direct * np.sin(elevation_rad[daytime_mask])

    # Apply cloud cover
    cloud_cover = np.asarray(cloud_cover)
    if cloud_cover.ndim == 0:
        irradiance = irradiance * (1.0 - cloud_cover)
    else:
        irradiance = irradiance * (1.0 - cloud_cover)

    return np.clip(irradiance, 0, None)


def altitude_correction(irradiance: np.ndarray, altitude_m: float) -> np.ndarray:
    """
    Correct irradiance for altitude.

    At higher altitudes, there is less atmosphere to absorb/scatter sunlight.
    Approximate correction: I(h) = I(0) * (1 + 0.0001 * h) for clear sky.

    Parameters:
        irradiance: Irradiance at sea level (W/m²)
        altitude_m: Altitude in meters

    Returns:
        Corrected irradiance at altitude
    """
    # Simple exponential correction factor based on reduced air mass
    # At 20km, air mass is roughly 10% of sea level
    correction_factor = 1.0 + 0.00012 * altitude_m
    return irradiance * correction_factor


def fetch_nasa_power(
    latitude: float,
    longitude: float,
    start_year: int = 2020,
    end_year: int = 2024
) -> Optional[dict]:
    """
    Fetch solar irradiance data from NASA POWER (RET2 dataset).

    NASA POWER provides daily radiation data averaged over multi-year periods.
    This is an optional enhancement for validation.

    Parameters:
        latitude: Latitude in degrees
        longitude: Longitude in degrees
        start_year: Start year for averaging
        end_year: End year for averaging

    Returns:
        Dictionary with daily irradiance values or None if unavailable
    """
    try:
        import requests
    except ImportError:
        print("Warning: requests library not available for NASA POWER fetch")
        return None

    # NASA POWER API endpoint (RET2.5 format)
    # This is a simplified version - full API would require proper URL construction
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"

    params = {
        "parameters": "ALLSKY_SFC_SW_DWN",
        "community": "RE",
        "longitude": longitude,
        "latitude": latitude,
        "start": f"{start_year}0101",
        "end": f"{end_year}1231",
        "format": "JSON"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract relevant data
        irradiance_data = data.get("properties", {}).get("parameter", {})

        return irradiance_data

    except Exception as e:
        print(f"Warning: Could not fetch NASA POWER data: {e}")
        return None


def compute_solar_position(
    time_hours: float,
    day_of_year: int,
    latitude_deg: float
) -> Tuple[float, float, float]:
    """
    Compute solar position parameters.

    Parameters:
        time_hours: Time of day (hours)
        day_of_year: Day of year
        latitude_deg: Latitude (degrees)

    Returns:
        (elevation_deg, azimuth_deg, day_length_hours)
    """
    lat_rad = np.radians(latitude_deg)

    # Declination
    declination_deg = 23.45 * np.sin(np.radians(360.0 / 365.0 * (day_of_year + 284)))
    decl_rad = np.radians(declination_deg)

    # Hour angle
    hour_angle_deg = 15.0 * (time_hours - 12.0)
    hour_angle_rad = np.radians(hour_angle_deg)

    # Elevation
    sin_elev = np.sin(lat_rad) * np.sin(decl_rad) + np.cos(lat_rad) * np.cos(decl_rad) * np.cos(hour_angle_rad)
    elevation_rad = np.arcsin(np.clip(sin_elev, -1.0, 1.0))
    elevation_deg = np.degrees(elevation_rad)

    # Approximate azimuth (simplified)
    cos_azimuth = (np.sin(decl_rad) - np.sin(lat_rad) * sin_elev) / (np.cos(lat_rad) * np.cos(elevation_rad))
    azimuth_deg = np.degrees(np.arccos(np.clip(cos_azimuth, -1.0, 1.0)))
    if hour_angle_deg > 0:
        azimuth_deg = 360.0 - azimuth_deg

    # Day length (hours when sun is above horizon)
    cos_hour_angle = -np.tan(lat_rad) * np.tan(decl_rad)
    cos_hour_angle = np.clip(cos_hour_angle, -1.0, 1.0)
    hour_angle_sunset = np.arccos(cos_hour_angle)
    day_length_hours = 2.0 * np.degrees(hour_angle_sunset) / 15.0

    return elevation_deg, azimuth_deg, day_length_hours


def get_solar_noon(day_of_year: int, longitude_deg: float = 0.0) -> float:
    """
    Calculate solar noon time adjustment.

    Parameters:
        day_of_year: Day of year
        longitude_deg: Longitude (positive east)

    Returns:
        Solar noon time in hours (local standard time)
    """
    # Equation of time (approximate)
    B = 2 * np.pi * (day_of_year - 81) / 365
    EoT = 9.87 * np.sin(2 * B) - 7.53 * np.cos(B) - 1.5 * np.sin(B)

    # Solar noon adjustment for longitude
    longitude_correction = 4.0 * longitude_deg  # minutes

    solar_noon = 12.0 - (EoT + longitude_correction) / 60.0

    return solar_noon


# Test function
if __name__ == "__main__":
    print("=== Solar Irradiance Model Test ===\n")

    # Test time series
    time_span = np.linspace(0, 24, 241)

    # Clear sky
    irradiance_clear = calculate_irradiance(time_span, day_of_year=172, latitude_deg=47.38, cloud_cover=0.0)
    print(f"Clear sky peak irradiance: {np.max(irradiance_clear):.1f} W/m²")

    # Cloudy
    irradiance_cloudy = calculate_irradiance(time_span, day_of_year=172, latitude_deg=47.38, cloud_cover=0.7)
    print(f"70% cloud cover peak: {np.max(irradiance_cloudy):.1f} W/m²")

    # Altitude effect
    irradiance_20km = calculate_irradiance(time_span, day_of_year=172, latitude_deg=47.38, cloud_cover=0.0, altitude_m=20000)
    print(f"Clear sky at 20km peak: {np.max(irradiance_20km):.1f} W/m²")

    # Solar position
    elev, az, daylen = compute_solar_position(12.0, 172, 47.38)
    print(f"\nSolar position at noon (day 172, 47.38°N):")
    print(f"  Elevation: {elev:.1f}°")
    print(f"  Day length: {daylen:.1f} hours")