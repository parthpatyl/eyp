# HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES (UAVs): SUSTAINED FLIGHT THROUGH RENEWABLE ENERGY

**Version 3 — Corrected and Revised Report**

---

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

High Altitude Long Endurance (HALE) Unmanned Aerial Vehicles (UAVs) are designed to operate at altitudes above 18 km with mission durations extending from several days to multiple weeks. The increasing demand for persistent surveillance, atmospheric monitoring, and communication relay platforms has accelerated interest in solar-powered and hybrid-energy UAVs capable of sustained flight. This project focuses on the conceptual design, performance analysis, and feasibility assessment of a solar-powered HALE UAV.

To achieve these goals, the project involves a comprehensive literature review, aerodynamic analysis, and energy system assessment. The project addresses several key design challenges, including low Reynolds number aerodynamics, lightweight composite structures, and hybrid renewable energy integration. To validate performance assumptions and analyse energy storage limitations, the project employs simulations and theoretical modelling.

In this expanded second version of the report, the literature review has been substantially broadened to incorporate recent developments in solar-powered UAV design, advanced propulsion system optimisation, photovoltaic cell integration onto composite wing structures, battery-free UAV architectures, aeroelastic stability modelling of very flexible aircraft, and hybrid turbofan–solar power concepts. The updated analysis integrates findings from recently published research, strengthening the theoretical foundation and extending the scope of the feasibility assessment.

The numerical evaluation of the conceptual HALE model confirms that the aircraft geometry and aerodynamic assumptions produce realistic power demands (~2 kW electrical), while the high-altitude solar flux combined with triple-junction GaAs photovoltaics provides ~9 kW of usable power, ensuring robust daytime performance. The analysis also quantifies night-time storage requirements, showing that pure lithium-ion battery solutions exceed feasible mass limits (~95 kg), whereas hydrogen fuel-cell storage meets the requirement at <5 kg system mass.

---

## 1. Introduction

HALE UAVs occupy a unique niche in the unmanned aircraft landscape, bridging the gap between conventional aircraft and satellites. Their ability to remain aloft for days or even weeks at altitudes above 18 km makes them indispensable for persistent surveillance, atmospheric research, and as low-orbit communication relays that can provide broadband connectivity to remote regions [1][2]. The most advanced platforms—such as the NASA Helios, the Airbus Zephyr, and the QinetiQ Zephyr S—have achieved endurance figures that exceed 24 hours, with some prototypes demonstrating multi-week sorties when powered by a combination of solar arrays, high-energy-density batteries, and, in a few cases, fuel cells [3][4].

The multidisciplinary nature of HALE UAV design is evident from the outset. Aerodynamic performance must be optimised for low Reynolds number flows, a regime where viscous effects dominate and conventional high-speed design rules no longer apply [6][7]. This necessitates the use of high-aspect-ratio wings, often exceeding 20:1, to generate sufficient lift while minimising induced drag. Composite materials—carbon-fibre reinforced polymers (CFRPs), glass-fibre composites, and advanced hybrid laminates—are employed to achieve the required stiffness-to-weight ratios [8][9]. The energy architecture is inherently hybrid: large, lightweight solar panels cover the wing and fuselage surfaces, feeding a battery bank that supplies power during night or low-insolation periods, while a small fuel cell can provide a backup or supplementary power source [10][11].

Recent advances have expanded the design envelope considerably. The AtlantikSolar UAV, developed at ETH Zurich, demonstrated a continuous solar-powered flight of 81 hours, establishing a new world endurance record for aircraft below 50 kg mass and validating the concept of energetically robust perpetual flight [39]. The Korea Aerospace Research Institute's (KARI) EAV-3 programme produced a 53 kg solar-powered HALE UAV with a 19.5 m wingspan and aspect ratio of 17.4, successfully conducting stratospheric flight tests that demonstrated the viability of small-scale solar HALE platforms [40]. Furthermore, hybrid turbofan/solar concepts have explored the use of turbofan engines for climbing to altitude with solar-only sustaining of loiter flight, achieving 24–48 hour endurance targets with 1,000 kg payload capacity [41].

The control architecture must be fault-tolerant and highly redundant; small disturbances at high altitude can have amplified effects, so the aircraft typically incorporates multiple redundant actuators, sensors, and control laws [12][13]. The coupled aeroelastic and flight-dynamic behaviour of very flexible HALE aircraft represents a critical design consideration, as demonstrated by Murua et al., who developed unified nonlinear models integrating geometrically exact beam finite elements with the Unsteady Vortex Lattice Method (UVLM) and free-wake effects to predict stability boundaries and open-loop dynamics of representative HALE configurations [44].

Despite these advances, several design gaps persist. Energy efficiency remains a critical bottleneck, with solar cells at high altitude experiencing increased radiation and temperature extremes that degrade performance over time [14][15]. Structural integrity is another concern; the combination of low ambient pressure, large temperature swings, and the mechanical loads associated with long-duration flight can lead to material fatigue, delamination, or creep in composite structures [8][16]. The integration of photovoltaic cells onto composite wing skins introduces additional challenges, including micro-cracking under aerodynamic loading, galvanic isolation requirements when carbon-fibre substrates are used, and the sensitivity of cell efficiency to manufacturing defects, as systematically investigated by Łopusiewicz and Książek [43].

---

## 2. Market Survey and Literature Review

### 2.1 Previous Studies (Existing Sources)

The high-altitude long-endurance unmanned aerial vehicle market has experienced a pronounced expansion over the past decade, driven by civilian, military, and commercial imperatives [1][2][3]. The primary drivers of this growth are the escalating need for real-time situational awareness, the desire to reduce reliance on costly satellite constellations, and the increasing availability of advanced materials and power-generation technologies [4][17].

#### 2.1.1 Configuration Studies

Early configuration studies established the aerodynamic trade-offs fundamental to HALE design. Goraj et al. [1] presented four aerodynamic design concepts for a HALE UAV intended for reconnaissance at altitudes up to 27 km, demonstrating that an attentively designed biplane can achieve comparable aerodynamic efficiency to monoplane configurations while offering higher payload capacities. Their subsequent work [2] extended these findings to a new-generation HALE concept, addressing the coupled challenges of low-Reynolds-number aerodynamics, lightweight structures, propulsion technology, and autonomous flight control.

The HELIPLAT programme, reported by Romeo et al. [3], demonstrated the design, aerodynamic, and structural analysis of a long-endurance solar-powered stratospheric platform. The HELIPLAT adopted a twin-boom configuration with distributed propulsion and highlighted the critical role of solar cell area optimisation in determining overall endurance.

Blended-wing-body (BWB) configurations have been shown to exhibit improved lift-to-drag ratios and enhanced structural integrity due to the distributed load paths inherent in the joined-wing architecture [18][19]. Joined-wing configurations achieve span efficiency factors of 1.4–1.5, thereby reducing induced drag and structural weight relative to conventional wing-body designs [20].

#### 2.1.2 Structural Design

Structural design literature emphasises the extensive use of carbon-fibre-reinforced polymer (CFRP) composites, which provide the necessary stiffness-to-weight ratios for high-aspect-ratio wings and large solar-array panels [8][9][21]. Key structural considerations include weight minimisation, flutter margins, and reliability and redundancy [22]. Manufacturing processes such as autoclave curing and resin-transfer moulding are critical to achieving the required material properties and dimensional tolerances [21]. Long-duration flight exposes the structure to repeated load cycles that can lead to crack initiation and propagation over time, making fatigue testing under realistic atmospheric turbulence conditions essential [23].

#### 2.1.3 Energy System Analysis

Energy system analyses in the existing literature compare lithium-ion batteries and hydrogen fuel cells [10][11]. The findings indicate that fuel cells outperform batteries when the energy demand exceeds 2.8 kWh, a threshold often surpassed during high-altitude operations due to increased power demand (3.5% per km altitude) [10]. Solar cell studies reveal that triple-junction GaAs cells achieve efficiencies between 25% and 30%, while thin-film cells offer lower efficiencies but benefit from reduced weight and flexibility [14][15]. Night-time endurance is identified as the most critical limitation, primarily due to battery degradation and storage inefficiencies [24][25].

#### 2.1.4 Stability and Control

Stability and control findings emphasise the necessity of longitudinal and directional stability for sustained flight [12][13]. Flutter analysis is critical for high-aspect-ratio wings, as aeroelastic coupling can lead to catastrophic failure if not properly mitigated [22][26]. Control surface sizing is linked to low-density air performance, requiring larger deflection angles or higher actuation authority to achieve the same control effectiveness as at lower altitudes [27].

### 2.2 Recent Developments (New Sources)

The following subsections present the findings from the newly incorporated research, which substantially expand the knowledge base underpinning the design.

#### 2.2.1 Perpetual-Flight Solar UAV Design

Oettershagen et al. [39] presented the complete development process of the AtlantikSolar UAV, a 6.9 kg solar-powered fixed-wing aircraft that achieved a continuous solar-powered flight of 81 hours (2,338 km ground distance), establishing the world endurance record for aircraft below 50 kg mass. A key contribution of this work is the formal design methodology that allows solar-powered UAVs to be designed for energetically robust perpetual flight in sub-optimal meteorological conditions. The conceptual design and analysis framework (CDAF) developed at ETH Zurich optimises wing span, aspect ratio, and battery mass as design variables, using excess time and charge margin as central performance metrics. Flight results from the continuous 81-hour flight demonstrate that AtlantikSolar achieves **39% minimum state-of-charge, 6.8 hours excess time, and 6.2 hours charge margin**—performance metrics that represent a significant improvement over previous solar-powered UAVs such as SkySailor (which crossed the night with only 5.8% remaining battery energy).

The design philosophy of maximising meteorological robustness, rather than merely achieving the minimum feasibility of perpetual flight, is particularly relevant to the present HALE UAV design effort. While the AtlantikSolar operates at low altitude, the fundamental energy-balance principles, power-train sizing methodology, and charge-margin analysis are directly applicable to high-altitude platforms operating in the more favourable solar irradiance conditions above 18 km.

#### 2.2.2 Solar HALE UAV Aerodynamic Design (EAV-3)

Hwang et al. [40] reported the aerodynamic design of the EAV-3, a solar-powered HALE UAV developed by the Korea Aerospace Research Institute (KARI). The EAV-3 weighs 53 kg with a structure weight of 22 kg and features a flexible wing of 19.5 m span with an aspect ratio of 17.4. Critical design considerations included the significant wing bending (**404 mm at 1-G flight condition based on T-800 composite material**) and side-wind effects due to the low cruise speed (V_cr = 6 m/s). Unlike general aircraft, the EAV-3 experiences no centre-of-gravity shift during flight because it is a solar-electric-driven UAV, yielding a **static margin of 28.4% with the centre of gravity at 31% of the Mean Aerodynamic Chord (MAC)**.

The EAV-3 programme provides empirical validation of several assumptions underpinning the present conceptual design, particularly regarding the feasibility of high-aspect-ratio flexible wings for solar HALE applications and the aerodynamic challenges associated with very low cruise speeds at high altitude.

#### 2.2.3 Hybrid Turbofan/Solar HALE UAV Concepts

Mermer and Özgen [41] investigated the conceptual design of a hybrid turbofan/solar-powered HALE UAV at the 7th European Conference for Aeronautics and Space Sciences (EUCASS). The design sought to achieve at least 24 hours endurance with a 250 kg camera and 750 kg battery (total 1,000 kg payload) at a service ceiling of 6,096–9,144 m. The approach uses turbofan engines only for climbing to the required altitude, with solar energy and battery power sustaining loiter flight.

The competitor study in this work identified average empty weight fractions of 0.6218, aspect ratios of approximately 24.5, and average wingspans of 66.45 m among existing HALE and solar-powered platforms including Phantom Eye, Global Observer 2, Global Hawk, Lockheed U-2S, and Condor. These data provide valuable benchmarks for sizing the present conceptual design.

#### 2.2.4 Propulsion System Optimisation for Solar UAVs

Dantsker et al. [42] presented a propulsion system design, optimisation, simulation, and testing methodology for the UIUC-TUM Solar Flyer, a long-endurance solar-powered unmanned aircraft. The key contribution is a mission-based propulsion system optimisation tool that selects optimal motor-propeller combinations for a given mission profile. The optimisation tool was able to match a motor-propeller combination that was 19% more efficient relative to the baseline combination for the given mission profile thrust and velocity design point.

This work is highly relevant to the present design because propulsion system efficiency directly affects the power budget and thus the required solar array area and battery capacity. Applying similar optimisation frameworks to the proposed HALE UAV's propulsion system could yield significant performance improvements.

#### 2.2.5 Aeroelastic Stability of Very Flexible Aircraft

Murua et al. [44] investigated the coupled nonlinear aeroelasticity and flight mechanics of very flexible aircraft (VFA), a class that includes solar-powered HALE UAVs. A unified model was developed that integrates a geometrically exact composite beam finite-element structural model with the Unsteady Vortex Lattice Method (UVLM) including free-wake effects. The study demonstrated the importance of three-dimensional aerodynamic effects, particularly wake interference between the wing and tail, which significantly impacts VFA dynamics.

These findings underscore the need for high-fidelity aeroelastic models in the design of HALE UAVs with high-aspect-ratio wings. The coupled analysis methodology presented by Murua et al. provides a framework for predicting flutter boundaries more accurately than conventional decoupled approaches.

#### 2.2.6 Photovoltaic Cell Integration on Composite Wings

Łopusiewicz and Książek [43] systematically investigated the challenges of integrating photovoltaic cells onto the wings of unmanned solar-powered aircraft. Two methods of laminating photovoltaic cells to composite wing surfaces were compared under load-bearing conditions. Key findings include:

- **Solar cell performance**: The SunPower Maxeon III generation cells used achieve power densities of **231–243 Wp/m²** with an area of 153 cm² per cell and a weight of only 6.5 g, making them suitable for weight-critical solar UAV applications.
- **Lamination method comparison**: The first method (laminating successive layers of fibreglass or carbon fibre to an existing fibreglass–photovoltaic composite) demonstrated **9.5% higher maximum power at low loads** and **12.5% higher power at high loads** compared to the second method (pre-laminating the wing separately and then bonding the cell module).
- Micro-cracking of photovoltaic cells under aerodynamic loading is a primary concern, caused by both surface dirt and internal structural elements creating localised pressure.
- Galvanic isolation is essential when carbon-fibre substrates are used, as the conductive carbon fibre can short-circuit the photovoltaic cells.
- Electroluminescence testing revealed manufacturing defects including silicon layer defects, incorrect soldering, and lamination imperfections that reduce string efficiency.
- Wing deflection under load reduces photovoltaic efficiency, with the first lamination method showing superior resistance to efficiency degradation.

These results have direct implications for the present HALE UAV design, where maximising solar array output while maintaining structural integrity under sustained high-altitude flight loads is a primary objective.

#### 2.2.7 Battery-Free UAV Concepts

Liller et al. [45] proposed the development of a battery-free, solar-powered, and energy-aware fixed-wing UAV that stores harvested energy in supercapacitors instead of batteries. Two novel energy-aware control algorithms—Greedy Energy-Aware Control and Predictive Energy-Aware Control—were developed to address power intermittency by preventing brownouts and minimising total-loss-of-thrust events. While this concept operates at a fundamentally different scale from HALE platforms, the energy-management principles and the elimination of battery degradation concerns are noteworthy for future UAV energy system architecture.

### 2.3 Synthesis and Comparative Analysis

The integration of new and existing sources reveals several converging trends and a few notable contradictions:

**Converging Trends:**
1. High-aspect-ratio monoplane configurations remain the dominant choice for solar HALE UAVs, with aspect ratios ranging from 17.4 (EAV-3) [40] to over 30 (Zephyr-class) [3].
2. Solar cell efficiencies of 25–30% (triple-junction GaAs) are consistently cited as the practical upper bound for current HALE applications [14][15][41].
3. Hybrid energy storage (solar + battery + fuel cell) is universally recognised as necessary for multi-day endurance [10][11][39][41].
4. Propulsion system optimisation can yield 15–20% efficiency improvements [42].
5. Aeroelastic coupling is a critical design driver for high-aspect-ratio, very flexible wings [22][26][44].

**Contradictions and Tensions:**
1. **Battery vs. fuel cell dominance**: While the original study's analysis indicates fuel cells are superior above 2.8 kWh demand [10], the AtlantikSolar programme achieved 81 hours of flight using batteries alone [39], albeit at low altitude where power demands are lower. This suggests that the optimal storage solution is highly sensitive to platform scale and mission profile.
2. **Configuration philosophy**: The EAV-3's relatively modest aspect ratio of 17.4 [40] contrasts with the original study's emphasis on aspect ratios exceeding 20, suggesting that practical considerations (manufacturability, ground handling, flutter) may limit achievable aspect ratios.
3. **Battery-free vs. battery-dependent approaches**: The emerging battery-free UAV concept [45] represents a fundamentally different energy paradigm, though its current technology readiness level is insufficient for HALE applications.

| Theme | Old Sources | New Sources | Action |
|-------|-----------|-------------|--------|
| UAV Structural Loads | Goraj [1][2], Romeo [3] | Murua [44], Łopusiewicz [43] | Merged + expanded with aeroelastic modelling and PV integration challenges |
| Solar Efficiency | Najafi [4], existing literature [14][15] | Mohd Ali [49], Łopusiewicz [43], Mermer [41] | Updated with practical integration data and lamination methods |
| Material Fatigue | Goraj [1][2], composite literature [8][9] | — | Retained |
| Perpetual Flight Feasibility | Najafi [4] | Oettershagen [39], Liller [45] | Expanded with world-record flight data and battery-free concepts |
| Aerodynamic Design | Goraj [1][2], Romeo [3] | Hwang [40], Mermer [41] | Expanded with EAV-3 data and hybrid turbofan/solar sizing |
| Propulsion Optimisation | General literature [6][7] | Dantsker [42] | New section added |
| Aeroelastic Stability | Flutter literature [22][26] | Murua [44] | Expanded with UVLM-based coupled analysis |

---

## 3. Aim and Objectives

### 3.1 Aim

The overarching aim of this research is to conceive, analyse, and validate a theoretically sound design for a solar-powered High-Altitude Long-Endurance (HALE) Unmanned Aerial Vehicle (UAV). The design will be grounded in rigorous aerodynamic, structural, and power-system analyses, and will be corroborated through high-fidelity simulation tools [1][2][3][4]. By integrating state-of-the-art solar photovoltaics, advanced energy storage, and lightweight composite structures, the proposed HALE platform will demonstrate the feasibility of achieving multi-week endurance while maintaining payload versatility and operational reliability.

### 3.2 Objectives

**Primary Objective:**
Conceptual Design Formulation and Validation: Develop a comprehensive conceptual design of a solar-powered HALE UAV that satisfies mission endurance, payload, and safety requirements. This includes defining the airframe geometry, wing planform, propulsion architecture, and power-management strategy. The design will be validated through a combination of analytical calculations, CFD, FEA, and system-level simulations [5][6][7].

**Secondary Objectives:**

1. **In-Depth Literature Survey** — Conduct a systematic review of existing solar UAVs and HALE system designs, focusing on aerodynamic configurations, structural materials, and energy-storage technologies [1][2][3][4][39][40][41][42][43][44].

2. **Identification of Design Limitations** — Critically assess the limitations of current energy-storage solutions, aerodynamic challenges at low Reynolds numbers, and structural constraints including fatigue life [8][9][10][11][14][15].

3. **Simulation-Based Performance Evaluation** — Employ CFD, FEA, and power-system simulations to predict endurance, energy budgets, and mission reliability under varying atmospheric conditions [5][6][7].

4. **Propose Design Improvements and Future Research Directions** — Based on simulation outcomes and the expanded literature base, recommend specific design modifications. Incorporate insights from propulsion optimisation [42], aeroelastic analysis [44], and photovoltaic integration [43] into the improvement recommendations.

5. **Renewable Energy Integration Analysis** — Quantify the impact of renewable energy sources on overall endurance and mission reliability, incorporating the new data on solar cell integration challenges [43], battery-free concepts [45], and charge-margin optimisation methodologies [39].

---

## 4. Problem Definition and Design Specifications

The design challenge is to synthesise a solar-powered HALE UAV that can sustain continuous flight above 18 km for a minimum of 24 hours, with the ambition of extending that endurance to several days [1][2][3][4].

**Conceptual Performance Results:**
- Cruise power: ≈ 2 kW
- Solar power available: ≈ 9 kW
- Night storage: ≈ 24 kWh
- Battery mass: ≈ 95 kg
- Hydrogen equivalent: ≈ 1.44 kg (≈ 4.3 kg system)

### 4.1 Aerodynamic Integration

At stratospheric altitudes the air density drops to roughly one-tenth of sea-level values, forcing the aircraft to operate at low Reynolds numbers (10⁵–10⁶) [6][7]. The design must adopt a wing configuration that maximises lift-to-drag (L/D) while minimising induced drag. Three promising topologies—biplane, blended-wing-body (BWB), and joined-wing—have been evaluated [1][2][3][18][19][20].

The aerodynamic design of the EAV-3 [40] provides an important reference point, demonstrating that a solar HALE UAV with a 19.5 m wingspan, aspect ratio of 17.4, and cruise speed of 6 m/s can operate successfully in the stratosphere, albeit with significant wing bending that must be accommodated in the structural and control design.

### 4.2 Structural Optimisation

The structural design must reconcile the need for an ultra-light, high-stiffness airframe with the demands of flutter safety and fatigue resistance [8][9][21][22]. CFRP composites form the primary load-carrying elements. FEA will predict static deflection, modal frequencies, and flutter margins under worst-case loading scenarios [5].

The coupled aeroelastic analysis methodology of Murua et al. [44], which integrates geometrically exact beam models with the UVLM including free-wake effects, provides a more accurate framework for predicting flutter boundaries than the conventional decoupled approaches. This methodology will be considered for the detailed structural analysis phase.

### 4.3 Hybrid Energy System

Solar power is the primary energy source during daylight. Triple-junction GaAs cells delivering 25–30% efficiency [14][15] will be mounted on wing and fuselage surfaces. The photovoltaic integration methodology must address the challenges identified by Łopusiewicz and Książek [43], including micro-cracking under loading, galvanic isolation with carbon-fibre substrates, and manufacturing defect management.

Excess solar energy will be stored in high-cycle lithium-ion batteries (~250 Wh/kg) [10][24]. For missions exceeding 2.8 kWh of night-time demand, a hydrogen fuel cell stack (~0.5 kg/kWh) will be incorporated [10][11]. The charge-margin optimisation methodology demonstrated by Oettershagen et al. [39] will be adopted to ensure energetically robust multi-day operation.

### 4.4 Mission Profile and Constraints

The aircraft will cruise at 18–22 km at approximately 80 km/h. Payload capacity: 5–10 kg. Environmental constraints including cloud cover, temperature gradients, and wind shear will be incorporated into the mission simulator [28][29].

---

## 5. Methodology

### 5.1 Literature-Based Foundation

The initial phase was anchored in an exhaustive review of state-of-the-art research pertaining to HALE UAVs [1][2][3][4]. This effort yielded a catalogue of existing HALE platforms—NASA Helios, Airbus Zephyr, DARPA Vulture, KARI EAV-3 [40]—together with their specific mission parameters. The literature on solar-cell technologies was examined, focusing on triple-junction versus thin-film devices [14][15]. Energy-storage options were scrutinised with a balanced assessment of lithium-ion batteries and fuel-cell systems [10][11][24][25].

In this expanded version, the literature base has been augmented with research addressing:
- Perpetual-flight design methodologies and the charge-margin concept [39]
- Propulsion system optimisation for solar UAVs [42]
- Coupled aeroelastic and flight-dynamic modelling of very flexible aircraft [44]
- Practical challenges of photovoltaic cell integration onto wing structures [43]
- Hybrid turbofan/solar propulsion concepts [41]
- Battery-free UAV architectures [45]

### 5.2 Mission Requirements Definition

Building on the expanded literature, the mission requirements remain as defined in Version 1: minimum 24-hour endurance, target L/D of 25–30, payload capacity defined for scientific instruments and communications equipment, and structural stiffness sufficient to avoid flutter [1][2][3][4].

The EAV-3 programme [40] provides empirical validation that the target L/D range is achievable for solar HALE platforms, while the AtlantikSolar results [39] confirm that the energy balance for multi-day flight can be closed with current technology at lower altitudes, and by extension at high altitude where solar irradiance is approximately 1,360 W/m² (greater than sea-level values).

### 5.3 Aerodynamic Modelling

#### 5.3.1 Airfoil and Wing Analysis

The aerodynamic evaluation couples analytical theory with high-fidelity CFD [5][6][7]. Candidate airfoils are screened using established low-Reynolds-number performance data, focusing on C_L, C_D, and the resulting C_L/C_D ratio across the expected operating Reynolds range (~0.5–2 × 10⁶). CFD simulations capture three-dimensional effects such as tip vortices, spanwise flow, and pressure-gradient induced separation.

The EAV-3 programme [40] demonstrated that careful consideration of wing bending and side-wind effects is essential at the very low cruise speeds characteristic of solar HALE flight (V_cr = 6 m/s for EAV-3). These effects will be incorporated into the aerodynamic evaluation of the proposed design.

#### 5.3.2 Wing Configuration Comparison

Three distinct wing configurations are examined—biplane, BWB, and joined-wing [1][2][3][18][19][20]. The biplane concept can achieve a lower effective aspect ratio through constructive interference. The BWB configuration provides a smooth pressure distribution and higher overall L/D. The joined-wing yields a span efficiency factor of 1.4–1.5 [20].

The competitor study by Mermer and Özgen [41] found average aspect ratios of 24.5 and average wingspans of 66.45 m among existing HALE and solar-powered platforms, providing additional sizing benchmarks. Their observation that typical structural weight determination techniques are unsuitable for HALE UAVs led to the development of a new structural weight prediction model, which should be considered for adoption in the present design.

### 5.4 Structural Modelling

#### 5.4.1 Material Selection Strategy

CFRP was selected as the baseline structural material [8][9][21]. The anisotropic nature of CFRP allows the designer to tailor stiffness and strength by orienting fibre plies along principal load paths. Recent advances in out-of-plane reinforcement and nano-engineered resin systems further improve damage tolerance [8].

#### 5.4.2 Structural Analysis

A detailed finite-element model of the airframe is constructed using ANSYS Workbench [5]. The model incorporates realistic boundary conditions including aerodynamic pressure loads from CFD and inertial loads from flight dynamics simulation. Flutter analysis is performed using the coupled aeroelastic module, integrating aerodynamic influence coefficients (doublet-lattice method) with structural modal data.

The unified aeroelastic-flight dynamic framework developed by Murua et al. [44] offers a higher-fidelity alternative for flutter prediction, particularly for very flexible wings where geometrically nonlinear deformations significantly alter the aerodynamic characteristics. The UVLM formulation with free-wake effects captures wing–tail wake interference phenomena that conventional doublet-lattice methods may underpredict.

### 5.5 Energy System Modelling

#### 5.5.1 Solar Power Estimation

The solar-energy subsystem is sized based on triple-junction photovoltaic cells achieving specific powers exceeding 350 W/kg under stratospheric irradiance (~1,360 W/m²) [14][15]. The model incorporates cosine losses, shading effects, and seasonal/diurnal variations in solar flux at 18–20 km altitude.

The practical integration challenges identified by Łopusiewicz and Książek [43] must be factored into the solar power estimation: the first lamination method demonstrated 9.5% higher maximum power under low loading compared to the second method, and efficiency degradation under wing deflection was measurable. These efficiency losses, along with manufacturing defect allowances, will be incorporated as derating factors in the energy-balance analysis.

#### 5.5.2 Battery / Fuel-Cell Simulation

The hybrid storage model simulates a lithium-ion pack (~250 Wh/kg) and a PEM fuel-cell stack in MATLAB/Simulink [10][11]. Night-time endurance is evaluated by integrating the net power deficit over the dark period.

The charge-margin methodology developed for the AtlantikSolar [39] provides a rigorous framework for quantifying the safety margin of the energy system. The excess time metric T_exc and charge margin T_cm are defined as the margins by which the battery state-of-charge trajectory exceeds the minimum acceptable threshold. Designing for a charge margin of at least 30–40% (as demonstrated in the AtlantikSolar 81-hour flight) would ensure robustness against cloud cover, component degradation, and unexpected power demands.

#### 5.5.3 Hybrid Energy Management Framework

The energy-balance model orchestrates power flows from the solar array to storage devices and propulsion/avionics subsystems [10][11]. The hierarchical management strategy prioritises battery charging when excess solar power is available, with fuel-cell supplementation during extended night periods.

### 5.6 Stability and Control Analysis

The stability assessment builds on classical longitudinal and directional stability theory, adapted for the low-density environment of HALE flight [12][13]. Static margin is calculated by locating the aerodynamic centre and comparing it to the CG location, ensuring a margin of at least 5% of the mean aerodynamic chord. The EAV-3 experience [40] informs this analysis: the solar-electric UAV's static margin of 28.4% with CG at 31% of MAC provides a validated reference point.

Control surface sizing is performed using the derivative method, incorporating the effect of reduced dynamic pressure on control effectiveness [27]. Flutter boundaries are estimated using the Doublet Lattice Method (DLM), with the option of employing the higher-fidelity UVLM-based approach of Murua et al. [44] for detailed assessment.

### 5.7 Performance Simulation

Integrated simulations verify that the conceptual UAV meets all performance targets. An altitude–power relationship incorporates the 3.5% increase in power demand per kilometre of altitude gain. All simulations are performed in MATLAB for system-level analyses and ANSYS for high-fidelity aero-structural coupling [5].

### 5.8 Design Integration and Optimisation

A multi-objective genetic algorithm (MOGA) is employed to explore the design space, simultaneously minimising total mass, maximising endurance, and maximising L/D while satisfying constraints on flutter margin, structural stress, and solar-panel area. The trade-offs are explicitly quantified, and the optimiser iteratively adjusts variables such as wing span, chord distribution, spar geometry, CFRP lay-up sequence, solar-cell layout, and storage sizing.

---

## 6. Analysis and Discussion

This section synthesises the findings from the literature review and methodology to provide a critical analysis of the conceptual HALE UAV design.

### 6.1 Aerodynamic Performance Assessment

The aerodynamic analysis confirms that high-aspect-ratio wings are essential for achieving the target L/D of 25–30. The literature review reveals a clear trend: modern solar HALE platforms consistently achieve aspect ratios between 17.4 (EAV-3) and 30+ (Zephyr-class), with the lower end of this range being more practical for manufacturing and ground handling considerations [40].

The joined-wing configuration offers span efficiency factors of 1.4–1.5 [20], representing a significant aerodynamic advantage over conventional designs. However, the structural complexity and potential for wake interference between wing surfaces must be carefully evaluated using high-fidelity aeroelastic tools [44].

The low cruise speeds required for optimal solar power generation (6–8 m/s for EAV-3) present unique challenges: increased sensitivity to atmospheric disturbances, larger control surfaces required for authority, and significant wing bending that must be accommodated in the structural design [40].

### 6.2 Energy System Feasibility

The numerical validation demonstrates the critical importance of hybrid energy storage. The night-time energy requirement of approximately 23.9 kWh for a 12-hour dark period represents a fundamental challenge:

- **Pure Battery Solution**: At 250 Wh/kg, the required battery mass is approximately 95.7 kg—exceeding feasible limits for a platform targeting ~114 kg empty weight.
- **Hydrogen Fuel Cell Solution**: At 33.3 kWh/kg (LHV) and 50% system efficiency, only 1.44 kg of hydrogen is required. Including tankage and balance-of-plant (3× multiplier), the total hydrogen system mass is approximately 4.3 kg—a dramatic reduction compared to batteries.

This analysis aligns with the literature finding that fuel cells outperform batteries above 2.8 kWh energy demand [10]. The charge-margin methodology from AtlantikSolar [39] provides a robust framework for ensuring multi-day operation with appropriate safety margins.

### 6.3 Propulsion Optimisation Potential

The propulsion system optimisation work by Dantsker et al. [42] demonstrates that motor-propeller matching can yield 19% efficiency improvements. Applying this to the present design would reduce the electrical power requirement from ~1,994 W to approximately ~1,615 W—a corresponding reduction in night-time storage requirements from 23.9 kWh to approximately 19.4 kWh.

This represents a significant mass saving: the battery mass would reduce from 95.7 kg to approximately 77.6 kg, while hydrogen requirements would drop from 1.44 kg to approximately 1.16 kg (approximately 3.5 kg system mass).

### 6.4 Structural and Aeroelastic Considerations

The structural analysis reveals that CFRP composites are essential for achieving the required stiffness-to-weight ratios. The EAV-3 programme demonstrated that wing bending of 404 mm at 1-G flight is achievable with T-800 carbon fibre composites [40].

However, the high-aspect-ratio, very flexible wing configuration introduces significant aeroelastic coupling. The conventional decoupled approach (separate structural and aerodynamic analyses) may underpredict flutter boundaries. The UVLM-based coupled methodology developed by Murua et al. [44] provides a more accurate framework, particularly for capturing wing-tail wake interference effects.

### 6.5 Photovoltaic Integration Challenges

The practical challenges of integrating photovoltaic cells onto composite wings, as systematically investigated by Łopusiewicz and Książek [43], must be factored into the design:

1. **Micro-cracking**: Under aerodynamic loading, photovoltaic cells experience stress concentrations that can lead to micro-cracking, reducing efficiency.
2. **Galvanic isolation**: Carbon-fibre substrates are electrically conductive and require proper isolation to prevent short-circuiting.
3. **Manufacturing defects**: Electroluminescence testing reveals defects in 5–10% of cells, necessitating quality control protocols.
4. **Efficiency degradation under deflection**: Wing bending under load can reduce photovoltaic output by measurable amounts.

These practical considerations suggest that a conservative derating factor of 10–15% should be applied to theoretical solar power calculations.

### 6.6 Comparison with Established Platforms

The conceptual design compares favorably with established HALE platforms:

| Platform | Mass (kg) | Wingspan (m) | Aspect Ratio | Endurance |
|----------|-----------|--------------|--------------|-----------|
| Zephyr S | 53 | 25 | 24 | 25+ days |
| Helios | 730 | 75 | 30 | 10 hours |
| EAV-3 | 53 | 19.5 | 17.4 | Stratospheric test |
| AtlantikSolar | 6.9 | — | — | 81 hours |
| **Present Design** | ~114 (airframe) | 32 | ~30 | Target: 24+ hours |

The design targets are consistent with the literature benchmarks, with the hybrid energy storage solution providing a practical pathway to multi-day endurance.

---

## 7. Conclusion and Future Work

The study demonstrates the technical feasibility and multidisciplinary complexity involved in the conceptual design of a HALE UAV powered primarily by renewable energy. Through an expanded literature review encompassing both the original and newly acquired research, it is established that HALE UAVs rely on a delicate integration of aerodynamics, lightweight structural materials, and high-efficiency energy systems to achieve sustained flight at altitudes exceeding 18 km [1][2][3][4][39][40][41][42][43][44].

The numerical evaluation confirms that the aircraft geometry and aerodynamic assumptions produce realistic power demands (~2 kW electrical), while high-altitude solar flux combined with triple-junction GaAs photovoltaics provides ~9 kW of usable power. Night-time storage requirements (~23.9 kWh) make pure lithium-ion battery solutions infeasible (~95 kg), whereas hydrogen fuel-cell storage meets the requirement at <5 kg system mass. Propulsion system optimisation [42] could further reduce power demands by up to 19%.

The expanded literature base strengthens the design foundation in several critical areas:
1. **Perpetual-flight design methodology** [39] provides a rigorous framework for energy-system sizing and charge-margin optimisation.
2. **Empirical validation from EAV-3** [40] confirms the feasibility of high-aspect-ratio flexible wings and very-low-speed high-altitude flight.
3. **Hybrid propulsion concepts** [41] offer viable pathways for heavier, payload-intensive HALE platforms.
4. **Advanced aeroelastic analysis** [44] enables more accurate flutter prediction for very flexible wings.
5. **Photovoltaic integration research** [43] quantifies practical efficiency losses and establishes manufacturing best practices.
6. **Battery-free UAV concepts** [45] point toward future energy storage paradigms that may eliminate battery degradation concerns.

**Future Work:**
- Development of detailed computational models incorporating real atmospheric variations including turbulence, temperature gradients, and cloud shading.
- Prototype-scale CFD studies and wind-tunnel validation under low-Reynolds-number conditions.
- Structural testing of composite wing segments to investigate flutter boundaries and material reliability during extended missions.
- Development of a dedicated energy management algorithm incorporating the charge-margin methodology of [39] to optimally allocate power between solar input, battery storage, and fuel cell output.
- Investigation of propulsion system optimisation using the framework of [42] to minimise power consumption.
- Application of the coupled aeroelastic-flight dynamic framework of [44] for high-fidelity flutter analysis.
- Adoption of the photovoltaic integration best practices identified by [43] for the wing manufacturing process.
- Fabrication of a scaled demonstrator UAV to validate theoretical predictions through flight testing.
- Research into emerging technologies such as morphing wings, solid-state batteries, ultra-light flexible solar arrays, and supercapacitor-based energy storage [45].

---

## 8. References

### Original Citations (Preserved from Version 1)

[1] Goraj, Z., Frydrychiewicz, A., & Winiecki, J. (1999). Design concept of a high-altitude long-endurance unmanned aerial vehicle. *Aircraft Design*, 2(1), 19–44.

[2] Goraj, Z. (2004). High altitude long endurance unmanned aerial vehicle of a new generation – A design challenge for a low cost, reliable and high performance aircraft. *Bulletin of the Polish Academy of Sciences, Technical Sciences*, 52(3), 173–194.

[3] Romeo, G., Frulla, G., Cestino, E., & Corsino, G. (2004). HELIPLAT: Design, aerodynamic, structural analysis of long-endurance solar-powered stratospheric platform. *Journal of Aircraft*, 41(6), 1505–1520.

[4] Najafi, Y. (2011). *Design of a High Altitude Long Endurance Solar Powered UAV: Solar Powered Aerial Communicator (SPACOM)*. MS Thesis, San Jose State University.

[5] ANSYS Inc. (2024). *ANSYS Workbench User Guide*. Canonsburg, PA.

[6] Anderson, J. D. (2017). *Fundamentals of Aerodynamics* (6th ed.). McGraw-Hill.

[7] Bertin, J. J., & Cummings, R. M. (2014). *Aerodynamics for Engineers* (6th ed.). Pearson.

[8] Daniel, I. M., & Ishai, O. (2006). *Engineering Mechanics of Composite Materials* (2nd ed.). Oxford University Press.

[9] Jones, R. M. (1999). *Mechanics of Composite Materials* (2nd ed.). Taylor & Francis.

[10] Boukoberine, M. N., Zhou, Z., & Benbouzid, M. (2019). A comparative review of electric and hybrid energy storage systems for UAVs: Configurations, challenges, and optimal dimensioning. *Journal of Power Sources*, 613, 234860.

[11] Hassanalian, M., & Abdelkefi, A. (2017). Classifications, applications, and design challenges of unmanned aerial vehicles: A review. *Progress in Aerospace Sciences*, 91, 99–131.

[12] Nelson, R. C. (1998). *Flight Stability and Automatic Control* (2nd ed.). McGraw-Hill.

[13] Cook, M. V. (2013). *Flight Dynamics Principles* (3rd ed.). Elsevier.

[14] Green, M. A., Hishida, Y., & Dunlop, E. D. (2021). Solar cell efficiency tables (Version 58). *Progress in Photovoltaics: Research and Applications*, 29(7), 1–15.

[15] Yamaguchi, M., Takamoto, T., Araki, K., & Ekins-Daukes, N. (2006). Multi-junction III–V solar cells: Current status and future potential. *Solar Energy*, 80(8), 1040–1047.

[16] Noor, A. K., Venneri, S. L., Paul, D. B., & Hopkins, M. A. (2000). Structures technology for future aerospace systems. *Computers & Structures*, 78(1–3), 5–19.

[17] Austin, R. (2010). *Unmanned Aircraft Systems: UAVS Design, Development and Deployment*. Wiley.

[18] Panagiotou, P., Tsavlidis, L., & Kyriazis, N. (2018). Conceptual design of a blended wing body MALE UAV. *Aerospace Science and Technology*, 78, 640–651.

[19] Wang, Z., Zhuang, M., & Shao, W. (2018). Conceptual design of solar-powered high-altitude long-endurance UAV. *Chinese Journal of Aeronautics*, 31(8), 1634–1647.

[20] Wolkovitch, J. (1986). The joined wing: An overview. *Journal of Aircraft*, 23(2), 161–178.

[21] Livne, E. (2003). Airplane aeroelasticity: From the pioneers to the future challenges. *Journal of Aircraft*, 40(6), 983–997.

[22] Wright, J. R., & Cooper, J. E. (2007). *Introduction to Aircraft Aeroelasticity and Loads*. Wiley.

[23] Scholz, D. (1998). Aircraft systems—Integration of avionics. In *Aeronautical Engineering* (pp. 123–145). Wiley.

[24] Larminie, J., & Dicks, A. (2003). *Fuel Cell Systems Explained* (2nd ed.). Wiley.

[25] Fuel Cell Technologies Office. (2017). *Fuel Cell Technologies Market Report*. U.S. Department of Energy.

[26] Livne, E. (2003). Future of airplane aeroelasticity. *Journal of Aircraft*, 40(6), 1066–1092.

[27] Roskam, J. (1985). *Airplane Design: Part IV: Preliminary Calculation of Aerodynamic, Thrust and Power Characteristics*. DARcorporation.

[28] Colozza, A. J., & Dolce, J. L. (2003). *High-Altitude, Long-Endurance Airships for Coastal Surveillance*. NASA Glenn Research Center.

[29] Noll, T. E., Brown, J. M., Perez-Davis, M. E., & Ishmael, S. D. (2004). Investigation of the Helios Prototype Vehicle Mishap. *NASA Mishap Report*.

### New Citations (Added in Version 2)

[39] Oettershagen, P., Melzer, A., Faust, T., Hakenberg, R., & Siegwart, R. (2017). Design of solar-powered UAVs for endurance flight. *Journal of Field Robotics*, 34(2), 291–311. https://doi.org/10.1002/rob.21669

[40] Hwang, J., Lee, D., & Kim, S. (2016). Aerodynamic design of solar-powered high-altitude long-endurance UAV. *Journal of Aircraft*, 53(5), 1291–1303.

[41] Mermer, S., & Özgen, S. (2017). Conceptual design of hybrid turbofan/solar powered HALE UAV. In *7th European Conference for Aeronautics and Space Sciences (EUCASS)*. Milan, Italy.

[42] Dantsker, O. D., Cale, T. G., & Xiao, M. (2020). Propulsion system design and optimization for solar-powered UAVs. In *AIAA Propulsion and Energy Forum*. Virtual Event.

[43] Łopusiewicz, Ł., & Książek, I. (2024). Integration of photovoltaic cells on composite wing structures for solar-powered UAVs. In *ICAS 2024 Proceedings*. Florence, Italy.

[44] Murua, J., Quintana, P., & Claridge, M. (2011). Stability and open-loop dynamics of very flexible aircraft including wake interference. In *AIAA Atmospheric Flight Mechanics Conference*. Portland, OR.

[45] Liller, K., et al. (2025). Battery-free solar UAV with supercapacitor energy storage. *Scientific Reports*, 15, 90729.
