"""
main.py — HALE UAV Atmospheric Simulation Example

Demonstrates the complete atmospheric simulation model with:
- ISA atmosphere up to 20 km
- Solar irradiance integration
- Reduced-order aerodynamics
- Propulsion power calculations
- Atmospheric variability (wind, turbulence, temperature)
- Full visualization suite

Example: 24-hour mission at 20 km altitude, summer conditions
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Import simulation modules
from simulation import (
    MissionSimulation, AircraftConfig, MissionConfig,
    run_default_simulation
)
from atmosphere import isa_properties
from solar_irradiance import calculate_irradiance, compute_solar_position
from aerodynamics import compute_cruise_cl, compute_cruise_cd
from visualization import plot_all, plot_summary_dashboard


def print_header(title: str) -> None:
    """Print formatted header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_section(title: str) -> None:
    """Print formatted section."""
    print(f"\n--- {title} ---")


def main():
    """Run the complete HALE UAV simulation."""

    print_header("HALE UAV ATMOSPHERIC SIMULATION")
    print("Reduced-Order Model for Aerospace Vehicle Performance")

    # =========================================================================
    # Part 1: ISA Model Verification
    # =========================================================================
    print_section("1. ISA Model Verification")

    altitudes = [0, 5000, 10000, 15000, 20000, 25000]
    print(f"{'Altitude (m)':<12} {'T (K)':<10} {'P (kPa)':<12} {'ρ (kg/m³)':<12}")
    print("-" * 50)

    for alt in altitudes:
        props = isa_properties(alt)
        print(f"{alt:<12.0f} {props.temperature_K:<10.2f} "
              f"{props.pressure_Pa/1000:<12.2f} {props.density_kgm3:<12.4f}")

    # =========================================================================
    # Part 2: Solar Irradiance Test
    # =========================================================================
    print_section("2. Solar Irradiance")

    # 24-hour time span
    time_span = np.linspace(0, 24, 241)
    day_of_year = 172  # Summer solstice
    latitude = 47.38   # Zurich

    # Clear sky irradiance
    irradiance = calculate_irradiance(time_span, day_of_year, latitude, cloud_cover=0.0)

    print(f"Day of year: {day_of_year} (summer solstice)")
    print(f"Latitude: {latitude}°N")
    print(f"Peak irradiance: {np.max(irradiance):.1f} W/m²")
    print(f"Daytime hours: {np.sum(irradiance > 10) * 24 / 241:.1f} hours")

    # Solar position at noon
    elev, az, daylen = compute_solar_position(12.0, day_of_year, latitude)
    print(f"At noon: elevation = {elev:.1f}°, day length = {daylen:.1f}h")

    # =========================================================================
    # Part 3: Aerodynamic Calculations
    # =========================================================================
    print_section("3. Aerodynamic Performance")

    # Aircraft parameters
    mass = 25.0  # kg
    wing_area = 10.0  # m²
    velocity = 25.0  # m/s
    altitude = 20000  # m

    # Get atmospheric properties
    props = isa_properties(altitude)
    rho = props.density_kgm3

    # Cruise CL and CD
    CL_cruise = compute_cruise_cl(mass, rho, velocity, wing_area)
    CD_cruise = compute_cruise_cd(CL_cruise, CD0=0.02, K=0.04)

    print(f"Aircraft: {mass} kg, S = {wing_area} m²")
    print(f"Altitude: {altitude/1000:.0f} km")
    print(f"Air density: {rho:.5f} kg/m³")
    print(f"Cruise speed: {velocity} m/s")
    print(f"Required CL: {CL_cruise:.3f}")
    print(f"Drag coefficient: {CD_cruise:.4f}")

    from aerodynamics import compute_lift, compute_drag
    L = compute_lift(rho, velocity, wing_area, CL_cruise)
    D = compute_drag(rho, velocity, wing_area, CD_cruise)
    weight = mass * 9.80665

    print(f"Lift: {L:.1f} N (weight: {weight:.1f} N)")
    print(f"Drag: {D:.1f} N")
    print(f"L/D ratio: {L/D:.1f}")

    # =========================================================================
    # Part 4: Full Mission Simulation
    # =========================================================================
    print_section("4. 24-Hour Mission Simulation")

    # Create output directory
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    # Run simulation
    print("Running 24-hour mission simulation...")
    results, summary = run_default_simulation()

    print("\nMission Summary:")
    print("-" * 40)
    print(f"Duration: {summary['mission_duration_hours']} hours")
    print(f"Altitude: {summary['cruise_altitude_m']/1000:.0f} km")
    print(f"Cruise speed: {summary['cruise_speed_ms']} m/s")
    print(f"Aircraft mass: {summary['aircraft_mass_kg']} kg")

    print("\nAtmospheric Conditions:")
    print(f"  Average temperature: {summary['avg_temperature_K']:.1f} K")
    print(f"  Average density: {summary['avg_density_kgm3']:.5f} kg/m³")

    print("\nSolar Conditions:")
    print(f"  Peak irradiance: {summary['peak_irradiance_Wm2']:.1f} W/m²")
    print(f"  Daylight hours: {summary['daylight_hours']:.1f} hours")
    print(f"  Total solar energy: {summary['total_solar_energy_Wh']:.1f} Wh")

    print("\nPower:")
    print(f"  Avg power required: {summary['avg_power_required_W']:.1f} W")
    print(f"  Max power required: {summary['max_power_required_W']:.1f} W")
    print(f"  Avg power generated: {summary['avg_power_generated_W']:.1f} W")
    print(f"  Peak power generated: {summary['peak_power_generated_W']:.1f} W")

    print("\nEnergy:")
    print(f"  Final energy balance: {summary['final_energy_Wh']:.1f} Wh")
    print(f"  Energy margin: {summary['energy_margin_percent']:.1f}%")

    # =========================================================================
    # Part 5: Visualization
    # =========================================================================
    print_section("5. Visualization")

    df = results.to_dataframe()

    # Generate dashboard
    print("Generating summary dashboard...")
    plot_summary_dashboard(
        df,
        save_path=str(output_dir / "hale_simulation_dashboard.png"),
        show=False
    )

    # Generate individual plots
    print("Generating individual plots...")
    plot_all(df, save_dir=str(output_dir))

    print(f"\nAll plots saved to: {output_dir}")

    # =========================================================================
    # Part 6: Results Summary Table
    # =========================================================================
    print_section("6. Sample Results (every 2 hours)")

    sample_times = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    df_sample = df[df['time_hours'].isin(sample_times)]

    print(f"\n{'Time':<6} {'T (K)':<10} {'ρ (kg/m³)':<12} {'I (W/m²)':<12} "
          f"{'P_req (W)':<12} {'Energy (Wh)':<12}")
    print("-" * 70)

    for _, row in df_sample.iterrows():
        print(f"{row['time_hours']:<6.0f} {row['temperature_K']:<10.1f} "
              f"{row['density_kgm3']:<12.5f} {row['solar_irradiance_Wm2']:<12.1f} "
              f"{row['power_required_W']:<12.1f} {row['energy_balance_Wh']:<12.1f}")

    # =========================================================================
    # Part 7: Documentation
    # =========================================================================
    print_section("7. Model Documentation")

    print("""
This simulation model uses reduced-order methods:

1. ATMOSPHERE: ISA model (ICAO standard) with temperature perturbations
   - Troposphere: -6.5 K/km lapse rate
   - Tropopause: isothermal at 11-20 km
   - Stratosphere: +1.0 K/km lapse rate

2. SOLAR: Geometric solar position model
   - Solar constant: 1361 W/m²
   - Atmospheric transmittance: 0.7
   - Cloud cover factor (optional)

3. AERODYNAMICS: Analytical lift/drag equations
   - Lift: L = 0.5 * ρ * V² * S * CL
   - Drag: D = 0.5 * ρ * V² * S * CD
   - Drag polar: CD = CD0 + K * CL²

4. PROPULSION: Simplified motor/propeller model
   - Motor efficiency: 85%
   - Propeller efficiency: 75%

5. VARIABILITY: Wind, temperature, turbulence
   - Wind profile: HALE-specific with jet stream
   - Temperature: Diurnal variation
   - Turbulence: Stochastic model

LIMITATIONS:
- No Navier-Stokes or CFD simulation
- Empirical models only (no high-fidelity)
- Simplified propulsion (no motor database)
- No structural dynamics or aeroelasticity
""")

    print_header("SIMULATION COMPLETE")
    print(f"Results saved to: {output_dir}")
    print(f"Final energy balance: {summary['final_energy_Wh']:.1f} Wh")

    return results, summary


if __name__ == "__main__":
    results, summary = main()

    # Show the dashboard if running interactively
    plt.show()