"""
simulation.py — Main Simulation Pipeline

Time-stepped simulation for HALE UAV mission profiles.
Integrates all components: atmosphere, solar, aerodynamics, propulsion.
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Optional, List, Tuple, Dict, Callable
from datetime import datetime, timedelta

from atmosphere import isa_properties, AtmosphereProperties
from solar_irradiance import calculate_irradiance, compute_solar_position
from aerodynamics import (
    compute_lift, compute_drag, compute_cruise_cl, compute_cruise_cd,
    compute_power_required as compute_aero_power
)
from propulsion import SimplifiedPropulsion, PropulsionSystem
from variability import (
    temperature_perturbation, wind_profile_hale,
    TurbulenceModel, combined_atmospheric_variability
)


@dataclass
class AircraftConfig:
    """Aircraft configuration parameters."""
    wing_area_m2: float = 10.0
    mass_kg: float = 25.0
    CL_max: float = 1.5
    CD0: float = 0.02
    K_factor: float = 0.04  # Induced drag factor
    CL0: float = 0.0  # Zero-lift coefficient
    CL_alpha: float = 5.0  # Lift curve slope (per rad)
    alpha_stall: float = 15.0  # Stall angle (deg)
    propeller_diameter_m: float = 1.5


@dataclass
class MissionConfig:
    """Mission configuration parameters."""
    cruise_altitude_m: float = 20000.0
    cruise_speed_ms: float = 25.0
    day_of_year: int = 172  # Summer solstice
    latitude_deg: float = 47.38
    longitude_deg: float = 8.53
    mission_duration_hours: float = 24.0
    time_step_minutes: float = 5.0
    start_time_hours: float = 6.0  # Sunrise-ish
    include_variability: bool = True
    include_turbulence: bool = True
    solar_panel_efficiency: float = 0.22
    solar_panel_area: float = 8.0  # m²


@dataclass
class SimulationResults:
    """Container for simulation results."""
    time_hours: np.ndarray
    time_seconds: np.ndarray
    altitude_m: np.ndarray
    temperature_K: np.ndarray
    pressure_Pa: np.ndarray
    density_kgm3: np.ndarray
    solar_irradiance_Wm2: np.ndarray
    power_generated_W: np.ndarray
    lift_N: np.ndarray
    drag_N: np.ndarray
    CL: np.ndarray
    CD: np.ndarray
    power_required_W: np.ndarray
    energy_balance_Wh: np.ndarray
    wind_ms: np.ndarray
    delta_T_K: np.ndarray
    turbulence_W: np.ndarray = None

    def to_dataframe(self) -> pd.DataFrame:
        """Convert to pandas DataFrame."""
        data = {
            "time_hours": self.time_hours,
            "altitude_m": self.altitude_m,
            "temperature_K": self.temperature_K,
            "pressure_Pa": self.pressure_Pa,
            "density_kgm3": self.density_kgm3,
            "solar_irradiance_Wm2": self.solar_irradiance_Wm2,
            "power_generated_W": self.power_generated_W,
            "lift_N": self.lift_N,
            "drag_N": self.drag_N,
            "CL": self.CL,
            "CD": self.CD,
            "power_required_W": self.power_required_W,
            "energy_balance_Wh": self.energy_balance_Wh,
            "wind_ms": self.wind_ms,
            "delta_T_K": self.delta_T_K,
        }
        if self.turbulence_W is not None:
            data["turbulence_W"] = self.turbulence_W

        return pd.DataFrame(data)


class MissionSimulation:
    """
    HALE UAV Mission Simulation.

    Orchestrates time-stepped simulation integrating:
    1. Atmospheric model (ISA + variations)
    2. Solar irradiance
    3. Aerodynamic forces
    4. Propulsion power requirements
    5. Energy balance
    """

    def __init__(
        self,
        aircraft: Optional[AircraftConfig] = None,
        mission: Optional[MissionConfig] = None
    ):
        """
        Initialize simulation.

        Parameters:
            aircraft: Aircraft configuration
            mission: Mission configuration
        """
        self.aircraft = aircraft if aircraft else AircraftConfig()
        self.mission = mission if mission else MissionConfig()

        # Initialize propulsion system
        self.propulsion = SimplifiedPropulsion(
            propeller_diameter_m=self.aircraft.propeller_diameter_m,
            motor_efficiency=0.85,
            prop_efficiency=0.75
        )

        # Initialize turbulence model
        self.turbulence_model = TurbulenceModel(
            intensity_category="moderate",
            seed=42
        )

        # Results storage
        self.results: Optional[SimulationResults] = None

    def set_aircraft(
        self,
        wing_area: float,
        mass: float,
        CL_max: float = 1.5,
        CD0: float = 0.02,
        K_factor: float = 0.04
    ) -> None:
        """Update aircraft configuration."""
        self.aircraft.wing_area_m2 = wing_area
        self.aircraft.mass_kg = mass
        self.aircraft.CL_max = CL_max
        self.aircraft.CD0 = CD0
        self.aircraft.K_factor = K_factor

    def set_location(
        self,
        latitude_deg: float,
        longitude_deg: float = 0.0,
        day_of_year: int = 172
    ) -> None:
        """Update mission location."""
        self.mission.latitude_deg = latitude_deg
        self.mission.longitude_deg = longitude_deg
        self.mission.day_of_year = day_of_year

    def run(self) -> SimulationResults:
        """
        Execute the mission simulation.

        Returns:
            SimulationResults object
        """
        # Time vector
        n_steps = int(self.mission.mission_duration_hours * 60 / self.mission.time_step_minutes)
        time_hours = self.mission.start_time_hours + np.arange(n_steps) * self.mission.time_step_minutes / 60.0

        # Wrap time to 0-24
        time_hours = np.mod(time_hours, 24.0)
        time_seconds = time_hours * 3600.0

        # Allocate arrays
        n = len(time_hours)
        altitude = np.full(n, self.mission.cruise_altitude_m)
        temperature = np.zeros(n)
        pressure = np.zeros(n)
        density = np.zeros(n)
        irradiance = np.zeros(n)
        power_gen = np.zeros(n)
        lift = np.zeros(n)
        drag = np.zeros(n)
        CL = np.zeros(n)
        CD = np.zeros(n)
        power_req = np.zeros(n)
        energy_balance = np.zeros(n)
        wind = np.zeros(n)
        delta_T = np.zeros(n)
        turbulence = np.zeros(n) if self.mission.include_turbulence else None

        # Compute ISA properties at cruise altitude
        isa = isa_properties(self.mission.cruise_altitude_m)

        # Weight for lift calculation
        weight_N = self.aircraft.mass_kg * 9.80665

        # Energy accumulator
        cumulative_energy_Wh = 0.0

        # Time step in hours for integration
        dt_hours = self.mission.time_step_minutes / 60.0

        for i, t in enumerate(time_hours):
            # --- 1. Atmosphere ---
            if self.mission.include_variability:
                # Apply temperature perturbation
                dT = temperature_perturbation(
                    self.mission.cruise_altitude_m,
                    t,
                    amplitude=5.0,
                    reference_altitude=10000.0
                )
                # Extract scalar value
                dT = float(dT) if np.ndim(dT) > 0 else dT
                # Use perturbed temperature
                T = float(isa.temperature_K) + dT
                # Adjust density accordingly
                if isa.temperature_K > 0:
                    rho = float(isa.density_kgm3) * (T / float(isa.temperature_K))
                    P = float(isa.pressure_Pa) * (T / float(isa.temperature_K))
                else:
                    rho = float(isa.density_kgm3)
                    P = float(isa.pressure_Pa)
            else:
                T = float(isa.temperature_K)
                P = float(isa.pressure_Pa)
                rho = float(isa.density_kgm3)

            temperature[i] = T
            pressure[i] = P
            density[i] = rho
            delta_T[i] = dT if self.mission.include_variability else 0.0

            # --- 2. Wind ---
            if self.mission.include_variability:
                wind[i] = wind_profile_hale(
                    self.mission.cruise_altitude_m,
                    cruise_altitude=self.mission.cruise_altitude_m,
                    max_wind=30.0
                )[0]
            else:
                wind[i] = 0.0

            # --- 3. Solar Irradiance ---
            cloud_cover = 0.0  # Clear sky
            irr = calculate_irradiance(
                t,
                self.mission.day_of_year,
                self.mission.latitude_deg,
                cloud_cover=cloud_cover,
                altitude_m=self.mission.cruise_altitude_m
            )
            irradiance[i] = irr

            # Solar power generated
            power_gen[i] = irr * self.mission.solar_panel_area * self.mission.solar_panel_efficiency

            # --- 4. Aerodynamics ---
            # Use actual airspeed (account for wind)
            V = self.mission.cruise_speed_ms

            # Required CL for steady flight
            CL_req = compute_cruise_cl(
                self.aircraft.mass_kg,
                rho,
                V,
                self.aircraft.wing_area_m2
            )
            CL[i] = CL_req

            # CD from polar
            CD[i] = compute_cruise_cd(CL_req, self.aircraft.CD0, self.aircraft.K_factor)

            # Forces
            lift[i] = compute_lift(rho, V, self.aircraft.wing_area_m2, CL_req)
            drag[i] = compute_drag(rho, V, self.aircraft.wing_area_m2, CD[i])

            # --- 5. Propulsion Power ---
            P_req = self.propulsion.power_required(drag[i], V)
            power_req[i] = P_req

            # --- 6. Turbulence (optional power perturbation) ---
            if self.mission.include_turbulence and self.mission.include_variability:
                turb_intensity = 1.0 * np.exp(-self.mission.cruise_altitude_m / 15000.0)
                turbulence[i] = turb_intensity * np.sin(2 * np.pi * t)
                # Add small power perturbation
                power_req[i] += turbulence[i] * 5.0

            # --- 7. Energy Balance ---
            energy_balance_step = (power_gen[i] - power_req[i]) * dt_hours
            cumulative_energy_Wh += energy_balance_step
            energy_balance[i] = cumulative_energy_Wh

        # Store results
        self.results = SimulationResults(
            time_hours=time_hours,
            time_seconds=time_seconds,
            altitude_m=altitude,
            temperature_K=temperature,
            pressure_Pa=pressure,
            density_kgm3=density,
            solar_irradiance_Wm2=irradiance,
            power_generated_W=power_gen,
            lift_N=lift,
            drag_N=drag,
            CL=CL,
            CD=CD,
            power_required_W=power_req,
            energy_balance_Wh=energy_balance,
            wind_ms=wind,
            delta_T_K=delta_T,
            turbulence_W=turbulence
        )

        return self.results

    def get_results(self) -> SimulationResults:
        """Get simulation results."""
        if self.results is None:
            self.run()
        return self.results

    def get_dataframe(self) -> pd.DataFrame:
        """Get results as DataFrame."""
        return self.get_results().to_dataframe()

    def summary(self) -> Dict:
        """
        Compute mission summary statistics.

        Returns:
            Dictionary with key metrics
        """
        res = self.get_results()

        # Find daylight hours
        daylight_mask = res.solar_irradiance_Wm2 > 10

        summary = {
            "mission_duration_hours": self.mission.mission_duration_hours,
            "cruise_altitude_m": self.mission.cruise_altitude_m,
            "cruise_speed_ms": self.mission.cruise_speed_ms,
            "aircraft_mass_kg": self.aircraft.mass_kg,
            "wing_area_m2": self.aircraft.wing_area_m2,

            # Atmospheric
            "avg_temperature_K": np.mean(res.temperature_K),
            "avg_density_kgm3": np.mean(res.density_kgm3),

            # Solar
            "peak_irradiance_Wm2": np.max(res.solar_irradiance_Wm2),
            "total_solar_energy_Wh": np.sum(res.power_generated_W * (self.mission.time_step_minutes / 60)),
            "daylight_hours": np.sum(daylight_mask) * self.mission.time_step_minutes / 60,

            # Power
            "avg_power_required_W": np.mean(res.power_required_W),
            "max_power_required_W": np.max(res.power_required_W),
            "avg_power_generated_W": np.mean(res.power_generated_W[daylight_mask]),
            "peak_power_generated_W": np.max(res.power_generated_W),

            # Energy
            "final_energy_Wh": res.energy_balance_Wh[-1],
            "energy_margin_percent": (res.energy_balance_Wh[-1] / (np.mean(res.power_required_W) * 24)) * 100,

            # Flight conditions
            "avg_drag_N": np.mean(res.drag_N),
            "avg_wind_ms": np.mean(res.wind_ms),
        }

        return summary


def run_default_simulation() -> Tuple[SimulationResults, Dict]:
    """
    Run default HALE UAV mission simulation.

    Returns:
        (SimulationResults, summary_dict)
    """
    # Aircraft: 25kg HALE, 10m² wing, typical parameters
    aircraft = AircraftConfig(
        wing_area_m2=10.0,
        mass_kg=25.0,
        CL_max=1.5,
        CD0=0.02,
        K_factor=0.04,
        propeller_diameter_m=1.5
    )

    # Mission: 24-hour flight at 20km, summer conditions
    mission = MissionConfig(
        cruise_altitude_m=20000.0,
        cruise_speed_ms=25.0,
        day_of_year=172,
        latitude_deg=47.38,
        longitude_deg=8.53,
        mission_duration_hours=24.0,
        time_step_minutes=5.0,
        start_time_hours=6.0,
        include_variability=True,
        include_turbulence=True,
        solar_panel_efficiency=0.22,
        solar_panel_area=8.0
    )

    sim = MissionSimulation(aircraft=aircraft, mission=mission)
    results = sim.run()
    summary = sim.summary()

    return results, summary


# Test function
if __name__ == "__main__":
    print("=== HALE UAV Mission Simulation ===\n")

    results, summary = run_default_simulation()

    print("Mission Summary:")
    print("-" * 50)
    for key, value in summary.items():
        if isinstance(value, float):
            print(f"{key}: {value:.1f}")
        else:
            print(f"{key}: {value}")

    print("\n=== Sample Results ===")
    df = results.to_dataframe()
    print(df[["time_hours", "density_kgm3", "solar_irradiance_Wm2",
              "power_required_W", "power_generated_W", "energy_balance_Wh"]].head(10))