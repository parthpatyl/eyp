"""
propulsion.py — Propulsion System Integration

Combines motor and propeller models for power required and thrust available.
Integrates with existing motor_model.py and propeller_database.py.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional, List, Tuple
import sys
from pathlib import Path

# Import existing propulsion modules
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "propulsion_optimisation"))
    from motor_model import Motor, ESC, load_motor_database
    from propeller_database import Propeller, load_database
    PROPULSION_MODELS_AVAILABLE = True
except ImportError:
    PROPULSION_MODELS_AVAILABLE = False
    print("Warning: Could not import propulsion models, using simplified approach")


@dataclass
class PropulsionPerformance:
    """Container for propulsion system performance."""
    power_required_w: float
    power_available_w: float
    thrust_available_n: float
    rpm: float
    motor_efficiency: float
    propeller_efficiency: float
    overall_efficiency: float


def compute_power_coefficient(
    thrust_n: float,
    density: float,
    diameter_m: float,
    velocity_ms: float
) -> float:
    """
    Compute power coefficient from thrust.

    CT = T / (ρ * n² * D⁴)
    CP = P / (ρ * n³ * D⁵)
    -> Compute n from thrust, then CP

    Parameters:
        thrust_n: Thrust in Newtons
        density: Air density (kg/m³)
        diameter_m: Propeller diameter (m)
        velocity_ms: Forward velocity (m/s)

    Returns:
        Power coefficient
    """
    # Advance ratio
    J = velocity_ms / (1.0 * diameter_m) if diameter_m > 0 else 0
    return 0.05 * (1.0 + J * 0.5)  # Simplified


def estimate_rpm_from_thrust(
    thrust_n: float,
    density: float,
    diameter_m: float,
    CT_max: float = 0.12
) -> float:
    """
    Estimate RPM required to produce given thrust.

    CT = T / (ρ * n² * D⁴)
    n = sqrt(T / (CT * ρ * D⁴))

    Parameters:
        thrust_n: Required thrust (N)
        density: Air density (kg/m³)
        diameter_m: Propeller diameter (m)
        CT_max: Maximum thrust coefficient

    Returns:
        RPM
    """
    if thrust_n <= 0 or density <= 0 or diameter_m <= 0:
        return 0.0

    n_squared = thrust_n / (CT_max * density * diameter_m ** 4)
    n_rps = np.sqrt(n_squared)
    return n_rps * 60.0  # Convert to RPM


def simple_power_required(
    drag_n: float,
    velocity_ms: float,
    motor_efficiency: float = 0.85,
    propeller_efficiency: float = 0.75
) -> Tuple[float, float]:
    """
    Simplified power required calculation.

    Parameters:
        drag_n: Drag force (N)
        velocity_ms: Velocity (m/s)
        motor_efficiency: Motor efficiency
        propeller_efficiency: Propeller efficiency

    Returns:
        (power_electrical_w, power_mechanical_w)
    """
    power_mechanical = drag_n * velocity_ms
    overall_eff = motor_efficiency * propeller_efficiency
    power_electrical = power_mechanical / overall_eff if overall_eff > 0 else 0

    return power_electrical, power_mechanical


class PropulsionSystem:
    """
    Complete propulsion system: Motor + ESC + Propeller.

    This class integrates the existing motor and propeller models
    to compute power required and available thrust.
    """

    def __init__(
        self,
        motor: Optional[Motor] = None,
        propeller: Optional[Propeller] = None,
        esc: Optional[ESC] = None,
        bus_voltage: float = 96.0,
        n_motors: int = 1
    ):
        """
        Initialize propulsion system.

        Parameters:
            motor: Motor object (from motor_model.py)
            propeller: Propeller object (from propeller_database.py)
            esc: ESC object
            bus_voltage: Battery bus voltage (V)
            n_motors: Number of motors
        """
        self.motor = motor
        self.propeller = propeller
        self.esc = esc if esc else ESC()
        self.bus_voltage = bus_voltage
        self.n_motors = n_motors

    def power_required(
        self,
        drag_n: float,
        velocity_ms: float,
        density: float
    ) -> PropulsionPerformance:
        """
        Compute power required for given drag and velocity.

        Parameters:
            drag_n: Total drag (N)
            velocity_ms: True air speed (m/s)
            density: Air density (kg/m³)

        Returns:
            PropulsionPerformance object
        """
        # Mechanical power needed
        P_mech = drag_n * velocity_ms

        # Estimate propeller efficiency at this condition
        if self.propeller and velocity_ms > 0:
            # Compute advance ratio
            J = velocity_ms / (self.propeller.diameter * 1000)  # Approximate
            prop_eff = self.propeller.eta(np.clip(J, 0.1, 0.9))
        else:
            prop_eff = 0.75  # Default

        # Motor efficiency (estimate based on load)
        if self.motor and velocity_ms > 0:
            # Estimate RPM from advance ratio
            if self.propeller:
                J = velocity_ms / self.propeller.diameter
                n_rps = velocity_ms / (J * self.propeller.diameter)
                rpm_estimate = n_rps * 60.0
            else:
                rpm_estimate = 1500.0

            motor_eff = self.motor.efficiency(self.bus_voltage, rpm_estimate)
        else:
            motor_eff = 0.85

        # Overall efficiency
        overall_eff = motor_eff * prop_eff * self.esc.efficiency

        # Electrical power required
        P_elec = P_mech / overall_eff if overall_eff > 0 else 0

        return PropulsionPerformance(
            power_required_w=P_elec,
            power_available_w=P_elec,  # Same for required calculation
            thrust_available_n=drag_n,
            rpm=rpm_estimate if self.motor else 1500.0,
            motor_efficiency=motor_eff,
            propeller_efficiency=prop_eff,
            overall_efficiency=overall_eff
        )

    def thrust_available(
        self,
        velocity_ms: float,
        density: float,
        rpm: Optional[float] = None,
        throttle: float = 1.0
    ) -> Tuple[float, float]:
        """
        Compute available thrust at given velocity.

        Parameters:
            velocity_ms: Forward velocity (m/s)
            density: Air density (kg/m³)
            rpm: Motor RPM (if None, compute from throttle)
            throttle: Throttle fraction (0-1)

        Returns:
            (thrust_N, power_W)
        """
        if rpm is None:
            rpm = self.motor.KV * self.bus_voltage * throttle if self.motor else 1500.0

        # Compute advance ratio
        if self.propeller:
            J = velocity_ms / (self.propeller.diameter * 1000)  # Approximate
            J = np.clip(J, 0.05, 1.0)

            CT = self.propeller.CT(J)
            n_rps = rpm / 60.0
            thrust = CT * density * n_rps ** 2 * self.propeller.diameter ** 4

            # Power required
            CP = self.propeller.CP(J)
            P_mech = CP * density * n_rps ** 3 * self.propeller.diameter ** 5

            # Electrical power
            motor_eff = self.motor.efficiency(self.bus_voltage, rpm) if self.motor else 0.85
            P_elec = P_mech / (motor_eff * self.esc.efficiency)

        else:
            # Simplified thrust model
            thrust = 50.0 * throttle * (density / 1.225)  # Scaled thrust
            P_elec = 500.0 * throttle

        return thrust * self.n_motors, P_elec


# =============================================================================
# Simplified Propulsion Model (when existing modules unavailable)
# =============================================================================

class SimplifiedPropulsion:
    """
    Simplified propulsion model for when motor/propeller databases unavailable.

    Uses empirical relations for HALE UAV class vehicles.
    """

    def __init__(
        self,
        propeller_diameter_m: float = 1.5,
        motor_efficiency: float = 0.85,
        prop_efficiency: float = 0.75
    ):
        """
        Initialize simplified propulsion.

        Parameters:
            propeller_diameter_m: Propeller diameter (m)
            motor_efficiency: Motor efficiency
            prop_efficiency: Propeller efficiency
        """
        self.diameter = propeller_diameter_m
        self.motor_eff = motor_efficiency
        self.prop_eff = prop_efficiency

    def power_required(
        self,
        drag_n: float,
        velocity_ms: float
    ) -> float:
        """
        Compute electrical power required.

        P_elec = D * V / (η_motor * η_prop)
        """
        P_mech = drag_n * velocity_ms
        return P_mech / (self.motor_eff * self.prop_eff)

    def thrust_available(
        self,
        velocity_ms: float,
        density: float,
        power_w: float,
        max_thrust_factor: float = 1.5
    ) -> float:
        """
        Compute available thrust.

        Uses momentum theory: T = sqrt(P * η * ρ * A) with corrections.
        """
        A = np.pi * self.diameter ** 2 / 4.0
        # Actuator disk theory
        T = np.sqrt(power_w * self.motor_eff * self.prop_eff * density * A)
        return T * max_thrust_factor


def get_default_propulsion() -> SimplifiedPropulsion:
    """Get default propulsion system for HALE UAV."""
    return SimplifiedPropulsion(
        propeller_diameter_m=1.5,
        motor_efficiency=0.85,
        prop_efficiency=0.75
    )


# Test function
if __name__ == "__main__":
    print("=== Propulsion System Test ===\n")

    from aerodynamics import compute_power_required

    # Test parameters
    mass = 25.0  # kg
    wing_area = 10.0  # m²
    velocity = 25.0  # m/s
    altitude = 20000  # m

    from atmosphere import isa_properties
    props = isa_properties(altitude)
    rho = props.density_kgm3

    # Drag calculation
    P_req = compute_power_required(mass, rho, velocity, wing_area)
    print(f"Power required at cruise: {P_req:.1f} W")

    # Use simplified propulsion
    prop = get_default_propulsion()
    P_elec = prop.power_required(P_req / velocity, velocity)
    print(f"Electrical power required: {P_elec:.1f} W")

    # Thrust available
    max_power = 2000.0  # W available
    T_avail = prop.thrust_available(velocity, rho, max_power)
    print(f"Available thrust at {max_power}W: {T_avail:.1f} N")