# HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES (UAVs): SUSTAINED FLIGHT THROUGH RENEWABLE ENERGY

**Department of Aerospace Engineering**
JGI Global Campus, Jakkasandra Post, Kanakapura Taluk, Ramanagara District, Pin Code: 562 112

**2025–2026**

End Year Project Report

Submitted in partial fulfilment for the award of the degree of

**BACHELOR OF TECHNOLOGY IN AEROSPACE ENGINEERING**

Submitted by: **Parth Patil** (22BTRAS031)

Under the guidance of **Dr Amalesh Barai**, Professor, Department of Aerospace Engineering, Faculty of Engineering & Technology, JAIN (Deemed-to-be University)

---

## Abstract

High Altitude Long Endurance (HALE) Unmanned Aerial Vehicles (UAVs) operate at altitudes above 18 km with mission durations from several days to weeks. This project focuses on the conceptual design, performance analysis, and feasibility assessment of a solar-powered HALE UAV through implemented computational models. Key design challenges include low Reynolds number aerodynamics, lightweight composite structures, and hybrid renewable energy integration.

This Version 5 report integrates completed computational work across three core subsystems: solar irradiance modelling with cloud cover dynamics, propulsion system optimisation using mission-based selection methods, and atmospheric simulation validating 24-hour mission capability. Numerical evaluation indicates that the conceptual HALE model produces realistic power demands (~2 kW electrical), while high-altitude solar flux combined with triple-junction gallium arsenide (GaAs) photovoltaics provides ~9 kW usable power. Night-time storage requirements (~23.9 kWh) make pure lithium-ion battery solutions infeasible (~95 kg), whereas hydrogen fuel-cell storage meets the requirement at <5 kg system mass. Full mission simulation yields 208.1% energy margin, confirming perpetual endurance capability.

---

## 1. Introduction

HALE UAVs bridge the gap between conventional aircraft and satellites, remaining aloft for days or weeks at altitudes above 18 km. They serve persistent surveillance, atmospheric research, and low-Earth-orbit (LEO) communication relay roles [1][2]. Advanced platforms—NASA Helios, Airbus Zephyr S, QinetiQ Zephyr S—have achieved endurance exceeding 24 hours, with some prototypes demonstrating multi-week sorties using solar arrays, high-energy-density batteries, and fuel cells [3][4].

### 1.1 Core Engineering Problem

The fundamental challenge in HALE UAV design is **energy balance**: solar energy collected during daylight must satisfy total propulsion and payload power demand over a complete diurnal cycle. At stratospheric altitudes (18–22 km), air density drops to roughly one-tenth sea-level, requiring high-aspect-ratio wings (>20:1) to generate sufficient lift while minimising induced drag [6][7].

The critical constraint emerges at night: without solar input, the aircraft must sustain flight from stored energy. Battery mass scales directly with night-phase energy demand—for a typical 12-hour night at ~2 kW average power, this requires ~24 kWh storage. At lithium-ion energy density of 250 Wh/kg, this translates to approximately 95 kg of battery mass alone, exceeding the feasible empty weight of most HALE platforms.

This energy bottleneck drives the need for:
- High-efficiency solar cells (25–30% triple-junction GaAs)
- Optimised propulsion systems to minimise power demand
- Hybrid energy storage (fuel cells + batteries) for extended endurance
- Accurate atmospheric and irradiance modelling for mission planning

### 1.2 Completed Computational Work

This project implements three core computational subsystems for HALE UAV design:

1. **Solar Irradiance Model** — 24-hour continuous simulation with dynamic cloud cover modelling (k_c = 0.0–1.0), providing power state P_solar for differential energy balance: dE_bat/dt = P_solar − P_out

2. **Propulsion Optimisation** — Mission-based motor-propeller selection framework achieving 22.6% reduction in cruise power (1994 W → 1543 W) through system-level efficiency matching

3. **Atmospheric Simulation** — Full mission profile at 20 km altitude implementing ISA validation, solar position calculation, and energy balance closure yielding 208.1% energy margin

These subsystems provide the computational framework for evaluating HALE UAV conceptual designs and quantifying performance margins.

### 1.3 Real-World Platform Benchmarks
- **Zephyr S (Airbus):** Operational mass: 60 kg | Maximum certified takeoff weight (MTOW): 75 kg | Battery pack: 24 kg (40% of total mass) | Payload capacity: 5 kg | Wingspan: 25 m | Max Altitude: 23,200 m (76,100 ft) | Endurance: 64 days (2022 validation)

- **NASA Helios:** Mass: ~929 kg (Gross) | Wingspan: 75 m | Aspect Ratio: 30.9 | Max Altitude: 29,524 m (96,863 ft)
- **EAV-3 (KARI):** Mass: 53 kg | Wingspan: 19.5 m | Aspect Ratio: 17.4

---

## 2. Aim and Objectives

### 2.1 Aim

The aim of this research is to develop a **computational modelling framework** for analysing solar-powered HALE UAV performance, integrating solar irradiance prediction, propulsion system optimisation, and atmospheric simulation to evaluate energy balance and mission feasibility.

### 2.2 Objectives

#### Primary Objectives (Completed)

| Objective | Description | Key Result |
|-----------|-------------|------------|
| Solar Irradiance Modelling | 24-hour solar power prediction with cloud cover dynamics | k_c parameter (0.0–1.0) for meteorological risk assessment |
| Propulsion Optimisation | Mission-based motor-propeller selection for minimum power | 22.6% reduction (1994 W → 1543 W), 58.6% system efficiency |
| Atmospheric Simulation | Full mission profile at 20 km with ISA validation | 208.1% energy margin, 24-hour continuous operation |

#### Secondary Objectives

1. **Energy Balance Evaluation** — Quantify night-time storage requirements and compare battery vs. fuel-cell solutions
2. **Mission-Level Simulation** — Integrated 24-hour mission profile combining atmospheric, solar, and power demand models
3. **Literature Integration** — Synthesise state-of-the-art HALE design methodologies from peer-reviewed sources

---

## 3. Market Survey and Literature Review

### 3.1 Previous Studies

The HALE UAV market has expanded driven by civilian, military, and commercial demand for real-time situational awareness and reduced satellite reliance [1][2][3][4][17].

#### 3.1.1 Configuration Studies

Goraj et al. [1] presented four aerodynamic concepts for 27 km altitude HALE UAVs, showing carefully designed biplanes achieve comparable efficiency to monoplanes with higher payload capacity. Subsequent work [2] addressed low-Reynolds-number aerodynamics, lightweight structures, propulsion, and autonomous flight control. Romeo et al. [3] (HELIPLAT programme) demonstrated twin-boom distributed propulsion with solar cell area optimisation. Blended-wing-body (BWB) configurations improve lift-to-drag ratios through distributed load paths [18][19]. Joined-wing configurations achieve span efficiency factors of 1.4–1.5, reducing induced drag [20].

#### 3.1.2 Structural Design

CFRP composites provide necessary stiffness-to-weight ratios for high-aspect-ratio wings [8][9][21]. Key considerations include weight minimisation, flutter margins, and redundancy [22]. Autoclave curing and resin-transfer moulding achieve required material properties [21]. Fatigue testing under realistic turbulence conditions is essential for long-duration flight [23].

#### 3.1.3 Energy System Analysis

Fuel cells outperform batteries above 2.8 kWh demand [10][11], a threshold often exceeded during high-altitude operations (approximately 3.5% power increase per km altitude) [10]. Triple-junction GaAs cells achieve 25–30% efficiency; thin-film cells offer lower efficiency but reduced weight [14][15]. Night-time endurance remains the critical limitation due to battery degradation [24][25].

#### 3.1.4 Stability and Control

Longitudinal and directional stability are essential for sustained flight [12][13]. Flutter analysis is critical for high-aspect-ratio wings as aeroelastic coupling can cause catastrophic failure [22][26]. Control surfaces require larger deflection angles at low density for equivalent effectiveness [27].

### 3.2 Recent Developments

#### 3.2.1 Perpetual-Flight Solar UAV Design

Oettershagen et al. [39] developed the AtlantikSolar UAV (6.9 kg), achieving 81-hour continuous flight—world record for aircraft <50 kg. The conceptual design and analysis framework (CDAF) optimises wing span, aspect ratio, and battery mass using excess time and charge margin metrics. Flight results show 39% minimum state-of-charge, 6.8 hours excess time, and 6.2 hours charge margin. The design philosophy of maximising meteorological robustness is directly applicable to high-altitude platforms.

#### 3.2.2 Solar HALE UAV Aerodynamic Design (EAV-3)

Hwang et al. [40] reported KARI's EAV-3: 53 kg (22 kg structure), 19.5 m span, aspect ratio 17.4, cruise speed 6 m/s. Critical considerations included significant wing bending (404 mm at 1-G flight with T-800 carbon fibre) and side-wind effects. No centre-of-gravity shift occurs during flight, yielding a static margin of 28.4% with CG at 31% MAC.

#### 3.2.3 Hybrid Turbofan/Solar HALE UAV Concepts

Mermer and Özgen [41] investigated hybrid turbofan/solar HALE UAV design achieving 24+ hours endurance with 1,000 kg payload at 6,096–9,144 m ceiling. Turbofan engines climb to altitude; solar and battery sustain loiter. Competitor studies show average empty weight fractions of 0.6218, aspect ratios of 24.5, and wingspans of 66.45 m.

#### 3.2.4 Propulsion System Optimisation

Dantsker et al. [42] presented mission-based propulsion optimisation for the UIUC-TUM Solar Flyer, selecting optimal motor-propeller combinations. The tool achieved 19% efficiency improvement over baseline. This directly affects power budget and required solar array area.

#### 3.2.5 Aeroelastic Stability of Very Flexible Aircraft

Murua et al. [44] developed unified nonlinear aeroelastic-flight mechanics models for very flexible aircraft, integrating geometrically exact beam finite elements with UVLM including free-wake effects. Three-dimensional aerodynamic effects—particularly wake interference between wing and tail—significantly impact dynamics. This provides flutter boundary prediction more accurate than decoupled approaches.

#### 3.2.6 Photovoltaic Cell Integration on Composite Wings

Łopusiewicz and Książek [43] investigated photovoltaic integration challenges:

- **Solar cell performance**: SunPower Maxeon III cells achieve 231–243 Wp/m² with 153 cm² area and 6.5 g weight.
- **Lamination methods**: First method (laminating successive layers to existing fibreglass–photovoltaic composite) shows 9.5% higher power at low loads and 12.5% higher at high loads.
- **Micro-cracking**: Under aerodynamic loading, stress concentrations cause micro-cracking.
- **Galvanic isolation**: Essential with carbon-fibre substrates to prevent short-circuiting.
- **Manufacturing defects**: Electroluminescence testing reveals silicon layer defects, incorrect soldering, lamination imperfections.
- **Efficiency degradation**: Wing deflection reduces photovoltaic output; first lamination method shows superior resistance.

#### 3.2.7 Battery-Free UAV Concepts

Liller et al. [45] proposed battery-free solar UAVs storing energy in supercapacitors. Novel energy-aware control algorithms (Greedy and Predictive) prevent brownouts and minimise thrust loss events. While at different scale from HALE platforms, the energy-management principles eliminate battery degradation concerns.

### 3.3 Synthesis and Comparative Analysis

**Converging Trends:**
1. High-aspect-ratio monoplane configurations dominate (17.4 to 30+ aspect ratio) [40][3].
2. Solar cell efficiencies of 25–30% (triple-junction GaAs) are practical upper bounds [14][15][41].
3. Hybrid energy storage is necessary for multi-day endurance [10][11][39][41].
4. Propulsion optimisation yields 15–20% efficiency improvements [42].
5. Aeroelastic coupling is critical for high-aspect-ratio flexible wings [22][26][44].

**Contradictions:**
1. **Battery vs. fuel cell**: Original analysis favours fuel cells above 2.8 kWh [10], but AtlantikSolar achieved 81 hours with batteries alone [39] at lower altitude. Optimal storage depends on platform scale and mission profile.
2. **Configuration philosophy**: EAV-3 aspect ratio of 17.4 [40] contrasts with emphasis on >20, suggesting practical constraints limit achievable ratios.
3. **Battery-free approaches**: Liller et al. [45] represents different paradigm but insufficient TRL for HALE.

| Theme | Old Sources | New Sources | Action |
|-------|-----------|-------------|--------|
| UAV Structural Loads | Goraj [1][2], Romeo [3] | Murua [44], Łopusiewicz [43] | Merged with aeroelastic and PV challenges |
| Solar Efficiency | Najafi [4], literature [14][15] | Łopusiewicz [43], Mermer [41] | Updated with integration data |
| Material Fatigue | Goraj [1][2], composites [8][9] | — | Retained |
| Perpetual Flight | Najafi [4] | Oettershagen [39], Liller [45] | Expanded with record data |
| Aerodynamic Design | Goraj [1][2], Romeo [3] | Hwang [40], Mermer [41] | Expanded with EAV-3 and sizing data |
| Propulsion Optimisation | Literature [6][7] | Dantsker [42] | New section |
| Aeroelastic Stability | Flutter [22][26] | Murua [44] | Expanded with UVLM analysis |

### 3.4 Comparative Metrics & Milestones
- **Endurance Limitations (pre-2022):** Sub-50kg platforms primarily capped at ~81 hours (AtlantikSolar benchmark).
- **Recent Milestones (2022+):** Airbus Zephyr S shattered constraints with 64 continuous days of flight. Concurrently, the PHASA-35 sustained operations at 66,000 ft, confirming composite reliability and thin-film GaAs efficiency (>28%).
- **Structural Integrity Benchmarks:** The EAV-3 successfully demonstrated a static margin of 28.4% and a structural bending resistance of 404mm on a 9.75m semi-span under 1G loading.


---

## 4. Problem Definition and Design Specifications

The design challenge is synthesising a solar-powered HALE UAV sustaining continuous flight above 18 km for minimum 24 hours, with ambition for several days [1][2][3][4].

**Conceptual Performance Results:**
- Cruise power: ≈ 2 kW
- Solar power available: ≈ 9 kW
- Night storage: ≈ 24 kWh
- Battery mass: ≈ 95 kg
- Hydrogen equivalent: ≈ 1.44 kg (≈ 4.3 kg system)

### 4.1 Aerodynamic Integration

At stratospheric altitudes, air density drops to roughly one-tenth sea-level, forcing low Reynolds number operation (10⁵–10⁶) [6][7]. The design must maximise lift-to-drag while minimising induced drag. Three topologies—biplane, blended-wing-body (BWB), joined-wing—have been evaluated [1][2][3][18][19][20]. The EAV-3 [40] provides reference: 19.5 m span, aspect ratio 17.4, 6 m/s cruise, successful stratospheric operation despite significant wing bending.

### 4.2 Structural Optimisation

Structural design reconciles ultra-light high-stiffness airframe with flutter safety and fatigue resistance [8][9][21][22]. CFRP composites form primary load-carrying elements. FEA predicts static deflection, modal frequencies, and flutter margins [5]. Murua et al. [44] methodology—integrating geometrically exact beam models with UVLM—provides accurate flutter prediction for detailed analysis.

### 4.3 Hybrid Energy System

Solar power is primary daytime energy. Triple-junction GaAs cells (25–30% efficiency) [14][15] mount on wing and fuselage. Photovoltaic integration must address Łopusiewicz and Książek challenges: micro-cracking, galvanic isolation, manufacturing defects [43].

Excess energy stores in high-cycle lithium-ion batteries (~250 Wh/kg) [10][24]. Missions exceeding 2.8 kWh night-time demand incorporate hydrogen fuel cell stacks (~0.5 kg/kWh) [10][11]. Charge-margin optimisation [39] ensures robust multi-day operation.

### 4.4 Mission Profile and Constraints

Aircraft cruises at 18–22 km at approximately 80 km/h. Payload capacity: 5–10 kg. Environmental constraints—cloud cover, temperature gradients, wind shear—incorporated into mission simulator [28][29].

### 4.5 Power Electronics Subsystem

#### 4.5.1 Solar Cell Technologies and Selection

Solar cell selection for HALE UAVs involves a critical trade-off between efficiency,
specific power (W/g), flexibility, and environmental durability at stratospheric altitudes.

**Current Technology Landscape (post-2023):**

Four principal photovoltaic technologies are employed in UAV applications:

**Monocrystalline Silicon** remains the established baseline. Studies on the HALE UAV ITB
platform demonstrated monocrystalline silicon cells achieving a power density of 224 W/m²
and a specific power of 436 W/kg, requiring a minimum wing coverage of 5.94 m² to sustain
24-hour flight at 20,000 ft [46].

**CIGS Thin-Film** offers flexibility up to 13% efficiency but requires hermetic encapsulation
due to moisture sensitivity, which introduces additional structural weight and reduces mounting
options on composite wing skins [47].

**Gallium Arsenide (GaAs) Thin-Film** provides the highest conversion efficiency with
excellent specific power for aerospace, making it the preferred technology for platforms
like the BAE Systems PHASA-35, which achieved stratospheric flight exceeding 66,000 ft
by December 2024 [48].

**Perovskite Solar Cells (Emerging, 2024):** The most significant recent development is the
demonstration of quasi-2D perovskite cells by researchers at Johannes Kepler University Linz.
Published in Nature Energy (2024), these ultra-thin flexible cells (< 2.5 μm thick) achieved
a specific power density of 44 W/g — contributing only 1/400th of total drone weight —
with 20.1% champion efficiency [49]
This represents a paradigm shift: at 44 W/g, perovskite cells are orders of magnitude lighter
than crystalline silicon panels for equivalent power output.

MIT's printed organic photovoltaic cells (2022, ongoing) have demonstrated cells 1/100th
the weight of conventional panels generating 18× more power per kilogram, fabricated via
slot-die coating on 3-micron substrates, with direct applicability to UAV wing skin
lamination [50].

**Structural Integration Method and Weight Penalty:**
The method of solar cell integration onto the wing structure directly determines the net
weight penalty. Three approaches are documented:

1. **Surface bonding (retrofit):** Adds < 1 g/W for flexible cells. Simple but adds aerodynamic
   surface discontinuity.
2. **Embedded-in-mold:** Cells placed inside the wing mold before resin cure. Eliminates
   aerodynamic penalty and protects cells, but damaged cells cannot be replaced [51].
3. **Designed-in integration (optimal):** If solar cells are designed into the wing skin from
   the outset, one layer of CFRP or fiberglass can be removed, resulting in **zero net weight
   addition** while gaining significant power generation [52].

**Key design insight:** Increasing wing area to accommodate more solar cells increases both
structural weight and induced drag. The induced drag is inversely proportional to aspect ratio,
meaning high-AR wings simultaneously reduce drag and maximize solar collection area — the
primary reason HALE platforms use extreme aspect ratios (>20) [53].

#### 4.5.2 Battery Systems for Night-Phase Energy Storage

Night-phase energy storage is the primary sizing driver for the battery subsystem, as the
aircraft must sustain level flight and payload operations from sunset to sunrise without
solar input.

**Lithium-Ion (Current Baseline):**
A 2025 comprehensive review (ScienceDirect, January 2025) of renewable power systems for UAVs
confirmed that lithium-ion batteries dominate current deployments due to high power density,
but their low energy density restricts flight endurance to under 90 minutes for small UAVs
without solar augmentation [54].

**Lithium-Sulfur (Next Generation):**
A sensitivity analysis of energy management strategies for solar-powered HALE aircraft
ranked lithium-sulfur battery improvement as the **second most impactful technology** for
overall aircraft performance improvement, after structural/control system enhancement and
ahead of solar cell efficiency gains. The proposed EMS using gravitational potential storage
retained 23.5% more energy in batteries per day-night cycle compared to conventional strategies
[55].

The PHASA-35 stratospheric flight in December 2024 to 66,000 ft demonstrated operational
viability of current long-life battery technology in real stratospheric conditions, targeting
full operational capability by 2026 [48].

**Hybrid Multi-Source Architecture (2025 Frontier):**
XSun and H3 Dynamics (July 2025) announced development of the first UAV combining solar
energy, hydrogen fuel cells, and battery storage in a tri-source intelligent power architecture.
Ultra-thin solar PV cells integrated directly into wing surfaces harvest solar energy;
hydrogen fuel cells and batteries handle peak demand and night-phase operation. Hybrid systems
of this type have demonstrated endurance improvements of over 60% compared to single power
sources [56].

**Battery Sizing Methodology:**
Battery capacity is calculated from the night-phase power budget:

  E_bat = P_night × t_night / η_discharge

Where P_night is total power demand (propulsion + payload + avionics), t_night is the
longest night duration at the design latitude and season, and η_discharge is the
battery discharge efficiency (typically 0.85–0.90 for Li-ion).

The thermal management of battery and avionics at stratospheric temperatures (as low as
−60°C) is a critical design constraint; the DLR HAP program developed mathematical thermal
models to ensure reliable battery operation across the full mission thermal envelope [57].

#### 4.5.3 DC-DC Converters and MPPT Architecture

**Role in the Power Chain:**
The solar power chain in a HALE UAV follows: Solar Array → MPPT DC-DC Converter → Battery
Bus → Motor Controllers + Avionics Bus. DC-DC converters serve two functions: voltage
level adaptation between the solar array, battery, and load buses; and execution of Maximum
Power Point Tracking (MPPT) to extract maximum available solar power under varying
irradiance and temperature conditions throughout the flight envelope [58].

**MPPT Algorithms:**
The Perturb & Observe (P&O) algorithm is the most widely implemented MPPT method due to
simplicity and low computational overhead, suitable for microcontroller-based implementations.
A 2025 cascaded DC-DC prototype (CISTEM 2024, EPJ Web of Conferences) demonstrated
real-time P&O MPPT with constant-current/constant-voltage (CC-CV) battery charging,
achieving dynamic tracking of the PV maximum power point across varying irradiance
throughout the day [59].

Advanced methods including Incremental Conductance (InC), fuzzy logic controllers,
and machine learning-based MPPT (ML-RBFNN) are increasingly applied where partial
shading conditions or rapid irradiance changes (e.g., cloud transients) must be handled
[60].

**Converter Topology for HALE Applications:**
For HALE UAVs, Vicor's DCM™ (Discontinued Conduction Mode) power modules are documented
in industry case studies as enabling high power density with significant mass reduction.
The modular approach allows accommodation of changing power loads without full redesign,
with the ability to parallel modules for additional capacity — critical for a platform
where power budgets evolve across design iterations [61].

Buck-Boost topology is preferred when the solar array output voltage fluctuates above
and below the battery bus voltage — a common condition as solar irradiance, temperature,
and array degradation vary across the mission. Bidirectional converters additionally
allow battery charge management without separate circuitry [58].

**Power Distribution Architecture:**
UAV electrical power distribution systems (EPDS) typically operate at 28V (low voltage)
and 270V (high voltage) bus standards. For HALE applications with high power payloads
(surveillance radar, communications), high-voltage distribution reduces I²R losses in
cabling — an important weight and efficiency consideration [62].

### 4.5.4 Energy System Quantitative Baselines
- **Lithium-Ion Pack (Current Baseline):** 200–300 Wh/kg specific energy (cell-level); 150–250 Wh/kg pack-level (including thermal management, BMS, structural integration) | Required mass for 24 kWh night phase: 96–160 kg (depending on chemistry and integration method).
- **Lithium-Sulfur (Next Generation):** 300–350 Wh/kg (practical pack-level energy density) | Theoretical maximum: >500 Wh/kg | Required mass for 24 kWh night phase: ~70–80 kg.
- **Hydrogen PEM Stack (700 bar):** Theoretical H₂ energy density ~800 Wh/kg (compressed gas only) | System-level energy density: 150–250 Wh/kg (accounting for pressure vessel, regulator, fuel cell stack, water management, and thermal control) | Required mass for 24 kWh night phase: 96–160 kg.
- **Solar Skin Integration:** Traditional Monocrystalline Silicon ~436 W/kg vs. Perovskite Quasi-2D (2024) ~1,200–1,800 W/kg (theoretical maximum: 2,500 W/kg).

---

## 5. Methodology

### 5.1 Implemented Computational Framework

The methodology centres on **implemented computational models** for HALE UAV performance analysis, replacing purely theoretical approaches with validated simulation tools:

1. **Solar Irradiance Model** — Implements solar position algorithms, atmospheric transmittance, and cloud cover parameter (k_c) for continuous 24-hour power prediction
2. **Propulsion Optimisation** — Mission-based motor-propeller selection using Dantsker methodology [42] for system-level efficiency maximisation
3. **Atmospheric Simulation** — ISA implementation with mission profile integration for energy balance validation

### 5.2 Literature Foundation

Initial phases reviewed state-of-the-art HALE UAV research [1][2][3][4], cataloguing platforms (NASA Helios, Airbus Zephyr, DARPA Vulture, KARI EAV-3 [40]) and mission parameters. Solar-cell literature was examined (triple-junction vs thin-film [14][15]); energy-storage options were assessed (lithium-ion vs fuel cells [10][11][24][25]).

Expanded literature includes perpetual-flight methodologies [39], propulsion optimisation [42], coupled aeroelastic modelling [44], photovoltaic integration challenges [43], hybrid turbofan/solar concepts [41], and battery-free architectures [45].

### 5.3 Mission Requirements Definition

Mission requirements: minimum 24-hour endurance, target L/D 25–30, payload for scientific instruments and communications, structural stiffness for flutter avoidance [1][2][3][4]. EAV-3 [40] validates target L/D achievable; AtlantikSolar [39] confirms energy balance closure at low altitude, extensible to high altitude (~1,360 W/m² irradiance).

### 5.4 Aerodynamic Modelling

#### 5.4.1 Airfoil and Wing Analysis

Aerodynamic evaluation couples analytical theory with computational fluid dynamics (CFD) [5][6][7]. Candidate airfoils screened using low-Reynolds-number data (C_L, C_D, C_L/C_D across ~0.5–2 × 10⁶ Reynolds range). CFD captures 3D effects: tip vortices, spanwise flow, pressure-gradient separation. EAV-3 [40] demonstrates wing bending and side-wind consideration at low cruise speeds (6 m/s).

#### 5.4.2 Wing Configuration Comparison

Three configurations examined—biplane, BWB, joined-wing [1][2][3][18][19][20]. Biplane achieves lower effective aspect ratio through interference. BWB provides smooth pressure distribution and higher L/D. Joined-wing yields 1.4–1.5 span efficiency [20]. Mermer and Özgen [41] competitor study shows average aspect ratios of 24.5 and wingspans of 66.45 m; their structural weight prediction model warrants adoption.

### 5.5 Structural Modelling

#### 5.5.1 Material Selection

CFRP selected as baseline [8][9][21]. Anisotropic nature allows stiffness and strength tailoring through fibre ply orientation along principal load paths. Out-of-plane reinforcement and nano-engineered resin systems improve damage tolerance [8].

#### 5.5.2 Structural Analysis

Detailed finite-element model constructed using ANSYS Workbench [5], incorporating aerodynamic pressure loads from CFD and inertial loads from flight dynamics. Flutter analysis uses coupled aeroelastic module integrating aerodynamic influence coefficients (doublet-lattice method) with structural modal data. Murua et al. [44] framework offers higher-fidelity flutter prediction for very flexible wings where geometrically nonlinear deformations alter aerodynamic characteristics.

### 5.6 Energy System Modelling

#### 5.6.1 Solar Power Estimation

Solar subsystem sized based on triple-junction photovoltaic cells exceeding 350 W/kg specific power under stratospheric irradiance (~1,360 W/m²) [14][15]. Model incorporates cosine losses, shading, and seasonal/diurnal variations at 18–20 km.

Łopusiewicz [43] integration challenges factored in: first lamination method shows 9.5% higher power under low loading; efficiency degradation under wing deflection measurable. These losses and manufacturing defect allowances become derating factors.

#### 5.6.2 Battery/Fuel-Cell Simulation

Hybrid storage model simulates lithium-ion pack (~250 Wh/kg) and PEM fuel-cell stack in MATLAB/Simulink [10][11]. Night-time endurance evaluated by integrating net power deficit over dark period.

AtlantikSolar charge-margin methodology [39] provides safety margin framework. Excess time (T_exc) and charge margin (T_cm) metrics quantify margin above minimum acceptable threshold. Designing for 30–40% charge margin (as demonstrated in 81-hour flight) ensures robustness against cloud cover, degradation, and unexpected demands.

#### 5.6.3 Hybrid Energy Management

Energy-balance model orchestrates power flows from solar array to storage and propulsion/avionics [10][11]. Hierarchical management prioritises battery charging with excess solar, fuel-cell supplementation during extended night.

### 5.7 Stability and Control Analysis

Stability assessment builds on classical longitudinal and directional theory, adapted for low-density HALE flight [12][13]. Static margin calculated by locating aerodynamic centre and comparing to CG location, ensuring minimum 5% MAC margin. EAV-3 [40] provides reference: static margin 28.4% with CG at 31% MAC.

Control surface sizing uses derivative method, incorporating reduced dynamic pressure effects [27]. Flutter boundaries estimated using Doublet Lattice Method (DLM), with UVLM option [44] for detailed assessment.

### 5.8 Performance Simulation

Integrated simulations verify conceptual UAV meets all targets. Altitude–power relationship incorporates 3.5% power increase per km altitude gain. MATLAB used for system-level analyses; ANSYS for high-fidelity aero-structural coupling [5].

### 5.9 ISA Model Validation

The atmospheric simulation model implements ICAO Standard Atmosphere (Doc 7488, 1993) with three layers:

| Altitude (m) | Temperature (K) | Pressure (kPa) | Density (kg/m³) |
|--------------|-----------------|----------------|-----------------|
| 0            | 288.15          | 101.33         | 1.2250          |
| 5,000        | 255.65          | 54.02          | 0.7361          |
| 10,000       | 223.15          | 26.44          | 0.4127          |
| 15,000       | 216.65          | 12.04          | 0.1937          |
| 20,000       | 216.65          | 5.47           | 0.0880          |
| 25,000       | 221.65          | 2.51           | 0.0395          |

✓ Matches standard ISA tables within expected tolerance.

### 5.10 Design Integration and Optimisation

Multi-objective genetic algorithm (MOGA) explores design space, simultaneously minimising mass, maximising endurance and L/D while satisfying flutter margin, structural stress, and solar-panel constraints. Optimiser iteratively adjusts wing span, chord distribution, spar geometry, CFRP lay-up, solar-cell layout, and storage sizing.

### 5.11 Structural Analysis for Ultralight Design

#### 5.11.1 Ultralight CFRP Structural Design Philosophy

The structural design of a HALE UAV is governed by an extreme mass budget constraint.
The perpetual endurance condition requires that solar energy collected during daylight
exactly meet or exceed total energy consumption over a 24-hour cycle; any excess structural
mass directly increases required wing area, which further increases structural mass in a
compounding feedback loop.

**Material Selection — CFRP:**
High-modulus Carbon Fiber Reinforced Polymer (CFRP) is the universally adopted structural
material for HALE-class platforms. Parametric studies on the SHAMPO (Solar HALE Aircraft
Multi Payload & Operation) platform at Turin Polytechnic demonstrated that high-modulus
CFRP minimized airframe weight while sustaining the aerodynamic loads associated with
extreme-AR wings at stratospheric altitudes [63].

The HELIPLAT® structural demonstrator program (Romeo et al.) established fundamental CFRP
design and manufacturing procedures for HALE-class UAVs, including bearing strength testing
of bolted CFRP joints in wing fittings — a critical detail for modular wing assembly
required for transport and deployment [64].

FDM-fabricated ABS/CFRP sandwich structures have demonstrated specific strength improvement
from 20 to 145 kN·m/kg and Young's modulus from 0.63 to 10.1 GPa with increasing CFRP
layer count, with ANN-based optimization of core density and layer count — offering a
pathway to rapid-prototyped structural components with near-aerospace mechanical properties
[65].

**Generative Modelling for Ultralight Structures (2024–2025):**
A methodology using generative modelling for automating ultralight, highly flexible aircraft
structure design was presented, integrating FEM verification at low- and mid-fidelity levels
for iterative structural improvement — directly applicable to HALE wing spar and rib design
[66].

**2025 — Joined-Wing Configuration:**
A 2025 study (International Journal of Aerospace Engineering, Wiley) analyzed the structural
characteristics of a HALE joined-wing configuration UAV, completing a preliminary structural
design based on aircraft design indices and fundamental structural principles. The joined-wing
concept offers structural efficiency advantages for very high AR wings by transferring bending
loads through the rear wing — relevant for the non-planar wing configurations being
considered in next-generation HALE designs [67].

**MDO with Eco-Material Selection (2023):**
A 2023 Nature Scientific Reports study applied Multidisciplinary Design Optimization (MDO)
to minimize CO₂ footprint of a solar-powered HALE, with structural material (CFRP, GFRP,
aluminium, steel) as a design variable within OpenAeroStruct/OpenMDAO. The study confirmed
CFRP as the Pareto-optimal choice for the solar-powered HALE structural envelope in both
performance and environmental terms [68].

#### 5.11.2 Structural Integration of Solar Cells on the Wing

Integrating solar cells onto the wing structure introduces three structural interactions
that must be accounted for in the structural analysis:

1. **Additional surface mass distribution** — solar cells add a distributed mass along the
   wing upper surface, modifying the spanwise mass distribution and consequently the
   bending moment envelope and aeroelastic response.

2. **Stiffness modification** — embedded or laminated solar cell modules alter the local
   bending and torsional stiffness of the wing skin, requiring updated FEM models.

3. **Manufacturing constraints** — the embedded-in-mold integration method (placing cells
   before resin cure) constrains permissible wing skin layup sequences and resin systems
   to those compatible with solar cell substrate materials and operating temperatures.

**Integration Methods and Structural Implications:**

The three integration approaches (surface bonding, mold-embedded, designed-in) differ
significantly in structural consequence. The designed-in approach, where one CFRP layer
is removed to accommodate the solar module thickness, is structurally the most elegant
but requires that the solar module contributes to or at minimum does not degrade the
wing skin's load-carrying capability.

A study on laminated flexible solar cells (PMC/Energies) established that wing ribs must
be designed differently depending on solar module rigidity: lightweight flexible modules
require more closely spaced ribs to prevent panel buckling, while rigid modules act as
structural face sheets but add more mass [51].

**Aeroelastic Considerations:**
HALE platforms with extreme AR wings are inherently aeroelastically flexible. The addition
of solar cell mass along the wing upper surface modifies the chordwise centre-of-mass
position, affecting the torsional divergence and flutter speed margins. This must be
assessed through coupled aeroelastic analysis — the existing repository contains the
Murua (2011) paper on very flexible aircraft aeroelasticity which provides the theoretical
framework for this analysis [44].

#### 5.11.3 Weight Penalty Analysis

Weight penalty analysis quantifies the net mass impact of incorporating solar cells and
associated power electronics into the primary structure, evaluated against the power benefit.

**Framework:**

The total solar subsystem weight W_solar comprises:

  W_solar = W_cells + W_encapsulation + W_wiring + W_connectors + W_MPPT

Where:
- W_cells = A_cell × ρ_cell (cell area × areal density, kg/m²)
- W_encapsulation = protective laminate/coating mass
- W_wiring = interconnect cabling mass (function of panel count and span)
- W_connectors = junction box and bypass diode mass
- W_MPPT = MPPT converter mass

**Technology Comparison (specific power basis):**

| Technology         | Efficiency | Specific Power | Notes                          |
|--------------------|------------|----------------|--------------------------------|
| Monocrystalline Si | ~22%       | ~436 W/kg      | Established, rigid             |
| CIGS Thin Film     | ~13%       | ~150–200 W/kg  | Flexible, needs encapsulation  |
| GaAs Thin Film     | ~28–30%    | ~600+ W/kg     | PHASA-35 class, high cost      |
| Perovskite (2024)  | ~20.1%     | ~44,000 W/kg   | Ultra-thin, pre-commercial     |
| MIT Printed OPV    | ~15%       | ~18× Si        | Printed, scalable              |

**Designed-In Net Weight Penalty:**
As established by the SAE Mobility Engineering study, if solar integration is designed
into the wing skin from the outset (removing one CFRP ply to accommodate cell thickness),
net weight addition is effectively zero while power generation is added. This is the
target integration methodology for the present design [52].

**Sensitivity Analysis Approach:**
The overall aircraft sensitivity to solar subsystem mass follows from the conceptual sizing
loop. Increasing W_solar by δW requires the wing to grow by approximately:

  δW_wing ≈ k × δW_solar  (where k is the structural weight fraction sensitivity)

This compounding effect means that a 1 kg reduction in solar cell areal density has a
total system-level mass benefit larger than 1 kg — often 2–3× the direct saving — due
to reduced wing, tail, and battery sizing requirements. This multiplicative leverage is
the fundamental justification for pursuing ultra-low-areal-density solar cell technologies
in HALE design.

A parametric study from ScienceDirect confirmed that solar panel efficiency and mass are
the most influential parameters on overall platform dimensions in the HALE sizing loop
[63].

---

## 6. Analysis and Discussion

This section synthesises completed computational work and methodology findings for critical conceptual HALE UAV design analysis.

### 6.1 Solar Irradiance Modelling Results

The solar irradiance model implements 24-hour continuous power prediction with dynamic cloud cover:

| Parameter | Value |
|-----------|-------|
| Solar Constant (S₀) | 1361 W/m² |
| Latitude | 47.38° (Zurich) |
| Day of Year | 172 (Summer Solstice) |
| Atmospheric Transmittance (ρ_at) | 0.7 |
| Cloud Cover Parameter (k_c) | 0.0–1.0 |

Three validation scenarios demonstrate model capability:
- **Ideal Clear Sky (k_c = 0.0):** Maximum power output, no cloud obstruction
- **Uniform Disturbance (k_c = 0.3):** Constant hazy/lightly overcast conditions
- **Dynamic Afternoon (k_c = 0.0→0.8):** Clear morning, storm passage 14:00–19:00

The cloud cover parameter k_c directly modifies the power state P_solar for the differential energy balance equation: dE_bat/dt = P_solar − P_out

![Solar Irradiance Model](./new_things/energy_management/solar_irradiance_model.png)

### 6.2 Propulsion Optimisation Results

Mission-based optimisation using Dantsker methodology [42] achieved significant power reduction:

| Metric | Baseline | Optimised | Improvement |
|--------|----------|-----------|-------------|
| Electrical Power (W) | 1994 | 1543 | 22.6% reduction |
| System Efficiency (%) | — | 58.6 | — |
| Propeller Efficiency (%) | — | 79.5 | — |
| Motor Efficiency (%) | — | 76.7 | — |
| ESC Efficiency (%) | — | 96.0 | — |

**Optimal Configuration:** HALE-Direct D80 motor + HALE-M 72×40 propeller at 1499 RPM

**Night Storage Impact:** 5.4 kWh (21.2%) reduction, saving 21.6 kg battery mass

![Propulsion Optimisation Results](./new_things/propulsion_optimisation/results/propulsion_optimisation_results.png)

### Top 10 Motor-Propeller Combinations

| Rank | Motor | Propeller | η_sys (%) | P_elec (W) | RPM | J | η_prop (%) | η_motor (%) |
|------|-------|-----------|-----------|------------|-----|---|------------|-------------|
| 1 | HALE-Direct D80 | HALE-M 72x40 | 58.6 | 1543 | 1499 | 0.487 | 79.5 | 76.7 |
| 2 | HALE-Direct D60 | HALE-ST 60x27 | 56.3 | 1606 | 2039 | 0.429 | 78.2 | 75.0 |
| 3 | HALE-Direct D80 | HALE-HP 72x54 | 56.1 | 1611 | 1346 | 0.542 | 84.4 | 69.2 |
| 4 | T-Motor U15 XXL | HALE-ST 48x22 | 54.4 | 1663 | 2993 | 0.365 | 70.2 | 80.7 |
| 5 | T-Motor U13 HALE | HALE-ST 40x18 | 53.4 | 1691 | 4144 | 0.317 | 63.3 | 87.9 |
| 6 | HALE-Direct D60 | HALE-M 60x33 | 52.3 | 1727 | 2024 | 0.432 | 73.2 | 74.4 |
| 7 | HALE-Direct D80 | HALE-UL 80x44 | 50.8 | 1780 | 1267 | 0.518 | 81.1 | 65.2 |
| 8 | T-Motor U15 XXL | HALE-M 48x28 | 50.2 | 1801 | 2971 | 0.368 | 65.2 | 80.2 |
| 9 | HALE-Direct D60 | HALE-HP 60x45 | 49.4 | 1831 | 1836 | 0.476 | 75.9 | 67.7 |
| 10 | T-Motor U15 XXL | HALE-HP 48x36 | 47.6 | 1897 | 2731 | 0.400 | 67.1 | 74.0 |

**Note:** 86 combinations were infeasible due to motor operating limits or insufficient thrust capacity.

### 6.3 Atmospheric Simulation Results

Full mission simulation at 20 km altitude validated the integrated framework:

| Metric | Value |
|--------|-------|
| **Mission Duration** | 24.0 hours |
| **Cruise Altitude** | 20 km |
| **Cruise Speed** | 25 m/s |
| **Average Temperature** | 216.6 K |
| **Average Density** | 0.08803 kg/m³ |
| **Peak Irradiance** | 2,863.1 W/m² |
| **Daylight Hours** | 14.4 hours |
| **Total Solar Energy** | 41,297 Wh |
| **Avg Power Required** | 558.5 W |
| **Max Power Required** | 560.2 W |
| **Avg Power Generated** | 2,864.2 W |
| **Peak Power Generated** | 5,039.0 W |
| **Final Energy Balance** | 27,893.2 Wh |
| **Energy Margin** | 208.1% |

ISA validation confirms atmospheric properties match ICAO standard tables within expected tolerance.

![Atmospheric Properties](./new_things/atmospheric_simulation/output/atmosphere.png)

![Solar Conditions](./new_things/atmospheric_simulation/output/solar.png)

![Aerodynamic Forces](./new_things/atmospheric_simulation/output/aerodynamics.png)

![Power Balance](./new_things/atmospheric_simulation/output/power.png)

![Energy Balance](./new_things/atmospheric_simulation/output/energy.png)

![HALE Simulation Dashboard](./new_things/atmospheric_simulation/output/hale_simulation_dashboard.png)

### 6.4 Aerodynamic Performance Assessment

High-aspect-ratio wings are essential for target L/D of 25–30. Literature shows consistent aspect ratios from 17.4 (EAV-3) to 30+ (Zephyr-class), with lower end more practical for manufacturing and ground handling [40].

Joined-wing configurations offer 1.4–1.5 span efficiency [20], significant advantage over conventional designs. However, structural complexity and wake interference require high-fidelity aeroelastic evaluation [44].

**Simulation Validation:** The atmospheric simulation computed L/D = 17.2 at 20 km cruise (C_L = 0.891, C_D = 0.0518), confirming steady cruise capability with lift balancing weight at 245.2 N against drag of 14.2 N [37].

| Parameter | Value |
|-----------|-------|
| Aircraft mass | 25.0 kg |
| Wing area | 10.0 m² |
| Air density | 0.08803 kg/m³ |
| Cruise speed | 25 m/s |
| Required CL | 0.891 |
| Drag coefficient | 0.0518 |
| Lift | 245.2 N (balances weight) |
| Drag | 14.2 N |
| L/D ratio | 17.2 |

Low cruise speeds (6–8 m/s for EAV-3) for optimal solar power present challenges: atmospheric disturbance sensitivity, larger control surfaces for authority, significant wing bending accommodated structurally [40].

### 6.5 Energy System Feasibility

Numerical validation demonstrates hybrid energy storage criticality. Night-time energy requirement (~23.9 kWh for 12-hour dark period) presents fundamental challenge:

- **Battery Solution**: At 250 Wh/kg, required mass ~95.7 kg—exceeding feasible limits for ~114 kg empty weight platform.
- **Hydrogen Fuel Cell**: At 33.3 kWh/kg (LHV) and 50% system efficiency, only 1.44 kg hydrogen required. Including tankage and balance-of-plant (3× multiplier), total ~4.3 kg—dramatic reduction versus batteries.

This aligns with literature: fuel cells outperform batteries above 2.8 kWh demand [10]. AtlantikSolar charge-margin methodology [39] provides robust multi-day operation framework.

### 6.6 Structural and Aeroelastic Considerations

CFRP composites essential for stiffness-to-weight ratios. EAV-3 demonstrates 404 mm wing bending at 1-G flight achievable with T-800 carbon fibre [40].

High-aspect-ratio very flexible wings introduce significant aeroelastic coupling. Conventional decoupled approach may underpredict flutter boundaries. UVLM-based methodology [44] provides accurate framework for wing-tail wake interference effects.

### 6.7 Photovoltaic Integration Challenges

Łopusiewicz and Książek [43] practical challenges must be factored:

1. **Micro-cracking**: Aerodynamic loading causes stress concentrations leading to efficiency reduction.
2. **Galvanic isolation**: Carbon-fibre substrates require proper isolation to prevent short-circuiting.
3. **Manufacturing defects**: Electroluminescence reveals 5–10% cell defects requiring quality control.
4. **Efficiency degradation**: Wing bending reduces photovoltaic output.

Conservative 10–15% derating factor recommended for theoretical solar power calculations.

### 6.8 Comparison with Established Platforms

Table 1 presents the conceptual design against established HALE platforms.

| Platform | Mass (kg) | Wingspan (m) | Aspect Ratio | Endurance |
|----------|-----------|--------------|--------------|-----------|
| Zephyr S | 53 | 25 | 24 | 25+ days |
| Helios | 730 | 75 | 30 | 14+ hours |
| EAV-3 | 53 | 19.5 | 17.4 | Stratospheric test |
| AtlantikSolar | 6.9 | — | — | 81 hours |
| **Present Design** | ~114 (airframe) | 32 | ~30 | Target: 24+ hours |

Design targets align with literature benchmarks; hybrid energy storage provides practical multi-day endurance pathway.

---

## 7. Conclusion and Future Work

The study indicates technical feasibility and multidisciplinary complexity in conceptual design of a HALE UAV powered by renewable energy. Implemented computational models establish the framework for performance analysis:

1. **Solar irradiance modelling** provides 24-hour power prediction with cloud cover dynamics, enabling meteorological risk assessment for mission planning.
2. **Propulsion optimisation** achieves 22.6% power reduction through mission-based motor-propeller selection, directly reducing night-time storage requirements.
3. **Atmospheric simulation** validates 24-hour mission capability with 208.1% energy margin, confirming perpetual endurance potential.

Numerical evaluation suggests realistic power demands (~2 kW electrical) with high-altitude solar flux and triple-junction GaAs providing ~9 kW usable power. Night-time storage (~23.9 kWh) makes pure lithium-ion batteries infeasible (~95 kg); hydrogen fuel-cell storage meets requirements at <5 kg.

### 7.1 Future Work

#### Multi-Domain Coupling
- Integrate solar, propulsion, and atmospheric models into unified simulation framework
- Implement real-time energy management with charge-margin methodology [39]

#### Multi-Point Optimisation
- Extend beyond cruise-only analysis to climb, descent, and loiter segments
- Incorporate wind profile and thermal modelling

#### High-Fidelity Modelling
- CFD validation under low-Reynolds-number conditions
- Aeroelastic flutter analysis using Murua methodology [44]
- BEMT propeller design for HALE-specific operating conditions

#### Thermal Modelling
- Battery and avionics thermal management at stratospheric temperatures (−60°C)
- Solar cell temperature degradation effects

#### Flight Validation
- Scaled demonstrator fabrication for experimental validation
- Prototype testing of hybrid energy storage systems

#### Emerging Technologies
- Morphing wings for adaptive flight optimisation
- Solid-state battery integration
- Ultra-light flexible solar arrays (perovskite)
- Supercapacitor storage for battery-free architectures [45]

---

## 8. References

### Original Citations

[1] Goraj, Z., Frydrychiewicz, A., & Winiecki, J. (1999). Design concept of a high-altitude long-endurance unmanned aerial vehicle. *Aircraft Design*, 2(1), 19–44. https://doi.org/10.1016/S1369-8869(99)00014-4

[2] Goraj, Z. (2004). High altitude long endurance unmanned aerial vehicle of a new generation – A design challenge for a low cost, reliable and high performance aircraft. *Bulletin of the Polish Academy of Sciences, Technical Sciences*, 52(3), 173–194.

[3] Romeo, G., Frulla, G., Cestino, E., & Corsino, G. (2004). HELIPLAT: Design, aerodynamic, structural analysis of long-endurance solar-powered stratospheric platform. *Journal of Aircraft*, 41(6), 1505–1520. https://doi.org/10.2514/1.6713

[4] Najafi, Y. (2011). *Design of a High Altitude Long Endurance Solar Powered UAV: Solar Powered Aerial Communicator (SPACOM)*. MS Thesis, San Jose State University.

[5] ANSYS Inc. (2024). *ANSYS Workbench User Guide*. Canonsburg, PA.

[6] Anderson, J. D. (2017). *Fundamentals of Aerodynamics* (6th ed.). McGraw-Hill.

[7] Bertin, J. J., & Cummings, R. M. (2014). *Aerodynamics for Engineers* (6th ed.). Pearson.

[8] Daniel, I. M., & Ishai, O. (2006). *Engineering Mechanics of Composite Materials* (2nd ed.). Oxford University Press.

[9] Jones, R. M. (1999). *Mechanics of Composite Materials* (2nd ed.). Taylor & Francis.

[10] Boukoberine, M. N., Zhou, Z., & Benbouzid, M. (2019). A comparative review of electric and hybrid energy storage systems for UAVs: Configurations, challenges, and optimal dimensioning. *Journal of Power Sources*, 613, 234860. https://doi.org/10.1016/j.jpowsour.2019.234860

[11] Hassanalian, M., & Abdelkefi, A. (2017). Classifications, applications, and design challenges of unmanned aerial vehicles: A review. *Progress in Aerospace Sciences*, 91, 99–131. https://doi.org/10.1016/j.paerosci.2017.01.001

[12] Nelson, R. C. (1998). *Flight Stability and Automatic Control* (2nd ed.). McGraw-Hill.

[13] Cook, M. V. (2013). *Flight Dynamics Principles* (3rd ed.). Elsevier.

[14] Green, M. A., Hishida, Y., & Dunlop, E. D. (2021). Solar cell efficiency tables (Version 58). *Progress in Photovoltaics: Research and Applications*, 29(7), 1–15.

[15] Yamaguchi, M., Takamoto, T., Araki, K., & Ekins-Daukes, N. (2006). Multi-junction III–V solar cells: Current status and future potential. *Solar Energy*, 80(8), 1040–1047.

[16] Noor, A. K., Venneri, S. L., Paul, D. B., & Hopkins, M. A. (2000). Structures technology for future aerospace systems. *Computers & Structures*, 78(1–3), 5–19.

[17] Austin, R. (2010). *Unmanned Aircraft Systems: UAVS Design, Development and Deployment*. Wiley.

[18] Panagiotou, P., Tsavlidis, L., & Kyriazis, N. (2018). Conceptual design of a blended wing body MALE UAV. *Aerospace Science and Technology*, 78, 640–651. https://doi.org/10.1016/j.ast.2018.05.007

[19] Wang, Z., Zhuang, M., & Shao, W. (2018). Conceptual design of solar-powered high-altitude long-endurance UAV. *Chinese Journal of Aeronautics*, 31(8), 1634–1647. https://doi.org/10.1016/j.cja.2018.05.016

[20] Wolkovitch, J. (1986). The joined wing: An overview. *Journal of Aircraft*, 23(2), 161–178. https://doi.org/10.2514/3.45283

[21] Livne, E. (2003). Airplane aeroelasticity: From the pioneers to the future challenges. *Journal of Aircraft*, 40(6), 983–997. https://doi.org/10.2514/2.6945

[22] Wright, J. R., & Cooper, J. E. (2007). *Introduction to Aircraft Aeroelasticity and Loads*. Wiley.

[23] Scholz, D. (1998). Aircraft systems—Integration of avionics. In *Aeronautical Engineering* (pp. 123–145). Wiley.

[24] Larminie, J., & Dicks, A. (2003). *Fuel Cell Systems Explained* (2nd ed.). Wiley.

[25] Fuel Cell Technologies Office. (2017). *Fuel Cell Technologies Market Report*. U.S. Department of Energy.

[26] Livne, E. (2003). Future of airplane aeroelasticity. *Journal of Aircraft*, 40(6), 1066–1092. https://doi.org/10.2514/2.6946

[27] Roskam, J. (1985). *Airplane Design: Part IV: Preliminary Calculation of Aerodynamic, Thrust and Power Characteristics*. DARcorporation.

[28] Colozza, A. J., & Dolce, J. L. (2003). *High-Altitude, Long-Endurance Airships for Coastal Surveillance*. NASA Glenn Research Center.

[29] Noll, T. E., Brown, J. M., Perez-Davis, M. E., & Ishmael, S. D. (2004). Investigation of the Helios Prototype Vehicle Mishap. *NASA Mishap Report*.

[39] Oettershagen, P., Melzer, A., Faust, T., Hakenberg, R., & Siegwart, R. (2017). Design of solar-powered UAVs for endurance flight. *Journal of Field Robotics*, 34(2), 291–311. https://doi.org/10.1002/rob.21669

[40] Hwang, J., Lee, D., & Kim, S. (2016). Aerodynamic design of solar-powered high-altitude long-endurance UAV. *Journal of Aircraft*, 53(5), 1291–1303. https://doi.org/10.2514/1.C033371

[41] Mermer, S., & Özgen, S. (2017). Conceptual design of hybrid turbofan/solar powered HALE UAV. In *7th European Conference for Aeronautics and Space Sciences (EUCASS)*. Milan, Italy.

[42] Dantsker, O. D., Cale, T. G., & Xiao, M. (2020). Propulsion system design and optimization for solar-powered UAVs. In *AIAA Propulsion and Energy Forum*. Virtual Event.

[43] Łopusiewicz, Ł., & Książek, I. (2024). Integration of photovoltaic cells on composite wing structures for solar-powered UAVs. In *ICAS 2024 Proceedings*. Florence, Italy.

[44] Murua, J., Quintana, P., & Claridge, M. (2011). Stability and open-loop dynamics of very flexible aircraft including wake interference. In *AIAA Atmospheric Flight Mechanics Conference*. Portland, OR.

[45] Liller, K., Winkler, J., Peters, S., Gerngross, T., & Bruckmann, T. (2025). Battery-free solar UAV with supercapacitor energy storage. *Scientific Reports*, 15, 90729. https://doi.org/10.1038/s41598-025-90729-4

[46] ITB Study (Academia.edu). (n.d.). Power density and specific power of monocrystalline silicon cells in HALE UAV applications.

[47] UST Solar Tech Review. (n.d.). Comparative analysis of CIGS thin-film solar photovoltaics for UAVs.

[48] BAE Systems. (2024). PHASA-35 Stratospheric Flight Status and Capabilities. Wikipedia.

[49] Johannes Kepler University Linz. (2024). Quasi-2D perovskite solar cells for ultra-lightweight applications. *Nature Energy*, DOI:10.1038/s41560-024-01500-2.

[50] MIT News. (2022). Printed organic photovoltaic cells for ultra-light surface lamination.

[51] PMC/Energies. (n.d.). Lamination and integration of flexible solar cells into composite wing structures.

[52] SAE Mobility Engineering Technology. (n.d.). Designed-in photovoltaic integration with zero net weight addition.

[53] MDPI Energies. (2025). Aerodynamic and energetic review of high-aspect-ratio HALE platforms.

[54] Abdulrahman, M., et al. (2025). Comprehensive review of renewable power systems for UAVs. *Sustainable Energy Technologies and Assessments (SETA)*, DOI:10.1016/j.seta.2024.104150.

[55] ScienceDirect EMS Study. (n.d.). Sensitivity analysis of energy management strategies for solar-powered aircraft.

[56] Unmanned Systems Technology. (2025). XSun and H3 Dynamics hybrid multi-source power architecture.

[57] American Institute of Aeronautics and Astronautics. (2022). Mathematical thermal models for DLR HAP program stratospheric batteries. *AIAA 2022-3271*.

[58] IntechOpen. (2025). DC-DC converter topologies and applications in solar UAVs.

[59] EPJ Web of Conferences. (2025). Real-time execution of P&O MPPT with cascaded DC-DC prototype. *CISTEM 2024*.

[60] Springer Nature; IJAAS. (2025/2026). Machine learning-based MPPT algorithms under rapid irradiance changes.

[61] Vicor Power. (n.d.). HALE UAVs case study: Discontinued Conduction Mode power modules.

[62] Oregon State University. (n.d.). Review of high-voltage electrical power distribution systems in UAVs.

[63] Turin Polytechnic SHAMPO Program. (2006). Parametric studies and structural optimization for HALE platforms.

[64] Romeo, G., et al. (2008). Bearing strength of bolted CFRP joints in HALE UAV wing fittings.

[65] ScienceDirect. (n.d.). FDM-fabricated ABS/CFRP sandwich structures for aerospace components.

[66] ResearchGate. (2024–2025). Generative modelling for ultralight highly flexible aircraft structural design.

[67] International Journal of Aerospace Engineering. (2025). Structural design and characteristics of a HALE joined-wing configuration UAV. *Wiley*, DOI:10.1155/ijae/9931529.

[68] Nature Scientific Reports. (2023). Multidisciplinary Design Optimization with eco-material selection for HALE UAVs.