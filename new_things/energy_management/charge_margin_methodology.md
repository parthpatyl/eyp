# Energy Management Algorithm: Charge-Margin Methodology

## Overview
This document outlines the conceptual framework and mathematical foundation for the HALE UAV energy management algorithm, drawing heavily from the robust methodology established by Oettershagen's AtlantikSolar project. 

The primary goal of this algorithm is to ensure perpetual flight capability even in the presence of meteorological disturbances (e.g., cloud cover factor) by optimizing specific energetic safety margins.

## Central Performance Metrics

Two key metrics define the robustness of the solar-powered UAV's energy management:

1. **Excess Time ($T_{exc}$)**: The duration the UAV can maintain level flight exclusively on battery power during low/zero solar irradiance (e.g., night-time or heavy cloud cover). This metric represents the margin of safety against prolonged negative net energy balance.

2. **Charge Margin ($T_{cm}$)**: The buffer available during the recharging phase (daytime). A positive charge margin means the UAV is capable of reaching 100% State of Charge (SOC) before sunset, even if solar power income is disturbed (reduced) by a defined cloud cover factor.

## Mathematical Formulation

The energy state of the UAV is governed by the differential equation of the battery energy ($E_{bat}$):

$$ \frac{dE_{bat}}{dt} = P_{solar}(t, \eta, S, \theta) - P_{out}(v, W, \rho, C_D, C_L) $$

### Variables:
*   $E_{bat}(t)$: Battery energy at time $t$
*   $P_{solar}$: Solar power generated (function of time, system efficiency $\eta$, solar area $S$, and incident angle $\theta$)
*   $P_{out}$: Power consumed for propulsion and avionics (function of velocity $v$, weight $W$, air density $\rho$, drag $C_D$, and lift $C_L$ coefficients)

### The Algorithm Objective
The energy management algorithm will continuously monitor these states and adjust the flight profile, specifically:
*   **Altitude Management**: Trading potential energy with electrical energy (e.g., climbing during peak solar irradiance).
*   **Speed Optimization**: Adjusting cruise velocity to minimum power speed ($V_{mp}$) or maximum range speed ($V_{mr}$) depending on the current charge margin ($T_{cm}$).

## Next Implementation Steps

1. **Environmental Modeling**: Develop a script to simulate solar irradiance over a 24-hour cycle including cloud-cover disturbance parameters.
2. **Power System Modeling**: Implement functions to calculate $P_{solar}$ and $P_{out}$ based on the UAV's aerodynamic and electrical specifications.
3. **State Trajectory Simulation**: Write an integration loop (using Runge-Kutta or similar) to map $E_{bat}$ over time.
4. **Control Logic**: Implement the decision matrix that prioritizes survival (maintaining $T_{exc} > 0$) while maximizing $T_{cm}$.

Target Environment: Python (using `numpy` and `scipy.integrate.solve_ivp`) or MATLAB/Simulink.
