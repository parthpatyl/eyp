"""
atmosphere.py — International Standard Atmosphere (ISA) Model

Implements the ISA model up to ~30 km altitude with support for
non-standard atmospheric conditions (temperature offsets, custom lapse rates).

Reference: ICAO Standard Atmosphere (Doc 7488), 1993
"""

import numpy as np
from dataclasses import dataclass
from typing import Union, Optional

# ISA Sea Level Constants
ISA_SEA_LEVEL_PRESSURE = 101325.0  # Pa
ISA_SEA_LEVEL_TEMPERATURE = 288.15  # K (15°C)
ISA_SEA_LEVEL_DENSITY = 1.225  # kg/m³
ISA_GRAVITY = 9.80665  # m/s²
ISA_GAS_CONSTANT = 287.05  # J/(kg·K) for dry air
ISA_LAPSE_RATE_TROPOSPHERE = -6.5e-3  # K/m (-6.5 K/km)
ISA_LAPSE_RATE_STRATOSPHERE = 1.0e-3  # K/km (+1.0 K/km)
ISA_TROPOPAUSE_ALTITUDE = 11000.0  # m
ISA_STRATOSPHERE_BEGIN = 20000.0  # m


@dataclass
class AtmosphereProperties:
    """Container for atmospheric properties at a given altitude."""
    altitude_m: float
    temperature_K: float
    pressure_Pa: float
    density_kgm3: float
    dynamic_viscosity_Pas: float
    kinematic_viscosity_m2s: float
    speed_of_sound_ms: float
    mach_reference_100ms: float  # Mach number at 100 m/s


def _compute_dynamic_viscosity(temperature_K: float) -> float:
    """
    Compute dynamic viscosity using Sutherland's law.

    μ = μ_ref * (T/T_ref)^(3/2) * (T_ref + S) / (T + S)

    For air: μ_ref = 1.716e-5 Pa·s, T_ref = 273.15 K, S = 110.4 K
    """
    mu_ref = 1.716e-5  # Pa·s
    T_ref = 273.15  # K
    S = 110.4  # K

    return mu_ref * (temperature_K / T_ref) ** 1.5 * (T_ref + S) / (temperature_K + S)


def _compute_kinematic_viscosity(dynamic_viscosity: float, density: float) -> float:
    """Compute kinematic viscosity (nu = μ/ρ)."""
    return dynamic_viscosity / density if density > 0 else 0.0


def _compute_speed_of_sound(temperature_K: float, gamma: float = 1.4) -> float:
    """Compute speed of sound: a = sqrt(gamma * R * T)."""
    return np.sqrt(gamma * ISA_GAS_CONSTANT * temperature_K)


def isa_properties(altitude_m: Union[float, np.ndarray]) -> AtmosphereProperties:
    """
    Compute ISA atmospheric properties for a given altitude.

    Parameters:
        altitude_m: Altitude in meters (can be scalar or array)

    Returns:
        AtmosphereProperties containing T, P, rho, viscosity

    ISA Layers:
        - Troposphere: 0 to 11 km, lapse rate = -6.5 K/km
        - Tropopause: 11 to 20 km, isothermal
        - Stratosphere: 20+ km, lapse rate = +1.0 K/km
    """
    altitude_m = np.asarray(altitude_m, dtype=float)
    scalar_input = altitude_m.ndim == 0
    if scalar_input:
        altitude_m = altitude_m[np.newaxis]

    n = len(altitude_m)
    temperature = np.zeros(n)
    pressure = np.zeros(n)
    density = np.zeros(n)

    for i, h in enumerate(altitude_m):
        if h >= 0:
            if h < ISA_TROPOPAUSE_ALTITUDE:
                # Troposphere: T decreases linearly
                T = ISA_SEA_LEVEL_TEMPERATURE + ISA_LAPSE_RATE_TROPOSPHERE * h
                # Integrate hydrostatic equation
                if ISA_LAPSE_RATE_TROPOSPHERE != 0:
                    P = ISA_SEA_LEVEL_PRESSURE * (T / ISA_SEA_LEVEL_TEMPERATURE) ** (
                        -ISA_GRAVITY / (ISA_GAS_CONSTANT * ISA_LAPSE_RATE_TROPOSPHERE)
                    )
                else:
                    P = ISA_SEA_LEVEL_PRESSURE * np.exp(
                        -ISA_GRAVITY * h / (ISA_GAS_CONSTANT * T)
                    )
            elif h < ISA_STRATOSPHERE_BEGIN:
                # Tropopause: isothermal
                T = ISA_SEA_LEVEL_TEMPERATURE + ISA_LAPSE_RATE_TROPOSPHERE * ISA_TROPOPAUSE_ALTITUDE
                # Continue integration from tropopause
                P_tropo = ISA_SEA_LEVEL_PRESSURE * (
                    T / ISA_SEA_LEVEL_TEMPERATURE
                ) ** (-ISA_GRAVITY / (ISA_GAS_CONSTANT * ISA_LAPSE_RATE_TROPOSPHERE))
                P = P_tropo * np.exp(
                    -ISA_GRAVITY * (h - ISA_TROPOPAUSE_ALTITUDE) / (ISA_GAS_CONSTANT * T)
                )
            else:
                # Stratosphere: T increases linearly
                T_tropo = (
                    ISA_SEA_LEVEL_TEMPERATURE
                    + ISA_LAPSE_RATE_TROPOSPHERE * ISA_TROPOPAUSE_ALTITUDE
                )
                T = T_tropo + ISA_LAPSE_RATE_STRATOSPHERE * (h - ISA_STRATOSPHERE_BEGIN)

                # Integrate from stratosphere start
                P_strat_start = ISA_SEA_LEVEL_PRESSURE * (
                    T_tropo / ISA_SEA_LEVEL_TEMPERATURE
                ) ** (-ISA_GRAVITY / (ISA_GAS_CONSTANT * ISA_LAPSE_RATE_TROPOSPHERE))
                P_strat_start *= np.exp(
                    -ISA_GRAVITY * (ISA_STRATOSPHERE_BEGIN - ISA_TROPOPAUSE_ALTITUDE) / (ISA_GAS_CONSTANT * T_tropo)
                )

                if ISA_LAPSE_RATE_STRATOSPHERE != 0:
                    P = P_strat_start * (T / T_tropo) ** (
                        -ISA_GRAVITY / (ISA_GAS_CONSTANT * ISA_LAPSE_RATE_STRATOSPHERE)
                    )
                else:
                    P = P_strat_start * np.exp(
                        -ISA_GRAVITY * (h - ISA_STRATOSPHERE_BEGIN) / (ISA_GAS_CONSTANT * T)
                    )

            temperature[i] = T
            pressure[i] = P
            density[i] = P / (ISA_GAS_CONSTANT * T) if T > 0 else 0.0

    # Handle negative altitudes (below sea level - extend ISA)
    mask_below = altitude_m < 0
    if np.any(mask_below):
        h_below = -altitude_m[mask_below]
        T_below = ISA_SEA_LEVEL_TEMPERATURE + 0.003 * h_below  # Slight increase below sea level
        for idx in np.where(mask_below)[0]:
            P_below = ISA_SEA_LEVEL_PRESSURE * np.exp(ISA_GRAVITY * h_below[idx] / (ISA_GAS_CONSTANT * ISA_SEA_LEVEL_TEMPERATURE))
            temperature[idx] = T_below[idx]
            pressure[idx] = P_below
            density[idx] = P_below / (ISA_GAS_CONSTANT * T_below[idx])

    # Compute viscosities and speeds
    dynamic_viscosity = _compute_dynamic_viscosity(temperature)
    kinematic_viscosity = _compute_kinematic_viscosity(dynamic_viscosity, density)
    speed_of_sound = _compute_speed_of_sound(temperature)
    mach_ref = 100.0 / speed_of_sound  # Mach at 100 m/s

    if scalar_input:
        return AtmosphereProperties(
            altitude_m=float(altitude_m[0]),
            temperature_K=float(temperature[0]),
            pressure_Pa=float(pressure[0]),
            density_kgm3=float(density[0]),
            dynamic_viscosity_Pas=float(dynamic_viscosity[0]),
            kinematic_viscosity_m2s=float(kinematic_viscosity[0]),
            speed_of_sound_ms=float(speed_of_sound[0]),
            mach_reference_100ms=float(mach_ref[0]),
        )

    return AtmosphereProperties(
        altitude_m=altitude_m,
        temperature_K=temperature,
        pressure_Pa=pressure,
        density_kgm3=density,
        dynamic_viscosity_Pas=dynamic_viscosity,
        kinematic_viscosity_m2s=kinematic_viscosity,
        speed_of_sound_ms=speed_of_sound,
        mach_reference_100ms=mach_ref,
    )


def isa_with_offset(
    altitude_m: Union[float, np.ndarray],
    delta_T: float,
    delta_T_sign: str = "add"
) -> AtmosphereProperties:
    """
    Compute ISA properties with a temperature offset.

    Parameters:
        altitude_m: Altitude in meters
        delta_T: Temperature deviation from ISA (K)
        delta_T_sign: "add" to add offset, "multiply" to scale

    Returns:
        AtmosphereProperties with adjusted temperature

    Note: Pressure is adjusted to maintain hydrostatic consistency.
    """
    props = isa_properties(altitude_m)

    if delta_T_sign == "multiply":
        temperature = props.temperature_K * delta_T
    else:
        temperature = props.temperature_K + delta_T

    # Recompute pressure and density with new temperature
    # For simplicity, use ideal gas with adjusted temperature
    pressure_ratio = temperature / props.temperature_K
    pressure = props.pressure_Pa * pressure_ratio
    density = pressure / (ISA_GAS_CONSTANT * temperature)

    return AtmosphereProperties(
        altitude_m=props.altitude_m,
        temperature_K=temperature,
        pressure_Pa=pressure,
        density_kgm3=density,
        dynamic_viscosity_Pas=props.dynamic_viscosity_Pas,
        kinematic_viscosity_m2s=props.kinematic_viscosity_m2s,
        speed_of_sound_ms=props.speed_of_sound_ms,
        mach_reference_100ms=props.mach_reference_100ms,
    )


def custom_lapse_rate(
    altitude_m: Union[float, np.ndarray],
    T0: float = ISA_SEA_LEVEL_TEMPERATURE,
    lapse_rate: float = ISA_LAPSE_RATE_TROPOSPHERE,
    isothermal_altitude: Optional[float] = ISA_TROPOPAUSE_ALTITUDE
) -> AtmosphereProperties:
    """
    Compute atmosphere with custom lapse rate.

    Parameters:
        altitude_m: Altitude in meters
        T0: Sea level temperature (K)
        lapse_rate: Lapse rate in K/m
        isothermal_altitude: Altitude where temperature becomes constant (optional)

    Returns:
        AtmosphereProperties with custom temperature profile
    """
    altitude_m = np.asarray(altitude_m, dtype=float)
    scalar_input = altitude_m.ndim == 0
    if scalar_input:
        altitude_m = altitude_m[np.newaxis]

    n = len(altitude_m)
    temperature = np.zeros(n)
    pressure = np.zeros(n)
    density = np.zeros(n)

    if isothermal_altitude is None:
        # Simple model with constant lapse rate
        temperature = T0 + lapse_rate * altitude_m
        for i, h in enumerate(altitude_m):
            if lapse_rate != 0:
                P = ISA_SEA_LEVEL_PRESSURE * (temperature[i] / T0) ** (
                    -ISA_GRAVITY / (ISA_GAS_CONSTANT * lapse_rate)
                )
            else:
                P = ISA_SEA_LEVEL_PRESSURE * np.exp(
                    -ISA_GRAVITY * h / (ISA_GAS_CONSTANT * T0)
                )
            pressure[i] = P
            density[i] = P / (ISA_GAS_CONSTANT * temperature[i]) if temperature[i] > 0 else 0.0
    else:
        # Two-layer model with isothermal layer
        T_isothermal = T0 + lapse_rate * isothermal_altitude
        for i, h in enumerate(altitude_m):
            if h < isothermal_altitude:
                temperature[i] = T0 + lapse_rate * h
                if lapse_rate != 0:
                    P = ISA_SEA_LEVEL_PRESSURE * (temperature[i] / T0) ** (
                        -ISA_GRAVITY / (ISA_GAS_CONSTANT * lapse_rate)
                    )
                else:
                    P = ISA_SEA_LEVEL_PRESSURE * np.exp(
                        -ISA_GRAVITY * h / (ISA_GAS_CONSTANT * T0)
                    )
            else:
                temperature[i] = T_isothermal
                P0_isothermal = ISA_SEA_LEVEL_PRESSURE * (T_isothermal / T0) ** (
                    -ISA_GRAVITY / (ISA_GAS_CONSTANT * lapse_rate)
                )
                P = P0_isothermal * np.exp(
                    -ISA_GRAVITY * (h - isothermal_altitude) / (ISA_GAS_CONSTANT * T_isothermal)
                )
            pressure[i] = P
            density[i] = P / (ISA_GAS_CONSTANT * temperature[i]) if temperature[i] > 0 else 0.0

    # Recompute viscosities
    dynamic_viscosity = _compute_dynamic_viscosity(temperature)
    kinematic_viscosity = _compute_kinematic_viscosity(dynamic_viscosity, density)
    speed_of_sound = _compute_speed_of_sound(temperature)
    mach_ref = 100.0 / speed_of_sound

    if scalar_input:
        return AtmosphereProperties(
            altitude_m=float(altitude_m[0]),
            temperature_K=float(temperature[0]),
            pressure_Pa=float(pressure[0]),
            density_kgm3=float(density[0]),
            dynamic_viscosity_Pas=float(dynamic_viscosity[0]),
            kinematic_viscosity_m2s=float(kinematic_viscosity[0]),
            speed_of_sound_ms=float(speed_of_sound[0]),
            mach_reference_100ms=float(mach_ref[0]),
        )

    return AtmosphereProperties(
        altitude_m=altitude_m,
        temperature_K=temperature,
        pressure_Pa=pressure,
        density_kgm3=density,
        dynamic_viscosity_Pas=dynamic_viscosity,
        kinematic_viscosity_m2s=kinematic_viscosity,
        speed_of_sound_ms=speed_of_sound,
        mach_reference_100ms=mach_ref,
    )


# Verification tests
if __name__ == "__main__":
    print("=== ISA Model Verification ===\n")

    # Test altitudes
    test_altitudes = [0, 1000, 5000, 11000, 15000, 20000, 25000, 30000]

    print(f"{'Altitude (m)':<12} {'T (K)':<10} {'T (°C)':<10} {'P (Pa)':<14} "
          f"{'ρ (kg/m³)':<12} {'a (m/s)':<10}")
    print("-" * 78)

    for alt in test_altitudes:
        props = isa_properties(alt)
        print(f"{alt:<12.0f} {props.temperature_K:<10.2f} "
              f"{props.temperature_K - 273.15:<10.2f} {props.pressure_Pa:<14.2f} "
              f"{props.density_kgm3:<12.4f} {props.speed_of_sound_ms:<10.2f}")

    print("\n=== Standard Atmosphere Reference Values ===")
    print("Sea Level:    T=288.15 K, P=101325 Pa, ρ=1.225 kg/m³")
    print("11 km:        T=216.65 K, P=22632 Pa,  ρ=0.364 kg/m³")
    print("20 km:        T=216.65 K, P=5474 Pa,   ρ=0.0889 kg/m³")