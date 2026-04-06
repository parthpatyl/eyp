"""
atmospheric_simulation — HALE UAV Atmospheric Performance Model

A reduced-order computational model for simulating atmospheric variations
and their impact on HALE UAV performance.

Modules:
- atmosphere: International Standard Atmosphere (ISA) model
- solar_irradiance: Solar irradiance calculations
- aerodynamics: Reduced-order aerodynamic forces
- propulsion: Propulsion system integration
- variability: Atmospheric perturbations (wind, turbulence)
- simulation: Main time-stepped simulation pipeline
- visualization: Plotting utilities
- main: Example usage

Usage:
    from atmospheric_simulation import run_default_simulation
    results, summary = run_default_simulation()
"""

from .simulation import (
    MissionSimulation,
    AircraftConfig,
    MissionConfig,
    SimulationResults,
    run_default_simulation
)

from .atmosphere import (
    isa_properties,
    AtmosphereProperties,
    isa_with_offset,
    custom_lapse_rate
)

from .solar_irradiance import (
    calculate_irradiance,
    compute_solar_position,
    altitude_correction
)

from .aerodynamics import (
    compute_lift,
    compute_drag,
    compute_cruise_cl,
    compute_cruise_cd,
    AerodynamicSurrogate
)

from .propulsion import (
    PropulsionSystem,
    SimplifiedPropulsion,
    get_default_propulsion
)

from .variability import (
    temperature_perturbation,
    wind_profile_logarithmic,
    wind_profile_linear,
    wind_profile_hale,
    TurbulenceModel
)

from .visualization import (
    plot_atmosphere,
    plot_solar,
    plot_aerodynamics,
    plot_power,
    plot_energy,
    plot_all,
    plot_summary_dashboard
)

__version__ = "1.0.0"
__author__ = "HALE UAV Research Project"

__all__ = [
    # Simulation
    "MissionSimulation",
    "AircraftConfig",
    "MissionConfig",
    "SimulationResults",
    "run_default_simulation",
    # Atmosphere
    "isa_properties",
    "AtmosphereProperties",
    "isa_with_offset",
    "custom_lapse_rate",
    # Solar
    "calculate_irradiance",
    "compute_solar_position",
    "altitude_correction",
    # Aerodynamics
    "compute_lift",
    "compute_drag",
    "compute_cruise_cl",
    "compute_cruise_cd",
    "AerodynamicSurrogate",
    # Propulsion
    "PropulsionSystem",
    "SimplifiedPropulsion",
    "get_default_propulsion",
    # Variability
    "temperature_perturbation",
    "wind_profile_logarithmic",
    "wind_profile_linear",
    "wind_profile_hale",
    "TurbulenceModel",
    # Visualization
    "plot_atmosphere",
    "plot_solar",
    "plot_aerodynamics",
    "plot_power",
    "plot_energy",
    "plot_all",
    "plot_summary_dashboard",
]