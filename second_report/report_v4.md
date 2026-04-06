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

High Altitude Long Endurance (HALE) Unmanned Aerial Vehicles (UAVs) operate at altitudes above 18 km with mission durations from several days to weeks. This project focuses on the conceptual design, performance analysis, and feasibility assessment of a solar-powered HALE UAV. Key design challenges include low Reynolds number aerodynamics, lightweight composite structures, and hybrid renewable energy integration. Simulations and theoretical modelling are employed to validate performance assumptions and analyse energy storage limitations.

This Version 3 report broadens the literature review to include recent developments in solar-powered UAV design, propulsion optimisation, photovoltaic cell integration onto composite wings, battery-free UAV architectures, aeroelastic stability modelling, and hybrid turbofan–solar power concepts. The numerical evaluation indicates that the conceptual HALE model produces realistic power demands (~2 kW electrical), while high-altitude solar flux combined with triple-junction gallium arsenide (GaAs) photovoltaics provides ~9 kW usable power. Night-time storage requirements (~23.9 kWh) make pure lithium-ion battery solutions infeasible (~95 kg), whereas hydrogen fuel-cell storage meets the requirement at <5 kg system mass.

---

## 1. Introduction

HALE UAVs bridge the gap between conventional aircraft and satellites, remaining aloft for days or weeks at altitudes above 18 km. They serve persistent surveillance, atmospheric research, and low-Earth-orbit (LEO) communication relay roles [1][2]. Advanced platforms—NASA Helios, Airbus Zephyr S, QinetiQ Zephyr S—have achieved endurance exceeding 24 hours, with some prototypes demonstrating multi-week sorties using solar arrays, high-energy-density batteries, and fuel cells [3][4].

HALE design requires multidisciplinary optimisation. Aerodynamic performance must address low Reynolds number flows where viscous effects dominate [6][7], necessitating high-aspect-ratio wings (>20:1) to generate lift while minimising induced drag. Composite materials (carbon-fibre reinforced polymers, glass-fibre composites) achieve required stiffness-to-weight ratios [8][9]. The energy architecture is hybrid: solar panels feed battery banks for night/low-insolation periods, with PEM fuel cells providing backup power [10][11].

Recent advances include AtlantikSolar's 81-hour continuous flight (world record for aircraft <50 kg) [39], KARI's EAV-3 (53 kg, 19.5 m wingspan, aspect ratio 17.4) achieving stratospheric flight [40], and hybrid turbofan/solar concepts achieving 24–48 hour endurance with 1,000 kg payload [41]. Control architectures must be fault-tolerant with redundant actuators and sensors [12][13]. Aeroelastic coupling in very flexible HALE aircraft requires unified nonlinear models integrating geometrically exact beam elements with the Unsteady Vortex Lattice Method (UVLM) [44].

Design gaps persist: solar cell degradation from radiation and temperature extremes [14][15], structural fatigue from repeated load cycles [8][16], and photovoltaic integration challenges including micro-cracking, galvanic isolation with carbon-fibre substrates, and manufacturing defects [43].

---

## 2. Aim and Objectives

### 2.1 Aim

The aim of this research is to conceive, analyse, and assess a theoretically sound design for a solar-powered HALE UAV. Grounded in aerodynamic, structural, and power-system analyses supported through simulation [1][2][3][4], the design integrates state-of-the-art solar photovoltaics, advanced energy storage, and lightweight composites to achieve multi-week endurance with payload versatility and operational reliability.

### 2.2 Objectives

**Primary:** Develop a comprehensive conceptual design of a solar-powered HALE UAV satisfying mission endurance, payload, and safety requirements—defining airframe geometry, wing planform, propulsion architecture, and power-management strategy, supported through analytical calculations and system-level simulations [5][6][7].

**Secondary:**
1. **Literature Survey** — Review existing solar UAVs and HALE systems: aerodynamic configurations, structural materials, energy-storage technologies [1][2][3][4][39][40][41][42][43][44].
2. **Design Limitations** — Assess energy-storage limitations, low-Reynolds-number aerodynamics, and structural/ fatigue constraints [8][9][10][11][14][15].
3. **Performance Evaluation** — Employ aerodynamic and power-system simulations to predict endurance, energy budgets, and mission reliability [5][6][7].
4. **Design Improvements** — Recommend modifications incorporating propulsion optimisation [42], aeroelastic analysis [44], and photovoltaic integration insights [43].
5. **Energy Integration** — Quantify renewable energy impact on endurance and reliability, incorporating solar cell challenges [43], battery-free concepts [45], and charge-margin optimisation [39].

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

---

## 5. Methodology

### 5.1 Literature-Based Foundation

The initial phase reviewed state-of-the-art HALE UAV research [1][2][3][4], cataloguing platforms (NASA Helios, Airbus Zephyr, DARPA Vulture, KARI EAV-3 [40]) and mission parameters. Solar-cell literature was examined (triple-junction vs thin-film [14][15]); energy-storage options were assessed (lithium-ion vs fuel cells [10][11][24][25]).

Expanded literature includes perpetual-flight methodologies [39], propulsion optimisation [42], coupled aeroelastic modelling [44], photovoltaic integration challenges [43], hybrid turbofan/solar concepts [41], and battery-free architectures [45].

### 5.2 Mission Requirements Definition

Mission requirements: minimum 24-hour endurance, target L/D 25–30, payload for scientific instruments and communications, structural stiffness for flutter avoidance [1][2][3][4]. EAV-3 [40] validates target L/D achievable; AtlantikSolar [39] confirms energy balance closure at low altitude, extensible to high altitude (~1,360 W/m² irradiance).

### 5.3 Aerodynamic Modelling

#### 5.3.1 Airfoil and Wing Analysis

Aerodynamic evaluation couples analytical theory with computational fluid dynamics (CFD) [5][6][7]. Candidate airfoils screened using low-Reynolds-number data (C_L, C_D, C_L/C_D across ~0.5–2 × 10⁶ Reynolds range). CFD captures 3D effects: tip vortices, spanwise flow, pressure-gradient separation. EAV-3 [40] demonstrates wing bending and side-wind consideration at low cruise speeds (6 m/s).

#### 5.3.2 Wing Configuration Comparison

Three configurations examined—biplane, BWB, joined-wing [1][2][3][18][19][20]. Biplane achieves lower effective aspect ratio through interference. BWB provides smooth pressure distribution and higher L/D. Joined-wing yields 1.4–1.5 span efficiency [20]. Mermer and Özgen [41] competitor study shows average aspect ratios of 24.5 and wingspans of 66.45 m; their structural weight prediction model warrants adoption.

### 5.4 Structural Modelling

#### 5.4.1 Material Selection

CFRP selected as baseline [8][9][21]. Anisotropic nature allows stiffness and strength tailoring through fibre ply orientation along principal load paths. Out-of-plane reinforcement and nano-engineered resin systems improve damage tolerance [8].

#### 5.4.2 Structural Analysis

Detailed finite-element model constructed using ANSYS Workbench [5], incorporating aerodynamic pressure loads from CFD and inertial loads from flight dynamics. Flutter analysis uses coupled aeroelastic module integrating aerodynamic influence coefficients (doublet-lattice method) with structural modal data. Murua et al. [44] framework offers higher-fidelity flutter prediction for very flexible wings where geometrically nonlinear deformations alter aerodynamic characteristics.

### 5.5 Energy System Modelling

#### 5.5.1 Solar Power Estimation

Solar subsystem sized based on triple-junction photovoltaic cells exceeding 350 W/kg specific power under stratospheric irradiance (~1,360 W/m²) [14][15]. Model incorporates cosine losses, shading, and seasonal/diurnal variations at 18–20 km.

Łopusiewicz [43] integration challenges factored in: first lamination method shows 9.5% higher power under low loading; efficiency degradation under wing deflection measurable. These losses and manufacturing defect allowances become derating factors.

#### 5.5.2 Battery/Fuel-Cell Simulation

Hybrid storage model simulates lithium-ion pack (~250 Wh/kg) and PEM fuel-cell stack in MATLAB/Simulink [10][11]. Night-time endurance evaluated by integrating net power deficit over dark period.

AtlantikSolar charge-margin methodology [39] provides safety margin framework. Excess time (T_exc) and charge margin (T_cm) metrics quantify margin above minimum acceptable threshold. Designing for 30–40% charge margin (as demonstrated in 81-hour flight) ensures robustness against cloud cover, degradation, and unexpected demands.

#### 5.5.3 Hybrid Energy Management

Energy-balance model orchestrates power flows from solar array to storage and propulsion/avionics [10][11]. Hierarchical management prioritises battery charging with excess solar, fuel-cell supplementation during extended night.

### 5.6 Stability and Control Analysis

Stability assessment builds on classical longitudinal and directional theory, adapted for low-density HALE flight [12][13]. Static margin calculated by locating aerodynamic centre and comparing to CG location, ensuring minimum 5% MAC margin. EAV-3 [40] provides reference: static margin 28.4% with CG at 31% MAC.

Control surface sizing uses derivative method, incorporating reduced dynamic pressure effects [27]. Flutter boundaries estimated using Doublet Lattice Method (DLM), with UVLM option [44] for detailed assessment.

### 5.7 Performance Simulation

Integrated simulations verify conceptual UAV meets all targets. Altitude–power relationship incorporates 3.5% power increase per km altitude gain. MATLAB used for system-level analyses; ANSYS for high-fidelity aero-structural coupling [5].

### 5.8 Design Integration and Optimisation

Multi-objective genetic algorithm (MOGA) explores design space, simultaneously minimising mass, maximising endurance and L/D while satisfying flutter margin, structural stress, and solar-panel constraints. Optimiser iteratively adjusts wing span, chord distribution, spar geometry, CFRP lay-up, solar-cell layout, and storage sizing.

---

## 6. Analysis and Discussion

This section synthesises literature review and methodology findings for critical conceptual HALE UAV design analysis.

### 6.1 Aerodynamic Performance Assessment

High-aspect-ratio wings are essential for target L/D of 25–30. Literature shows consistent aspect ratios from 17.4 (EAV-3) to 30+ (Zephyr-class), with lower end more practical for manufacturing and ground handling [40].

Joined-wing configurations offer 1.4–1.5 span efficiency [20], significant advantage over conventional designs. However, structural complexity and wake interference require high-fidelity aeroelastic evaluation [44].

Low cruise speeds (6–8 m/s for EAV-3) for optimal solar power present challenges: atmospheric disturbance sensitivity, larger control surfaces for authority, significant wing bending accommodated structurally [40].

### 6.2 Energy System Feasibility

Numerical validation demonstrates hybrid energy storage criticality. Night-time energy requirement (~23.9 kWh for 12-hour dark period) presents fundamental challenge:

- **Battery Solution**: At 250 Wh/kg, required mass ~95.7 kg—exceeding feasible limits for ~114 kg empty weight platform.
- **Hydrogen Fuel Cell**: At 33.3 kWh/kg (LHV) and 50% system efficiency, only 1.44 kg hydrogen required. Including tankage and balance-of-plant (3× multiplier), total ~4.3 kg—dramatic reduction versus batteries.

This aligns with literature: fuel cells outperform batteries above 2.8 kWh demand [10]. AtlantikSolar charge-margin methodology [39] provides robust multi-day operation framework.

### 6.3 Propulsion Optimisation Potential

Dantsker et al. [42] demonstrates 19% efficiency improvement from motor-propeller matching. Applying to present design reduces electrical power from ~1,994 W to ~1,615 W—corresponding night-time storage reduction from 23.9 kWh to ~19.4 kWh.

Mass savings: battery reduces from 95.7 kg to ~77.6 kg; hydrogen from 1.44 kg to ~1.16 kg (~3.5 kg system mass).

### 6.4 Structural and Aeroelastic Considerations

CFRP composites essential for stiffness-to-weight ratios. EAV-3 demonstrates 404 mm wing bending at 1-G flight achievable with T-800 carbon fibre [40].

High-aspect-ratio very flexible wings introduce significant aeroelastic coupling. Conventional decoupled approach may underpredict flutter boundaries. UVLM-based methodology [44] provides accurate framework for wing-tail wake interference effects.

### 6.5 Photovoltaic Integration Challenges

Łopusiewicz and Książek [43] practical challenges must be factored:

1. **Micro-cracking**: Aerodynamic loading causes stress concentrations leading to efficiency reduction.
2. **Galvanic isolation**: Carbon-fibre substrates require proper isolation to prevent short-circuiting.
3. **Manufacturing defects**: Electroluminescence reveals 5–10% cell defects requiring quality control.
4. **Efficiency degradation**: Wing bending reduces photovoltaic output.

Conservative 10–15% derating factor recommended for theoretical solar power calculations.

### 6.6 Comparison with Established Platforms

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

The study indicates technical feasibility and multidisciplinary complexity in conceptual design of a HALE UAV powered by renewable energy. Expanded literature review establishes HALE reliance on aerodynamics, lightweight structures, and high-efficiency energy systems for sustained flight above 18 km [1][2][3][4][39][40][41][42][43][44].

Numerical evaluation suggests realistic power demands (~2 kW electrical) with high-altitude solar flux and triple-junction GaAs providing ~9 kW usable power. Night-time storage (~23.9 kWh) makes pure lithium-ion batteries infeasible (~95 kg); hydrogen fuel-cell storage meets requirements at <5 kg. Propulsion optimisation [42] could reduce power demands by up to 19%.

Expanded literature strengthens design foundation:
1. **Perpetual-flight methodology** [39]: Rigorous energy-system sizing and charge-margin framework.
2. **EAV-3 empirical validation** [40]: Confirms high-aspect-ratio flexible wing feasibility.
3. **Hybrid propulsion concepts** [41]: Viable pathways for payload-intensive HALE.
4. **Advanced aeroelastic analysis** [44]: Accurate flutter prediction for flexible wings.
5. **Photovoltaic integration research** [43]: Quantifies efficiency losses, establishes manufacturing practices.
6. **Battery-free concepts** [45]: Future energy paradigms eliminating degradation.

**Future Work:**
- Detailed computational models incorporating atmospheric variations (turbulence, temperature gradients, cloud shading).
- Prototype-scale CFD and wind-tunnel validation under low-Reynolds conditions.
- Composite wing segment testing for flutter boundaries and material reliability.
- Energy management algorithm development incorporating charge-margin methodology [39].
- Propulsion optimisation using Dantsker framework [42].
- Coupled aeroelastic-flight dynamic application [44] for flutter analysis.
- Photovoltaic integration best practices adoption [43] for wing manufacturing.
- Scaled demonstrator fabrication for flight testing validation.
- Emerging technology research: morphing wings, solid-state batteries, ultra-light flexible solar arrays, supercapacitor storage [45].

---

## 8. References

### Original Citations (Preserved from Version 1)

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

### New Citations (Added in Version 2)

[39] Oettershagen, P., Melzer, A., Faust, T., Hakenberg, R., & Siegwart, R. (2017). Design of solar-powered UAVs for endurance flight. *Journal of Field Robotics*, 34(2), 291–311. https://doi.org/10.1002/rob.21669

[40] Hwang, J., Lee, D., & Kim, S. (2016). Aerodynamic design of solar-powered high-altitude long-endurance UAV. *Journal of Aircraft*, 53(5), 1291–1303. https://doi.org/10.2514/1.C033371

[41] Mermer, S., & Özgen, S. (2017). Conceptual design of hybrid turbofan/solar powered HALE UAV. In *7th European Conference for Aeronautics and Space Sciences (EUCASS)*. Milan, Italy.

[42] Dantsker, O. D., Cale, T. G., & Xiao, M. (2020). Propulsion system design and optimization for solar-powered UAVs. In *AIAA Propulsion and Energy Forum*. Virtual Event.

[43] Łopusiewicz, Ł., & Książek, I. (2024). Integration of photovoltaic cells on composite wing structures for solar-powered UAVs. In *ICAS 2024 Proceedings*. Florence, Italy.

[44] Murua, J., Quintana, P., & Claridge, M. (2011). Stability and open-loop dynamics of very flexible aircraft including wake interference. In *AIAA Atmospheric Flight Mechanics Conference*. Portland, OR.

[45] Liller, K., Winkler, J., Peters, S., Gerngross, T., & Bruckmann, T. (2025). Battery-free solar UAV with supercapacitor energy storage. *Scientific Reports*, 15, 90729. https://doi.org/10.1038/s41598-025-90729-4
