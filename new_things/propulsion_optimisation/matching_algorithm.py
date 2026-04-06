"""
matching_algorithm.py — Dantsker Motor-Propeller Matching Algorithm

Implements the coupled motor-propeller matching methodology from:
    Dantsker, O.D. et al. (2020). Propulsion system design and optimization
    for solar-powered UAVs. AIAA Propulsion and Energy Forum.

For each motor-propeller pair, the algorithm finds the operating point where
the motor provides exactly the torque required by the propeller to produce
the target thrust at the design cruise speed and altitude.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Optional, Tuple
from scipy.optimize import brentq

from propeller_database import Propeller
from motor_model import Motor, ESC


@dataclass
class DesignPoint:
    """Mission design point for propulsion optimisation."""
    thrust_required: float      # (N) Required cruise thrust
    cruise_speed: float         # (m/s) Freestream velocity
    air_density: float          # (kg/m³) At operating altitude
    battery_voltage: float      # (V) Supply voltage
    esc: ESC                    # ESC model

    @property
    def label(self) -> str:
        return (f"T={self.thrust_required:.1f}N, V={self.cruise_speed:.1f}m/s, "
                f"ρ={self.air_density:.4f}kg/m³, Vbat={self.battery_voltage:.0f}V")


@dataclass
class MatchResult:
    """Result of matching a single motor-propeller combination."""
    propeller: Propeller
    motor: Motor
    feasible: bool
    reason: str = ""

    # Operating point
    rpm: float = 0.0
    n_rps: float = 0.0         # revolutions per second
    advance_ratio: float = 0.0
    motor_current: float = 0.0
    motor_voltage: float = 0.0

    # Performance
    thrust: float = 0.0
    torque_prop: float = 0.0
    torque_motor: float = 0.0
    power_elec: float = 0.0     # W — total from battery
    power_shaft: float = 0.0    # W — mechanical
    power_thrust: float = 0.0   # W — useful thrust power

    # Efficiencies
    eta_prop: float = 0.0
    eta_motor: float = 0.0
    eta_esc: float = 0.0
    eta_system: float = 0.0

    @property
    def label(self) -> str:
        return f"{self.motor.name} + {self.propeller.label}"


def _propeller_thrust(prop: Propeller, n_rps: float, V: float,
                      rho: float) -> float:
    """Calculate thrust from propeller at given RPM and airspeed."""
    D = prop.diameter
    if n_rps <= 0:
        return 0.0
    J = V / (n_rps * D)
    CT = prop.CT(J)
    T = CT * rho * n_rps**2 * D**4
    return T


def _propeller_torque(prop: Propeller, n_rps: float, V: float,
                      rho: float) -> float:
    """Calculate torque required by propeller at given RPM and airspeed."""
    D = prop.diameter
    if n_rps <= 0:
        return 0.0
    J = V / (n_rps * D)
    CP = prop.CP(J)
    # P = CP * rho * n^3 * D^5, Q = P / (2*pi*n)
    Q = CP * rho * n_rps**2 * D**5 / (2.0 * np.pi)
    return Q


def match_motor_propeller(motor: Motor, prop: Propeller,
                          design: DesignPoint) -> MatchResult:
    """
    Find the operating point for a motor-propeller combination
    that produces the required thrust at the design cruise condition.

    The algorithm iterates RPM to find where:
        T(RPM) = T_required

    Then checks motor feasibility at that RPM.

    Parameters
    ----------
    motor : Motor
        Motor to evaluate
    prop : Propeller
        Propeller to evaluate
    design : DesignPoint
        Mission design conditions

    Returns
    -------
    MatchResult
        Full operating point and efficiency data
    """

    result = MatchResult(propeller=prop, motor=motor, feasible=False)

    V = design.cruise_speed
    rho = design.air_density
    T_req = design.thrust_required
    V_bat = design.battery_voltage
    D = prop.diameter

    # --- Step 1: Find RPM that produces required thrust ---
    # Thrust equation: T = CT(J) * rho * n^2 * D^4
    # where J = V / (n * D)
    # We need to solve: T(n) = T_req

    # Define search range for n (rev/s)
    J_max = prop.J_data[-1] if len(prop.J_data) > 0 else 0.8
    J_min = prop.J_data[0] if len(prop.J_data) > 0 else 0.05

    if J_max <= 0 or J_min <= 0:
        result.reason = "Invalid J range"
        return result

    # n_min from J_max (low RPM), n_max from J_min (high RPM)
    n_min = V / (J_max * D)
    n_max = V / (J_min * D)

    # Motor RPM ceiling: back-EMF = supply voltage
    motor_max_rpm = V_bat * motor.KV
    motor_max_n = motor_max_rpm / 60.0

    # Allow up to 95% of motor max RPM
    n_max = min(n_max, motor_max_n * 0.95)

    # Also set a sensible minimum n (avoid near-zero)
    n_min = max(n_min, 1.0)  # at least 1 rev/s = 60 RPM

    if n_min >= n_max:
        result.reason = (f"RPM range conflict: need {n_min*60:.0f}-{n_max*60:.0f} RPM, "
                         f"motor max {motor_max_rpm:.0f} RPM")
        return result

    # --- Step 2: Scan + root-find for T(n) = T_req ---
    def thrust_residual(n):
        return _propeller_thrust(prop, n, V, rho) - T_req

    try:
        # Scan across the RPM range to find where T crosses T_req
        n_scan = np.linspace(n_min, n_max, 500)
        T_scan = np.array([_propeller_thrust(prop, n, V, rho) for n in n_scan])

        # Find bracket where sign changes
        residuals = T_scan - T_req
        sign_changes = np.where(np.diff(np.sign(residuals)))[0]

        if len(sign_changes) == 0:
            T_max_achievable = np.max(T_scan)
            result.reason = (f"Cannot produce {T_req:.1f}N thrust "
                             f"(max achievable: {T_max_achievable:.1f}N at "
                             f"{n_scan[np.argmax(T_scan)]*60:.0f} RPM)")
            return result

        # Use the first bracket
        idx = sign_changes[0]
        n_lo, n_hi = n_scan[idx], n_scan[idx + 1]

        n_sol = brentq(thrust_residual, n_lo, n_hi, xtol=0.001,
                       maxiter=500)

    except (ValueError, RuntimeError) as e:
        result.reason = f"Solver failed: {str(e)[:60]}"
        return result

    # --- Step 3: Calculate operating point ---
    rpm_sol = n_sol * 60.0
    J_sol = V / (n_sol * D)

    # Propeller performance at operating point
    CT_sol = prop.CT(J_sol)
    CP_sol = prop.CP(J_sol)
    eta_prop = prop.eta(J_sol)

    T_sol = CT_sol * rho * n_sol**2 * D**4
    Q_prop = _propeller_torque(prop, n_sol, V, rho)

    # --- Step 4: Check motor feasibility ---
    motor_current = motor.current(V_bat, rpm_sol)
    motor_torque = motor.torque(V_bat, rpm_sol)

    if not motor.is_feasible(V_bat, rpm_sol):
        result.reason = "Motor outside operating limits"
        result.rpm = rpm_sol
        result.advance_ratio = J_sol
        return result

    # Check torque matching (motor must produce >= propeller torque)
    if motor_torque < Q_prop * 0.95:  # 5% tolerance
        result.reason = f"Insufficient torque ({motor_torque:.4f} < {Q_prop:.4f} N·m)"
        result.rpm = rpm_sol
        result.advance_ratio = J_sol
        return result

    # --- Step 5: Calculate efficiencies ---
    eta_motor = motor.efficiency(V_bat, rpm_sol)
    eta_esc = design.esc.efficiency

    eta_system = eta_prop * eta_motor * eta_esc
    if eta_system <= 0:
        result.reason = "Zero system efficiency"
        return result

    # Thrust power (useful output)
    P_thrust = T_sol * V

    # Electrical power from battery
    P_elec = P_thrust / eta_system if eta_system > 0 else float('inf')
    P_shaft = motor.power_out(V_bat, rpm_sol)

    # --- Step 6: Store results ---
    result.feasible = True
    result.reason = "OK"
    result.rpm = rpm_sol
    result.n_rps = n_sol
    result.advance_ratio = J_sol
    result.motor_current = motor_current
    result.motor_voltage = V_bat

    result.thrust = T_sol
    result.torque_prop = Q_prop
    result.torque_motor = motor_torque
    result.power_elec = P_elec
    result.power_shaft = P_shaft
    result.power_thrust = P_thrust

    result.eta_prop = eta_prop
    result.eta_motor = eta_motor
    result.eta_esc = eta_esc
    result.eta_system = eta_system

    return result


def run_parametric_sweep(motors: List[Motor], propellers: List[Propeller],
                         design: DesignPoint) -> List[MatchResult]:
    """
    Exhaustively evaluate all motor-propeller combinations.

    Parameters
    ----------
    motors : List[Motor]
        Motor candidates
    propellers : List[Propeller]
        Propeller candidates
    design : DesignPoint
        Mission design conditions

    Returns
    -------
    List[MatchResult]
        All results, sorted by electrical power (best first)
    """

    results = []
    total = len(motors) * len(propellers)
    feasible_count = 0

    print(f"\n{'='*70}")
    print(f"  DANTSKER PROPULSION OPTIMISATION — PARAMETRIC SWEEP")
    print(f"{'='*70}")
    print(f"  Design Point: {design.label}")
    print(f"  Motor candidates: {len(motors)}")
    print(f"  Propeller candidates: {len(propellers)}")
    print(f"  Total combinations: {total}")
    print(f"{'='*70}\n")

    for motor in motors:
        for prop in propellers:
            result = match_motor_propeller(motor, prop, design)
            results.append(result)
            if result.feasible:
                feasible_count += 1

    # Sort feasible results by electrical power (ascending = best first)
    feasible = [r for r in results if r.feasible]
    infeasible = [r for r in results if not r.feasible]

    feasible.sort(key=lambda r: r.power_elec)

    print(f"  Feasible combinations: {feasible_count} / {total} "
          f"({100*feasible_count/total:.0f}%)")

    # Show failure breakdown if many infeasible
    if infeasible:
        reasons = {}
        for r in infeasible:
            key = r.reason.split('(')[0].strip()  # Group by prefix
            reasons[key] = reasons.get(key, 0) + 1
        print(f"\n  Failure breakdown:")
        for reason, count in sorted(reasons.items(), key=lambda x: -x[1]):
            print(f"    - {reason}: {count}")

    if feasible:
        best = feasible[0]
        worst = feasible[-1]
        print(f"\n  BEST:  {best.label}")
        print(f"         η_sys = {best.eta_system*100:.1f}%, "
              f"P_elec = {best.power_elec:.0f} W")
        print(f"         RPM = {best.rpm:.0f}, J = {best.advance_ratio:.3f}")
        print(f"         η_prop = {best.eta_prop*100:.1f}%, "
              f"η_motor = {best.eta_motor*100:.1f}%")
        print(f"  WORST: {worst.label}")
        print(f"         η_sys = {worst.eta_system*100:.1f}%, "
              f"P_elec = {worst.power_elec:.0f} W")

        improvement = (1 - best.power_elec / worst.power_elec) * 100
        print(f"\n  Efficiency improvement (best vs worst): {improvement:.1f}%")

    return feasible + infeasible


# Quick test
if __name__ == "__main__":
    from propeller_database import load_database
    from motor_model import load_motor_database

    # HALE UAV design point at 20 km altitude
    design = DesignPoint(
        thrust_required=40.7,       # N (from W/(L/D) = 1118/27.5)
        cruise_speed=22.2,          # m/s (80 km/h)
        air_density=0.0889,         # kg/m³ at 20 km
        battery_voltage=96.0,       # V (high-voltage HALE bus)
        esc=ESC(efficiency=0.96),
    )

    motors = load_motor_database()
    props = load_database()

    results = run_parametric_sweep(motors, props, design)

    print(f"\n\n{'='*100}")
    print(f"  TOP 10 COMBINATIONS")
    print(f"{'='*100}")
    print(f"{'Rank':<5} {'Combination':<50} {'η_sys(%)':<10} {'P_elec(W)':<10} "
          f"{'RPM':<8} {'J':<8} {'η_prop':<8} {'η_motor':<8}")
    print(f"{'-'*100}")

    for i, r in enumerate(results[:10]):
        if r.feasible:
            print(f"{i+1:<5} {r.label:<50} {r.eta_system*100:<10.1f} "
                  f"{r.power_elec:<10.0f} {r.rpm:<8.0f} {r.advance_ratio:<8.3f} "
                  f"{r.eta_prop*100:<8.1f} {r.eta_motor*100:<8.1f}")
