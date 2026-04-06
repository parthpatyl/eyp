# Propulsion Optimisation: Dantsker Framework Applied to HALE UAV

## 1. Overview

This module implements a mission-based propulsion system optimisation tool following the
methodology established by Dantsker et al. (UIUC/TUM Solar Flyer, AIAA 2020) [42].

The fundamental insight of the Dantsker approach is that **motor and propeller must be
treated as a coupled system**, not independent components. A propeller that is individually
"efficient" may not be efficient when paired with a particular motor at the required
operating point. The tool exhaustively searches the motor–propeller design space to find
the combination that minimises electrical power consumption at the cruise design point.

**Published result**: Dantsker's tool achieved a **19% efficiency improvement** over the
baseline propulsion system on the UIUC-TUM Solar Flyer by matching motor torque–speed
characteristics to propeller loading.

## 2. Mathematical Formulation

### 2.1 Propeller Aerodynamic Coefficients

The UIUC propeller database uses standard non-dimensional coefficients:

- **Advance Ratio**: J = V∞ / (n × D)
  - V∞ = freestream velocity (m/s)
  - n = rotational speed (rev/s)
  - D = propeller diameter (m)

- **Thrust Coefficient**: CT = T / (ρ × n² × D⁴)

- **Power (Torque) Coefficient**: CP = P / (ρ × n³ × D⁵)

- **Propeller Efficiency**: η_prop = J × CT / CP

These coefficients are **non-dimensional** and remain valid across density changes,
making UIUC sea-level wind-tunnel data applicable to stratospheric conditions
when combined with the correct density in the dimensional equations.

### 2.2 DC Brushless Motor Model

The motor is modelled using standard steady-state equivalent circuit parameters:

- **KV**: motor velocity constant (RPM/V)
- **Kt**: motor torque constant = 60 / (2π × KV)  [N·m/A]
- **I₀**: no-load current (A) — represents friction and windage losses
- **Ra**: armature (winding) resistance (Ω)

At a given operating point:
- Back-EMF: V_bemf = RPM / KV
- Current: I = (V_supply - V_bemf) / Ra
- Motor torque: Q_motor = Kt × (I - I₀)
- Motor efficiency: η_motor = Q_motor × ω / (V_supply × I)
  where ω = 2π × RPM / 60

### 2.3 System Coupling

At equilibrium, the motor torque equals the propeller torque:

  Q_motor = Q_propeller = CP(J) × ρ × n² × D⁵ / (2π)

And the thrust produced equals:

  T = CT(J) × ρ × n² × D⁴

The total system efficiency is:

  η_sys = η_prop × η_motor × η_ESC

Leading to the electrical power required:

  P_elec = T × V∞ / η_sys

## 3. UIUC Propeller Database

The UIUC Propeller Data Site (University of Illinois at Urbana-Champaign) provides
wind-tunnel measurements for ~140 propellers across 4 volumes:

- **Volume 1** (Brandt, 2005–2008): Foundational measurements
- **Volume 2** (Deters, 2009–2015): Extended RPM and Reynolds effects
- **Volume 3** (Dantsker, 2020): Aero-Naut CAM folding propellers
- **Volume 4** (Dantsker, 2021–2022): APC Electric fixed-blade propellers

Data format (per RPM test): Columns of [J, CT, CP, η]

This module includes **15 representative propellers** with embedded coefficient data
spanning the diameter range relevant to solar UAV applications (8"–19").

**Citation**: J.B. Brandt, R.W. Deters, G.K. Ananda, O.D. Dantsker, and M.S. Selig,
UIUC Propeller Database, Vols 1–4, University of Illinois at Urbana-Champaign.

## 4. Matching Algorithm

For each motor–propeller combination at the design cruise point:

1. **Define design thrust** from weight and L/D ratio: T_req = W / (L/D)
2. **Iterate over RPM** to find the operating point where T(RPM, J) = T_req
3. **Calculate propeller torque** at that RPM from CP(J)
4. **Check motor feasibility**: Can the motor produce the required torque at
   this RPM within voltage and current limits?
5. **Compute efficiencies**: η_prop(J), η_motor(I, V), η_ESC
6. **Record system performance**: P_elec, η_sys, operating point details

The combination with the **lowest P_elec** (equivalently, highest η_sys) is optimal.

## 5. Altitude Correction

At 20 km altitude:
- Air density: ρ ≈ 0.0889 kg/m³ (vs 1.225 kg/m³ at sea level)
- Density ratio: σ = 0.0726

**Effect**: For the same thrust requirement, the propeller must spin faster
(approximately √(1/σ) ≈ 3.7× faster), or use a larger diameter. This shifts the
operating advance ratio J and changes the efficiency map.

The CT, CP coefficients themselves remain valid — they are non-dimensional.
Only the dimensional scaling (T = CT × ρ × n² × D⁴) uses the actual ρ.

## 6. Application to Present HALE UAV Design

**Design Point:**
- MTOW: ~114 kg → W = 1,118 N
- Cruise speed: 80 km/h (22.2 m/s)
- Altitude: 20 km → ρ = 0.0889 kg/m³
- Target L/D: 25–30
- Thrust required: T = 1,118 / 27.5 ≈ 40.7 N
- Battery bus: 48V (12S LiPo)
- ESC efficiency: 96%

**Expected outcome**: Selection of an optimal motor–propeller pair that reduces
cruise electrical power from baseline ~1,994 W to ~1,615 W (19% reduction),
directly reducing night-time energy storage requirements from 23.9 kWh to ~19.4 kWh.
