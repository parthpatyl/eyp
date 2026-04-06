"""
motor_model.py — Parametric DC Brushless Motor Model for HALE UAV

Models brushless DC motors using the standard equivalent circuit approach:
KV (RPM/V), I0 (no-load current), Ra (armature resistance).

Motors are sized for HALE applications with high-voltage bus (96V)
and low RPM requirements (500–4000 RPM for large propellers).
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Motor:
    """A brushless DC motor with equivalent circuit parameters."""
    name: str
    KV: float           # RPM per Volt
    I0: float           # No-load current (A)
    Ra: float           # Armature resistance (Ohm)
    I_max: float        # Maximum continuous current (A)
    mass_g: float       # Motor mass (grams)

    @property
    def Kt(self) -> float:
        """Torque constant (N·m/A) = 60 / (2π × KV)"""
        return 60.0 / (2.0 * np.pi * self.KV)

    @property
    def mass_kg(self) -> float:
        return self.mass_g / 1000.0

    def back_emf(self, rpm: float) -> float:
        """Back-EMF voltage at given RPM."""
        return rpm / self.KV

    def current(self, V_supply: float, rpm: float) -> float:
        """Motor current at given supply voltage and RPM."""
        V_bemf = self.back_emf(rpm)
        if V_supply <= V_bemf:
            return self.I0
        I = (V_supply - V_bemf) / self.Ra
        return max(I, self.I0)

    def torque(self, V_supply: float, rpm: float) -> float:
        """Shaft torque (N·m) at given operating point."""
        I = self.current(V_supply, rpm)
        Q = self.Kt * (I - self.I0)
        return max(Q, 0.0)

    def power_in(self, V_supply: float, rpm: float) -> float:
        """Electrical power input (W)."""
        I = self.current(V_supply, rpm)
        return V_supply * I

    def power_out(self, V_supply: float, rpm: float) -> float:
        """Mechanical shaft power output (W)."""
        Q = self.torque(V_supply, rpm)
        omega = 2.0 * np.pi * rpm / 60.0
        return Q * omega

    def efficiency(self, V_supply: float, rpm: float) -> float:
        """Motor efficiency at given operating point."""
        P_in = self.power_in(V_supply, rpm)
        P_out = self.power_out(V_supply, rpm)
        if P_in <= 0:
            return 0.0
        eta = P_out / P_in
        return np.clip(eta, 0.0, 0.99)

    def is_feasible(self, V_supply: float, rpm: float) -> bool:
        """Check if operating point is within motor limits."""
        V_bemf = self.back_emf(rpm)
        I = self.current(V_supply, rpm)
        if V_bemf > V_supply * 1.05:  # 5% margin
            return False
        if I > self.I_max:
            return False
        if I < self.I0:
            return False
        return True

    @property
    def label(self) -> str:
        return f"{self.name} (KV={self.KV:.0f})"


@dataclass
class ESC:
    """Electronic Speed Controller model (simple efficiency factor)."""
    efficiency: float = 0.96    # Typical 96% for quality ESCs
    name: str = "Generic ESC"

    def power_out(self, power_in: float) -> float:
        return power_in * self.efficiency


def load_motor_database() -> List[Motor]:
    """
    Returns motors suitable for HALE UAV propulsion.

    For HALE at 20 km altitude with large propellers (1–2.5 m),
    typical RPM range is 500–4000 RPM. With a 96V bus:
    - KV=20 → max 1,920 RPM
    - KV=50 → max 4,800 RPM
    - KV=80 → max 7,680 RPM

    Motor parameters chosen so that at typical operating point
    (70-90% of max RPM), motor efficiency is 80-92%. Ra values
    follow the scaling: Ra ≈ V_bus / (3 × I_max) to ensure
    reasonable efficiency at operating current (~10-25A for 2kW class).
    """

    motors = [
        # Ultra-low KV — very large props, very slow turning
        Motor(
            name="HALE-Direct D80",
            KV=20,
            I0=0.3,
            Ra=1.20,
            I_max=30,
            mass_g=1200,
        ),
        Motor(
            name="HALE-Direct D60",
            KV=28,
            I0=0.3,
            Ra=0.90,
            I_max=35,
            mass_g=980,
        ),

        # Low KV — standard HALE range
        Motor(
            name="T-Motor U15 XXL",
            KV=38,
            I0=0.4,
            Ra=0.70,
            I_max=40,
            mass_g=850,
        ),
        Motor(
            name="T-Motor U13 HALE",
            KV=48,
            I0=0.4,
            Ra=0.55,
            I_max=45,
            mass_g=680,
        ),

        # Medium KV — versatile
        Motor(
            name="Scorpion HALE-4030",
            KV=60,
            I0=0.5,
            Ra=0.45,
            I_max=50,
            mass_g=520,
        ),
        Motor(
            name="T-Motor AT5220",
            KV=75,
            I0=0.5,
            Ra=0.35,
            I_max=45,
            mass_g=420,
        ),

        # Higher KV — smaller HALE props or multi-motor setups
        Motor(
            name="Hacker Solar Q80",
            KV=95,
            I0=0.6,
            Ra=0.28,
            I_max=40,
            mass_g=350,
        ),
        Motor(
            name="T-Motor MN7010",
            KV=120,
            I0=0.6,
            Ra=0.22,
            I_max=35,
            mass_g=280,
        ),
    ]

    return motors


# Quick test
if __name__ == "__main__":
    motors = load_motor_database()
    esc = ESC()

    V_bus = 96.0  # HALE bus voltage

    print(f"HALE Motor Database ({len(motors)} motors):")
    print(f"Bus voltage: {V_bus:.0f} V\n")
    print(f"{'#':<3} {'Name':<22} {'KV':<6} {'Kt(Nm/A)':<10} {'I0(A)':<7} "
          f"{'Ra(Ω)':<8} {'Imax(A)':<8} {'Mass(g)':<8} {'MaxRPM':<8}")
    print("-" * 95)
    for i, m in enumerate(motors):
        max_rpm = m.KV * V_bus
        print(f"{i+1:<3} {m.name:<22} {m.KV:<6.0f} {m.Kt:<10.4f} {m.I0:<7.1f} "
              f"{m.Ra:<8.3f} {m.I_max:<8.0f} {m.mass_g:<8.0f} {max_rpm:<8.0f}")

    # Sample operating point
    print(f"\n--- Sample Operating Point ---")
    m = motors[3]  # T-Motor U13 HALE (KV=48)
    rpm = 2500
    print(f"Motor: {m.label}")
    print(f"Voltage: {V_bus:.0f} V, RPM: {rpm}")
    print(f"Back-EMF: {m.back_emf(rpm):.1f} V")
    print(f"Current: {m.current(V_bus, rpm):.2f} A")
    print(f"Torque: {m.torque(V_bus, rpm):.4f} N·m")
    print(f"Power In: {m.power_in(V_bus, rpm):.1f} W")
    print(f"Power Out: {m.power_out(V_bus, rpm):.1f} W")
    print(f"Efficiency: {m.efficiency(V_bus, rpm)*100:.1f}%")
    print(f"Feasible: {m.is_feasible(V_bus, rpm)}")
