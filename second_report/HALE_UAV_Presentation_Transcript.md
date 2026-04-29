# HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES (UAVs): Sustainable Flight Through Integrated Solar, Propulsion and Atmospheric Simulation

**Academic Presentation Transcript**

---

## Slide 1: Title Slide

**Title:** HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES (UAVs): Sustainable Flight Through Integrated Solar, Propulsion and Atmospheric Simulation

**Subtitle:** End Year Project Report | Bachelor of Technology in Aerospace Engineering

**Presenter:** Parth Patil (22BTRAS031)

**Guide:** Dr Amalesh Barai, Professor, Department of Aerospace Engineering, JAIN (Deemed-to-be University)

**Academic Year:** 2025–2026

**Visuals:** [Department logo placeholder]

---

## Slide 2: Introduction

**Title:** Introduction to HALE UAVs

**Content:**
- HALE UAVs operate at altitudes above 18 km with mission durations from days to weeks
- Serve persistent surveillance, atmospheric research, and LEO communication relay roles
- Advanced platforms: NASA Helios, Airbus Zephyr S, QinetiQ Zephyr S achieved 24+ hours endurance
- Zephyr S achieved 64-day continuous flight (2022 world record)

**Speaker Notes:**
HALE UAVs represent a unique intersection of aerospace engineering challenges—extreme aspect ratio wings, ultra-lightweight structures, and renewable energy integration. Unlike conventional aircraft or satellites, these platforms must sustain flight for days or weeks at altitudes exceeding 18 kilometers, where air density is roughly one-tenth of sea-level conditions. This places them in a regime where traditional aircraft design methodologies require significant adaptation.

---

## Slide 3: Problem Statement

**Title:** The Core Engineering Challenge

**Content:**
- **Energy Balance:** Solar energy collected during daylight must satisfy total propulsion and payload power demand over complete diurnal cycle
- **Night-Time Storage Bottleneck:** ~24 kWh required for 12-hour night at ~2 kW average power
  - Battery solution: ~95 kg (at 250 Wh/kg) — exceeds feasible empty weight
  - Hydrogen fuel cell: ~4.3 kg system — dramatic reduction
- **Stratospheric Conditions:** Air density 0.088 kg/m³ at 20 km altitude
- **Required L/D:** 25–30 for practical endurance

**Speaker Notes:**
The fundamental constraint in HALE UAV design is energy. At stratospheric altitudes, the thin atmosphere demands extremely high lift coefficients from large wings, while simultaneously reducing the effectiveness of propulsion systems. The critical challenge emerges at night: without solar input, the aircraft must sustain flight from stored energy. Our analysis shows that a pure battery solution would require approximately 95 kilograms of lithium-ion cells—simply too heavy for a practical platform. Hydrogen fuel cells emerge as the viable alternative, reducing storage mass to under 5 kilograms while maintaining equivalent energy capacity.

---

## Slide 4: Research Objectives

**Title:** Project Objectives and Scope

**Content:**
- **Primary Objective:** Develop computational modelling framework integrating:
  1. Solar irradiance prediction with cloud cover dynamics
  2. Propulsion system optimisation via mission-based selection
  3. Atmospheric simulation for energy balance validation

- **Secondary Objectives:**
  - Energy balance evaluation (battery vs. fuel cell)
  - 24-hour mission-level simulation
  - Literature synthesis of state-of-the-art methodologies

**Speaker Notes:**
This project addresses the HALE design challenge through implemented computational models rather than purely theoretical analysis. Our three primary subsystems—solar irradiance modelling, propulsion optimisation, and atmospheric simulation—work together to evaluate energy balance and mission feasibility. Each component was validated against established benchmarks before integration, ensuring reliable predictions for conceptual design decisions.

---

## Slide 5: Literature Review — Configuration and Structural Studies

**Title:** Literature Survey: Platform Configurations

**Content:**
- **Configuration Studies:** High-AR monoplane configurations dominate (17.4 to 30+ aspect ratio)
- **Key Platforms:**
  - Zephyr S: 53 kg, 25 m span, 24+ days endurance
  - NASA Helios: 730 kg, 75 m span, AR 30.9
  - KARI EAV-3: 53 kg, 19.5 m span, AR 17.4
- **Structural Materials:** CFRP composites provide necessary stiffness-to-weight ratios
- **Aeroelasticity:** Flutter analysis critical for high-AR flexible wings

**Visuals:** [Comparison table of HALE platforms]

**Speaker Notes:**
Our literature survey revealed consistent trends across successful HALE platforms. High-aspect-ratio wings are universal, ranging from 17.4 in the EAV-3 to exceeding 30 in Helios-class vehicles. Carbon fiber reinforced polymer composites are the dominant structural material, providing the stiffness-to-weight ratios necessary to prevent aeroelastic coupling at extreme wing spans. The joined-wing configuration offers 1.4-1.5 span efficiency improvements, though structural complexity increases design challenges.

---

## Slide 6: Literature Review — Energy Systems

**Title:** Literature Survey: Energy Storage Technologies

**Content:**
- **Solar Cell Technologies:**
  - Triple-junction GaAs: 25–30% efficiency (current standard)
  - Perovskite (2024): 44,000 W/kg specific power, 20.1% efficiency
- **Energy Storage Thresholds:**
  - Fuel cells outperform batteries above 2.8 kWh demand
  - Lithium-sulfur: 300–350 Wh/kg (next generation)
- **Recent Milestones:**
  - PHASA-35: 66,000 ft stratospheric flight (December 2024)
  - AtlantikSolar: 81-hour continuous flight (world record <50 kg)

**Speaker Notes:**
Energy system technology has advanced significantly. While triple-junction gallium arsenide cells at 25-30% efficiency remain the practical standard, emerging perovskite technology promises transformative improvements—achieving 44,000 watts per kilogram, roughly 100 times better than conventional silicon. The decision between batteries and fuel cells follows a clear threshold: above 2.8 kilowatt-hours of night-time demand, fuel cells become mass-advantageous. This explains why the longest-endurance platforms all employ hybrid architectures.

---

## Slide 7: Methodology Overview

**Title:** Computational Methodology

**Content:**
- **Implemented Subsystems:**
  1. **Solar Irradiance Model:** 24-hour continuous simulation with cloud cover parameter k_c (0.0–1.0)
  2. **Propulsion Optimisation:** Mission-based motor-propeller selection using Dantsker methodology
  3. **Atmospheric Simulation:** ISA implementation with mission profile integration

- **Integration Pipeline:**
  ```
  Atmosphere → Solar Irradiance → Aerodynamics → Propulsion → Energy Balance
  ```

**Visuals:** [Methodology flowchart]

**Speaker Notes:**
Our methodology centers on implemented computational models rather than hand calculations. The solar irradiance model provides continuous 24-hour power prediction with dynamic cloud cover—essential for mission planning in variable meteorological conditions. Propulsion optimisation applies mission-based motor-propeller selection, systematically evaluating combinations to maximize system efficiency. The atmospheric simulation integrates these with ISA atmospheric properties to validate energy balance closure. Each module can be tested independently, enabling rapid iteration during conceptual design.

---

## Slide 8: Solar Irradiance Model

**Title:** Solar Irradiance Modelling

**Content:**
- **Model Parameters:**
  - Solar constant: S₀ = 1361 W/m²
  - Atmospheric transmittance: ρ_at = 0.7
  - Cloud cover parameter: k_c = 0.0–1.0

- **Validation Scenarios:**
  - Ideal clear sky (k_c = 0.0): Maximum power, no obstruction
  - Uniform disturbance (k_c = 0.3): Constant hazy conditions
  - Dynamic afternoon (k_c = 0.0→0.8): Clear morning, storm passage 14:00–19:00

- **Output:** Power state P_solar for energy balance: dE_bat/dt = P_solar − P_out

**Visuals:** [solar_irradiance_model.png]

**Speaker Notes:**
The solar irradiance model accounts for diurnal variations, seasonal changes through day-of-year parameter, and geographic location through latitude. The cloud cover parameter k_c directly modifies the power available from solar cells, enabling meteorological risk assessment for mission planning. Three validation scenarios demonstrate capability across weather conditions—from ideal clear-sky maximum power to dynamic afternoon storms. This parameterization allows mission planners to assess performance robustness across expected operating conditions.

---

## Slide 9: Propulsion Optimisation Results

**Title:** Propulsion System Optimisation

**Content:**
- **Mission-Based Selection Results:**
  | Metric | Baseline | Optimised | Improvement |
  |--------|----------|-----------|-------------|
  | Electrical Power (W) | 1994 | 1543 | 22.6% reduction |
  | System Efficiency (%) | — | 58.6 | — |
  | Propeller Efficiency (%) | — | 79.5 | — |
  | Motor Efficiency (%) | — | 76.7 | — |

- **Optimal Configuration:** HALE-Direct D80 motor + HALE-M 72×40 propeller at 1499 RPM
- **Night Storage Impact:** 5.4 kWh (21.2%) reduction, saving 21.6 kg battery mass

**Visuals:** [propulsion_optimisation_results.png]

**Speaker Notes:**
Propulsion optimisation using mission-based motor-propeller selection achieved a 22.6% reduction in cruise power—from 1994 watts to 1543 watts. This improvement directly impacts night-time energy storage requirements: the 5.4 kilowatt-hour reduction translates to 21.6 kilograms of battery mass saved. The optimal configuration combines the HALE-Direct D80 motor with a HALE-M 72x40 propeller operating at 1499 RPM, achieving 58.6% overall system efficiency. This demonstrates the significant payoff from system-level rather than component-level optimisation.

---

## Slide 10: Top Motor-Propeller Combinations

**Title:** Propulsion Optimisation — Top 10 Results

**Content:**
| Rank | Motor | Propeller | η_sys (%) | P_elec (W) | RPM |
|------|-------|-----------|-----------|------------|-----|
| 1 | HALE-Direct D80 | HALE-M 72x40 | 58.6 | 1543 | 1499 |
| 2 | HALE-Direct D60 | HALE-ST 60x27 | 56.3 | 1606 | 2039 |
| 3 | HALE-Direct D80 | HALE-HP 72x54 | 56.1 | 1611 | 1346 |
| 4 | T-Motor U15 XXL | HALE-ST 48x22 | 54.4 | 1663 | 2993 |
| 5 | T-Motor U13 HALE | HALE-ST 40x18 | 53.4 | 1691 | 4144 |

- **Analysis:** 86 combinations infeasible due to motor limits or insufficient thrust

**Speaker Notes:**
The systematic evaluation of motor-propeller combinations identified the top performers. The HALE-Direct D80 paired with the HALE-M 72x40 propeller emerges as optimal, achieving the highest system efficiency of 58.6%. Interestingly, the top five configurations all involve HALE-Direct motors, suggesting this motor line is well-suited for high-altitude applications. Notably, 86 of the 91 combinations evaluated were infeasible—either exceeding motor operating limits or providing insufficient thrust for the mission profile. This underscores the importance of system-level optimisation rather than selecting components in isolation.

---

## Slide 11: Atmospheric Simulation — ISA Validation

**Title:** Atmospheric Simulation: ISA Model Validation

**Content:**
- **ISA Model Implementation:** ICAO Standard Atmosphere (Doc 7488, 1993)

| Altitude (m) | Temperature (K) | Pressure (kPa) | Density (kg/m³) |
|--------------|-----------------|----------------|-----------------|
| 0            | 288.15          | 101.33         | 1.2250          |
| 10,000       | 223.15          | 26.44          | 0.4127          |
| 20,000       | 216.65          | 5.47           | 0.0880          |
| 25,000       | 221.65          | 2.51           | 0.0395          |

✓ Matches standard ISA tables within expected tolerance

**Visuals:** [atmosphere.png]

**Speaker Notes:**
The atmospheric simulation implements the ICAO Standard Atmosphere model, validated against published tables. At 20 kilometers—the design cruise altitude—air density is 0.088 kilograms per cubic meter, roughly one-tenth sea-level density. This extremely thin atmosphere is the primary driver for the high aspect ratio wings and low cruise speeds characteristic of HALE platforms. The ISA model provides the foundation for accurate power required calculations and energy balance assessment.

---

## Slide 12: Mission Simulation Results

**Title:** 24-Hour Mission Simulation Results

**Content:**
| Metric | Value |
|--------|-------|
| Mission Duration | 24.0 hours |
| Cruise Altitude | 20 km |
| Cruise Speed | 25 m/s |
| Average Temperature | 216.6 K |
| Average Density | 0.08803 kg/m³ |
| Daylight Hours | 14.4 hours |
| Total Solar Energy | 41,297 Wh |
| Avg Power Required | 558.5 W |
| Peak Power Generated | 5,039.0 W |
| **Energy Margin** | **208.1%** |

**Visuals:** [hale_simulation_dashboard.png]

**Speaker Notes:**
The full mission simulation at 20 kilometers altitude validates our integrated framework. Results show 208.1% energy margin—meaning solar collection exceeds consumption by more than double, confirming perpetual endurance capability. The 14.4 hours of daylight at the design latitude generates over 41,000 watt-hours of solar energy, while average power required is only 558.5 watts. This substantial surplus provides robust margins against degradation, unexpected conditions, and payload growth—a critical consideration for operational systems requiring multi-day endurance.

---

## Slide 13: Energy Balance Analysis

**Title:** Energy Balance and Storage Analysis

**Content:**
- **Night-Time Requirement:** ~23.9 kWh (12-hour dark period)
- **Storage Comparison:**
  | Technology | Energy Density | Required Mass | Feasibility |
  |------------|----------------|---------------|-------------|
  | Lithium-Ion | 250 Wh/kg | ~95.7 kg | ❌ Infeasible |
  | Hydrogen FC | 150–250 Wh/kg (system) | ~4.3 kg | ✓ Viable |

- **Key Insight:** Fuel cells outperform batteries above 2.8 kWh demand [10]

**Visuals:** [energy.png]

**Speaker Notes:**
The night-time storage requirement drives the fundamental design decision between battery and fuel cell architectures. At 23.9 kilowatt-hours for a typical 12-hour night, lithium-ion batteries require nearly 96 kilograms of cells—exceeding the entire empty weight budget of most HALE platforms. Hydrogen fuel cells, by contrast, require only 1.44 kilograms of hydrogen gas, plus approximately 3 kilograms for tankage and balance-of-plant—totaling under 5 kilograms. This dramatic mass difference explains why all longest-endurance platforms employ hybrid architectures combining solar, batteries, and fuel cells.

---

## Slide 14: Aerodynamic Performance

**Title:** Aerodynamic Performance Assessment

**Content:**
- **Simulation Results at 20 km Cruise:**
  | Parameter | Value |
  |-----------|-------|
  | Aircraft mass | 25.0 kg |
  | Wing area | 10.0 m² |
  | Required C_L | 0.891 |
  | Drag coefficient | 0.0518 |
  | Lift | 245.2 N |
  | Drag | 14.2 N |
  | **L/D ratio** | **17.2** |

- **Validation:** Lift balances weight for steady cruise ✓

**Visuals:** [aerodynamics.png]

**Speaker Notes:**
The atmospheric simulation computed aerodynamic forces at the design cruise condition. At 20 kilometers altitude, the aircraft requires a lift coefficient of 0.891 to maintain steady level flight—the drag coefficient of 0.0518 results in 14.2 newtons of drag at 25 meters per second cruise speed. The resulting lift-to-drag ratio of 17.2 is consistent with literature benchmarks for high aspect ratio HALE wings. This aerodynamic validation confirms the feasibility of steady cruise at the design altitude and speed.

---

## Slide 15: Power Balance Visualization

**Title:** Power Balance Throughout Mission

**Content:**
- **Power Flow:** Solar Array → MPPT → Battery Bus → Motor Controllers + Avionics
- **Key Metrics:**
  - Peak Power Generated: 5,039 W (solar noon)
  - Average Power Required: 558.5 W
  - Average Power Generated: 2,864.2 W
  - System efficiency chain: 58.6% (prop: 79.5%, motor: 76.7%, ESC: 96.0%)

**Visuals:** [power.png]

**Speaker Notes:**
The power balance visualization shows the diurnal variation in available solar power versus propulsion demand. Peak generation exceeds 5,000 watts at solar noon, dropping to zero overnight. Average power required of 558.5 watts is less than one-tenth the peak solar available, explaining the substantial energy margin. The system efficiency chain—from motor to propeller to electrical conversion—determines how effectively collected solar energy translates to useful thrust. The 58.6% overall efficiency achieved through optimisation represents meaningful improvement over baseline configurations.

---

## Slide 16: Summary Dashboard

**Title:** Integrated Simulation Dashboard

**Content:**
- **Six-Panel Dashboard:**
  1. Atmospheric properties (T, P, ρ vs time)
  2. Solar conditions (irradiance, power)
  3. Aerodynamic forces (lift, drag, CL, CD)
  4. Power balance (required vs generated)
  5. Energy balance (cumulative)
  6. Summary metrics

**Visuals:** [hale_simulation_dashboard.png]

**Speaker Notes:**
This comprehensive dashboard integrates all simulation outputs into a single view for mission analysis. The six panels show atmospheric properties varying with altitude, solar irradiance tracking the diurnal cycle, aerodynamic forces at cruise, power required versus generated, cumulative energy balance, and summary metrics. The positive energy slope throughout daylight hours and minimal overnight discharge confirms perpetual endurance capability for the design configuration.

---

## Slide 17: Key Computational Achievements

**Title:** Summary of Computational Results

**Content:**
| Subsystem | Key Metric | Value |
|-----------|------------|-------|
| Propulsion Optimisation | Cruise Power Reduction | 22.6% (1994 W → 1543 W) |
| Propulsion Optimisation | Optimal Configuration | HALE-Direct D80 + HALE-M 72×40 |
| Propulsion Optimisation | System Efficiency | 58.6% |
| Atmospheric Simulation | Energy Margin | 208.1% (27,893 Wh surplus) |
| Atmospheric Simulation | Total Solar Energy | 41,297 Wh |
| Atmospheric Simulation | Daylight Hours | 14.4 hours |
| Aerodynamic Performance | L/D Ratio at 20 km | 17.2 |

**Speaker Notes:**
These three computational subsystems provide the framework for evaluating HALE UAV conceptual designs. The propulsion optimisation achieves 22.6% power reduction through systematic motor-propeller matching. The atmospheric simulation validates 208.1% energy margin, confirming perpetual endurance potential. Combined with aerodynamic performance assessment, the integrated framework enables rapid evaluation of design alternatives and identifies critical trade-offs in the sizing process.

---

## Slide 18: Comparison with Established Platforms

**Title:** Design Comparison with Existing Platforms

**Content:**
| Platform | Mass (kg) | Wingspan (m) | Aspect Ratio | Endurance |
|----------|-----------|--------------|--------------|-----------|
| Zephyr S | 53 | 25 | 24 | 25+ days |
| Helios | 730 | 75 | 30 | 14+ hours |
| EAV-3 | 53 | 19.5 | 17.4 | Stratospheric test |
| AtlantikSolar | 6.9 | — | — | 81 hours |
| **Present Design** | ~114 | 32 | ~30 | Target: 24+ hours |

**Speaker Notes:**
Our conceptual design targets align with established HALE platform benchmarks. The 32-meter wingspan and approximately 30:1 aspect ratio position the design between the Zephyr S and Helios class—larger than production solar UAVs but smaller than the experimental Helios platform. The target 24-hour minimum endurance is conservative relative to Zephyr's 64-day achievement but represents a significant advancement over current sub-50-kilogram platforms. Hybrid energy storage provides the practical pathway to multi-day endurance.

---

## Slide 19: Conclusions

**Title:** Conclusions

**Content:**
- **Technical Feasibility:** Confirmed through implemented computational models
- **Key Findings:**
  1. Solar irradiance modelling provides 24-hour power prediction with cloud cover dynamics
  2. Propulsion optimisation achieves 22.6% power reduction, directly reducing storage requirements
  3. Atmospheric simulation validates 208.1% energy margin—perpetual endurance capability
  4. Hybrid energy storage (fuel cells + batteries) necessary for practical multi-day endurance
- **Practical Power Budget:** ~2 kW electrical demand met by ~9 kW solar flux with triple-junction GaAs

**Speaker Notes:**
This study confirms the technical feasibility of solar-powered HALE UAVs through implemented computational models rather than theoretical projections. The 208.1% energy margin validates perpetual endurance potential, while the 22.6% power reduction from propulsion optimisation directly impacts the critical night-time storage constraint. The fundamental insight: hybrid energy storage is necessary for practical multi-day endurance because pure battery solutions exceed feasible mass budgets. Future work should focus on high-fidelity validation, particularly CFD under low-Reynolds-number conditions and aeroelastic flutter analysis using the methodologies identified in literature.

---

## Slide 20: Future Work

**Title:** Recommendations for Future Work

**Content:**
- **Multi-Domain Coupling:** Integrate models into unified simulation framework
- **Multi-Point Optimisation:** Extend beyond cruise to climb, descent, loiter segments
- **High-Fidelity Modelling:**
  - CFD validation under low-Re conditions
  - Aeroelastic flutter analysis [44]
  - BEMT propeller design for HALE conditions
- **Thermal Modelling:** Battery/avionics at stratospheric temperatures (−60°C)
- **Flight Validation:** Scaled demonstrator fabrication
- **Emerging Technologies:**
  - Perovskite solar cells (44,000 W/kg)
  - Solid-state batteries
  - Supercapacitor storage

**Speaker Notes:**
Several avenues extend this work. Multi-point optimisation would analyze the complete mission profile rather than cruise-only conditions, capturing the power demands of climb and descent. High-fidelity CFD validation addresses the low-Reynolds-number regime where empirical methods have limited accuracy. Thermal modelling becomes critical at stratospheric temperatures where battery performance degrades significantly. The emerging perovskite solar cell technology—achieving 44,000 watts per kilogram—offers transformative potential if manufacturing maturity is achieved. Finally, flight validation through scaled demonstrator testing provides the ultimate validation of the analytical framework.

---

## Slide 21: References

**Title:** Key References

**Content:**
- [1] Goraj et al. (1999). Design concept of a HALE UAV. *Aircraft Design*
- [3] Romeo et al. (2004). HELIPLAT: Design analysis. *Journal of Aircraft*
- [10] Boukoberine et al. (2019). Energy storage systems for UAVs. *Journal of Power Sources*
- [39] Oettershagen et al. (2017). AtlantikSolar design. *Journal of Field Robotics*
- [40] Hwang et al. (2016). EAV-3 aerodynamic design. *Journal of Aircraft*
- [42] Dantsker et al. (2020). Propulsion optimisation for solar UAVs. *AIAA*
- [43] Łopusiewicz & Książek (2024). PV integration on composite wings. *ICAS*
- [44] Murua et al. (2011). Very flexible aircraft aeroelasticity. *AIAA*

**Speaker Notes:**
These references represent the foundational literature for HALE UAV design. Goraj and colleagues established early configuration studies. Romeo's HELIPLAT program demonstrated structural and aerodynamic analysis methodologies. Boukoberine's comparative review clarifies energy storage trade-offs. Oettershagen's AtlantikSolar work provides the charge-margin methodology adopted in our analysis. Dantsker's propulsion optimisation framework directly enables our motor-propeller selection approach. The remaining references address photovoltaic integration, aeroelasticity, and platform-specific design studies.

---

## Slide 22: Acknowledgments

**Title:** Acknowledgments

**Content:**
- **Guide:** Dr Amalesh Barai, Professor, Department of Aerospace Engineering
- **Department:** Faculty of Engineering & Technology, JAIN (Deemed-to-be University)
- **Computing Resources:** Python scientific computing ecosystem (NumPy, SciPy, Pandas, Matplotlib)

**Visuals:** [Thank you graphic]

---

## Slide 23: Questions

**Title:** Questions & Discussion

**Content:**
- Thank you for your attention
- Open for questions

**Visuals:** [Contact information placeholder]

---

*Presentation prepared using research data from implemented computational models: solar irradiance simulation, propulsion optimisation, and atmospheric mission simulation.*