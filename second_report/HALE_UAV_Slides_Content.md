# HALE UAV Presentation — Slide Content (Refactored)
**Version 2 — Corrected & References Added**

---

## Theme: Midnight Executive (Aerospace Navy/Cyan)

| Token | Hex | Usage |
|-------|-----|-------|
| Primary background (dark slides) | `#1B2A4A` | Title, Conclusions, Q&A slides |
| Content slide background | `#F4F6FA` | All body slides |
| Accent colour | `#2E86AB` | Left bars, stat boxes |
| Secondary accent | `#A8DADC` | Highlights, dividers |
| Text on dark | `#FFFFFF` | Dark-background slides |
| Text on light | `#1B2A4A` | Body slides |
| Data highlight | `#E63946` | Key numerical callouts |

---

## SLIDE 1: Title Slide
**Background:** Dark navy (`#1B2A4A`)
**Accent:** Thin cyan bar at bottom

**Content:**
- Title: HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES
- Subtitle: Sustained Flight Through Renewable Energy
- Author: Parth Patil (22BTRAS031)
- Advisor: Dr Amalesh Barai, Professor, Department of Aerospace Engineering
- Institution: Faculty of Engineering & Technology, JAIN (Deemed-to-be University)
- Year: 2025–2026

---

## SLIDE 2: Agenda
**Background:** Light steel (`#F4F6FA`)
**Accent:** Left blue bar

**Content:**
1. Project Motivation & Aims
2. Literature Review — Existing HALE UAVs
3. Design Requirements & Constraints
4. Conceptual Design Overview
5. Aerodynamic, Propulsion & Structural Design
6. Performance Analysis & Results
7. Stability, Trade-offs & Validation
8. Conclusions & Future Work

---

## SLIDE 3: Project Motivation & Aims
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Why HALE UAV?** *(Refs: [1][2])*
- Bridge the gap between conventional aircraft and satellites
- Operate at altitudes above 18 km for days or weeks
- Enable persistent surveillance and communication relay
- Reduce reliance on expensive satellite infrastructure

**Right Column — Project Aim** *(Refs: [1][2][3][4])*
Conceive, analyse, and assess a theoretically sound solar-powered HALE UAV achieving multi-week endurance with payload versatility and operational reliability.

**Bottom Callout Box (dark bg):**
> "Target: Continuous flight above 18 km for minimum 24 hours, with ambition for several days" [1][2][3][4]

---

## SLIDE 4: Project Objectives
**Background:** Light steel
**Accent:** Left blue bar

**Content:**
1. **Primary:** Develop comprehensive conceptual design satisfying mission endurance, payload, and safety requirements *(Refs: [1][2][3][4])*
2. **Literature Survey:** Review existing solar UAVs — aerodynamic configs, materials, energy storage *(Refs: [1][2][3][4][39][40][41][42][43][44])*
3. **Design Limitations:** Assess energy-storage limits, low-Re aerodynamics, structural/fatigue constraints *(Refs: [8][9][10][11][14][15])*
4. **Performance Evaluation:** Predict endurance, energy budgets, and mission reliability via simulation *(Refs: [5][6][7])*
5. **Design Improvements:** Recommend modifications — propulsion optimisation, aeroelastic analysis *(Refs: [42][44])*
6. **Energy Integration:** Quantify renewable energy impact on endurance and reliability *(Refs: [39][43][45])*

---

## SLIDE 5: Literature Review — Key Existing HALE UAVs
**Background:** Light steel
**Accent:** Left blue bar

**Platform Comparison Table:**

| Platform | Mass (kg) | Wingspan (m) | AR | Endurance | Ref |
|----------|-----------|--------------|----|-----------|-----|
| Zephyr S | 53 | 25 | 24 | 25+ days | [3][4] |
| Helios | 730 | 75 | 30 | 14+ hours | [3][4] |
| EAV-3 (KARI) | 53 | 19.5 | 17.4 | Stratospheric test | [40] |
| AtlantikSolar | 6.9 | — | — | 81 hours (world record <50 kg) | [39] |
| **Present Design** | ~114 kg *(structural estimate)* | 32 | ~30 | Target: 24+ hours | — |

> **Note on Present Design mass:** The ~114 kg figure is a structural airframe estimate from the report's energy feasibility analysis. It is not directly comparable to the MTOW figures of the platforms above and should not be read as take-off weight.

**Key Insights:** *(Refs: [1][2][3][14][15][39][40])*
- High-aspect-ratio monoplane configurations dominate existing platforms (AR 17.4 to 30+)
- Triple-junction GaAs cells achieve 25–30% efficiency — the practical upper bound for current photovoltaics

---

## SLIDE 6: Design Requirements & Constraints
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Mission Requirements:**
- Altitude: 18–22 km (stratospheric) *(Ref: [1][2])*
- Endurance: Minimum 24 hours (target: multi-day) *(Ref: [1][2][3][4])*
- Cruise speed: ~80 km/h
- Payload: 5–10 kg for instruments & communications

**Right Column — Technical Constraints:**
- Low Reynolds number flows (10⁵–10⁶): viscous effects dominate *(Ref: [6][7])*
- Structural stiffness for flutter avoidance *(Ref: [22][26])*
- Energy storage for night-time operation *(Ref: [10][11])*
- Environmental: cloud cover, wind shear, temperature gradients *(Ref: [28][29])*

**Bottom Stats (three boxes):**
- Box 1: **"25–30"** *(red)* — L/D Ratio Target
- Box 2: **">18 km"** *(blue)* — Service Ceiling
- Box 3: **">24 hrs"** *(blue)* — Endurance Target

---

## SLIDE 7: Conceptual Design Overview
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Top-Level Design Approach:** *(Refs: [1][2][3][4])*
- High-aspect-ratio monoplane configuration
- Solar cells on wing and fuselage surfaces
- Hybrid energy: solar + batteries + fuel cell
- CFRP composite ultra-lightweight structure
- Distributed propulsion system

**Right Column — Configuration Choice:** *(Refs: [1][18][19][20])*
Monoplane with high aspect ratio selected over biplane, BWB, and joined-wing based on:
- Manufacturing simplicity and lower fabrication risk
- Proven technology readiness (Zephyr S, Helios, EAV-3)
- Structural reliability and established load-path analysis
- Ground handling practicality at 32 m span

**Bottom Callout Box (dark bg):**
> "Selected Design Parameters: Wingspan: 32 m | Aspect Ratio: ~30 | Structural Estimate: ~114 kg | Payload: 5–10 kg"

---

## SLIDE 8: Aerodynamic Design
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Wing Geometry:** *(Refs: [6][7][40])*
- Wingspan: 32 m
- Aspect Ratio: ~30
- Low-Reynolds-number aerofoil selection (e.g., Eppler E387, Wortmann FX 63-137)
- High-lift, low-drag optimisation for Re 10⁵–10⁶

**Right Column — Key Considerations:** *(Refs: [5][6][7])*
- Low Re flows (10⁵–10⁶): viscous effects dominate, laminar separation bubbles critical
- Target L/D: 25–30
- Minimise induced drag via high aspect ratio (C_Di = C_L² / πeAR)
- CFD (ANSYS Fluent) + XFOIL analytical methods for validation

**Configuration Comparison Table:** *(Refs: [1][18][19][20])*

| Configuration | Pros | Cons |
|--------------|------|------|
| Monoplane | Simple, proven, easy solar integration | Large span, tip deflection |
| Biplane | Higher payload at lower span [1] | Interference drag, solar self-shading |
| BWB | Higher L/D, smooth pressure distribution [18][19] | Manufacturing complexity |
| Joined-wing | Span efficiency 1.4–1.5 [20] | Structural complexity, wake interference [44] |

> ⚠ **Correction:** The earlier claim of "AR ~40 possible" for joined-wing has been removed — the report supports only a span efficiency advantage of 1.4–1.5 [20], not a specific AR figure.

**Stat Callout (red bg):** **"30"** — Aspect Ratio *(Ref: [40])*

---

## SLIDE 9: Propulsion & Energy Architecture
**Background:** Light steel
**Accent:** Left blue bar

**Title:** Hybrid Energy Architecture

**Three Power Source Boxes (dark bg):**
1. **Solar (Day):** "~9 kW" — Triple-junction GaAs cells, 25–30% efficiency, 1,360 W/m² irradiance at altitude *(Refs: [14][15])*
2. **Storage (Night):** "~24 kWh" — Hybrid lithium-ion battery + hydrogen fuel cell *(Refs: [10][11][24])*
3. **Cruise Power:** "~2 kW" — Electrical power demand at 80 km/h cruise *(Refs: [10][11])*

**Energy System Reasoning:** *(Refs: [10][11][39][42])*
- Fuel cells outperform batteries above 2.8 kWh demand [10]
- Night-time requirement (~23.9 kWh) makes pure batteries infeasible (~95 kg at 250 Wh/kg) [10]
- Hydrogen fuel cell solution: ~1.44 kg H₂ + tankage + balance-of-plant ≈ 4.3 kg total [10][11]
- Charge-margin methodology (Oettershagen et al.) ensures multi-day robustness [39]
- Propulsion optimisation (Dantsker et al.) could reduce power demand by 19%, reducing night storage to ~19.4 kWh [42]

---

## SLIDE 10: Structural Design
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Material Selection: CFRP Composites** *(Refs: [8][9])*
- Carbon-fibre reinforced polymers (T-800 spar caps, T-300 fabric skins)
- High stiffness-to-weight ratio (~5× aluminium)
- Anisotropic tailoring for spanwise bending and torsion load paths
- Autoclave/RTM manufacturing for void content <1%

**Right Column — Structural Analysis** *(Refs: [5][22][44])*
- ANSYS Workbench for FEA (large-displacement formulation) [5]
- Static deflection: expected tip deflection 10–15% of semi-span [40]
- Modal frequency analysis for flutter margin prediction
- Murua et al. UVLM methodology for aeroelastic coupling [44]

**Weight Breakdown Table** *(Refs: [40] for structural benchmark)*

| Component | Mass (kg) | Notes |
|-----------|-----------|-------|
| Airframe (structure) | ~22 | CFRP primary; benchmarked to EAV-3 [40] |
| Solar panels | ~15 | GaAs on wing/fuselage upper surface |
| Energy storage | ~5 | Fuel cell + H₂ system [10][11] |
| Avionics & systems | ~5 | Sensors, comms, flight control |
| **Total (excl. payload)** | **~47–52** | **Structural estimate** |
| Payload | 5–10 | Mission equipment |
| **Max Take-off (est.)** | **~57–62** | **Conceptual estimate** |

> ⚠ **Clarification:** The ~114 kg figure referenced elsewhere in the report is the energy feasibility analysis mass (from Section 6.2 energy calculation), not a finalised MTOW. The weight table above represents the component-level mass build-up. These figures are benchmarked estimates and require detailed mass-property analysis.

---

## SLIDE 11: Performance Analysis
**Background:** Light steel
**Accent:** Left blue bar

**Four Metric Boxes (coloured backgrounds):**
1. *(red bg)* **">24 hrs"** — Endurance Target *(Ref: [1][2][3][4])*
2. *(blue bg)* **"18–22 km"** — Cruise Altitude *(Ref: [1][2])*
3. *(dark bg)* **"25–30"** — L/D Ratio Target *(Ref: [6][7][40])*
4. *(blue bg)* **"~80 km/h"** — Cruise Speed

**Key Analysis Results:**
- Cruise power: ~2 kW electrical *(Ref: [10][11])*
- Solar power available: ~9 kW (triple-junction GaAs at 1,360 W/m² stratospheric irradiance) *(Ref: [14][15])*
- Night-time energy storage required: ~23.9 kWh for 12-hour dark period *(Ref: [10])*
- Altitude power penalty: ~3.5% power increase per km altitude gain *(Ref: [10])*
- Propulsion optimisation potential: 19% efficiency improvement (Dantsker et al.) *(Ref: [42])*

---

## SLIDE 12: Stability & Control
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Stability Analysis:** *(Refs: [12][13][40])*
- Longitudinal and directional stability analysis
- Static margin target: minimum 5% MAC
- EAV-3 reference: 28.4% SM with CG at 31% MAC [40]
- CG remains fixed during flight (no fuel burn shift) [40]

**Right Column — Control Surfaces:** *(Refs: [12][13][27])*
- Conventional tail arrangement (elevator, rudder)
- Ailerons for roll control
- Larger deflection angles required at low air density [27]
- Fault-tolerant redundant actuator architecture [12][13]

**Flutter Analysis:** *(Refs: [22][26][44])*
High-aspect-ratio very flexible wings introduce significant aeroelastic bending-torsion coupling. Conventional doublet-lattice methods may overpredict flutter margins. Murua et al. [44] methodology — geometrically exact beam finite elements coupled with Unsteady Vortex Lattice Method (UVLM) including free-wake effects — provides accurate flutter boundary prediction, capturing wing-tail wake interference critical to pitch damping.

---

## SLIDE 13: Design Trade-offs & Decisions
**Background:** Light steel
**Accent:** Left blue bar

**Trade-offs Table:**

| Decision | Trade-off | Resolution | Refs |
|----------|-----------|------------|------|
| Aspect Ratio ~30 | Manufacturing complexity vs aerodynamic performance | Practical compromise; consistent with EAV-3 to Zephyr-class range | [40][3] |
| Fuel cell over pure battery | System complexity vs mass penalty | 95 kg battery vs 4.3 kg fuel cell system; fuel cell mandatory above 2.8 kWh | [10][11] |
| Monoplane over BWB/joined-wing | AR ceiling vs proven reliability | Proven technology, lower fabrication risk, simpler solar integration | [1][18][19][20] |
| GaAs over thin-film solar cells | Efficiency vs weight/flexibility | GaAs 25–30% for primary surfaces; thin-film considered for fuselage | [14][15][43] |

**Critical Trade-off Box (dark bg):**
> "Night-time storage of ~23.9 kWh makes pure lithium-ion solution infeasible [10]:
> - Battery mass: ~95.7 kg at 250 Wh/kg [10][24]
> - Hydrogen system: ~4.3 kg total (1.44 kg H₂ + tankage + BOP) [10][11]
> → Fuel cell selected as primary long-duration storage for multi-day endurance [39]"

---

## SLIDE 14: Results Summary
**Background:** Light steel
**Accent:** Left blue bar

**Results Table:**

| Parameter | Value | Status | Ref |
|-----------|-------|--------|-----|
| Wingspan | 32 m | Design target met | — |
| Aspect Ratio | ~30 | Within literature range (17.4–30+) | [40][3] |
| Structural Mass Estimate | ~47–52 kg (excl. payload) | Benchmarked; requires detailed mass analysis | [40] |
| Endurance | >24 hours | Target achievable per energy balance | [1][2][39] |
| Altitude | 18–22 km | Stratospheric | [1][2] |
| L/D Ratio | 25–30 | Target achievable per EAV-3 benchmark | [40] |
| Cruise Power | ~2 kW | Feasible | [10][11] |
| Solar Power Available | ~9 kW | At 1,360 W/m² stratospheric irradiance | [14][15] |
| Night Storage Required | ~23.9 kWh | Fuel cell solution adopted | [10][11] |
| Fuel Cell System Mass | ~4.3 kg | vs ~95.7 kg battery equivalent | [10][11] |

> ⚠ **Mass Note:** A single unified MTOW figure is not finalised at conceptual stage. The component-level estimate (~57–62 kg incl. payload) and the energy-analysis estimate (~114 kg) reflect different sizing assumptions and require reconciliation in detailed design.

---

## SLIDE 15: Validation & Limitations
**Background:** Light steel
**Accent:** Left blue bar

**Left Column — Validated Conceptually** *(green text)*
- ✓ Energy balance closure verified [39]
- ✓ Power requirements realistic (~2 kW) [10][11]
- ✓ Solar power adequate (~9 kW available) [14][15]
- ✓ Fuel cell mass savings confirmed (~4.3 kg vs ~95.7 kg) [10][11]
- ✓ L/D targets achievable — benchmarked to EAV-3 [40]

**Right Column — Limitations** *(red text)*
- ⚠ No wind tunnel testing performed
- ⚠ No high-fidelity CFD validation completed [5]
- ⚠ No flight testing conducted
- ⚠ Aeroelastic effects modelled at conceptual level only [44]
- ⚠ PV integration losses estimated; manufacturing defects not quantified experimentally [43]
- ⚠ Mass budget not fully reconciled across energy and structural analyses

**Bottom Box (dark bg):**
> "This is a CONCEPTUAL DESIGN study. Detailed computational modelling, prototype fabrication, and experimental flight testing are recommended for full validation."

---

## SLIDE 16: Conclusions
**Background:** Dark navy (`#1B2A4A`)
**Accent:** Left blue bar

**Objectives Achieved:**
- ✓ Comprehensive conceptual design developed [1][2][3][4]
- ✓ Literature review expanded with recent developments [39][40][41][42][43][44][45]
- ✓ Energy system feasibility confirmed — fuel cell solution viable [10][11]
- ✓ Design parameters aligned with established platform benchmarks [40][3]
- ✓ Trade-offs analysed and justified across all subsystems

**Key Findings:**
- Solar-powered HALE UAV is technically feasible for multi-day endurance [1][2][39]
- Hybrid energy storage (fuel cell) is essential over pure batteries for night-time power [10][11]
- Propulsion optimisation can reduce power demand by up to 19% [42]
- High-aspect-ratio wings require careful aeroelastic analysis beyond classical methods [44]
- Photovoltaic integration losses (10–15%) must be factored into solar array sizing [43]

---

## SLIDE 17: Future Work & Recommendations
**Background:** Light steel
**Accent:** Left blue bar

**Near-Term (Research):**
- Detailed CFD and wind tunnel validation under low-Reynolds conditions
- Composite wing segment testing for flutter boundaries and material reliability [44]
- Energy management algorithm development incorporating charge-margin methodology [39]
- Propulsion system optimisation using Dantsker et al. framework [42]

**Long-Term (Development):**
- Coupled aeroelastic–flight dynamic analysis for detailed flutter prediction [44]
- Photovoltaic integration best practices adoption for wing manufacturing [43]
- Scaled demonstrator fabrication for flight testing validation
- Mission system integration and operational scenario testing

**Emerging Technologies to Monitor:** *(Ref: [45])*
- Morphing wings for adaptive aerodynamics
- Solid-state batteries for improved energy density
- Ultra-light flexible solar arrays for conformal integration
- Supercapacitor hybrid storage — eliminating battery degradation [45]

---

## SLIDE 18: Key References
**Background:** Light steel
**Accent:** Left blue bar

**Original Sources:**

[1] Goraj, Z., Frydrychiewicz, A., & Winiecki, J. (1999). Design concept of a HALE UAV. *Aircraft Design*, 2(1), 19–44.

[2] Goraj, Z. (2004). HALE UAV of a new generation. *Bull. Polish Academy of Sciences, Technical Sciences*, 52(3), 173–194.

[3] Romeo, G. et al. (2004). HELIPLAT: Design, aerodynamic, structural analysis. *Journal of Aircraft*, 41(6), 1505–1520.

[4] Najafi, Y. (2011). Design of a HALE Solar Powered UAV (SPACOM). MS Thesis, San Jose State University.

[10] Boukoberine, M. N. et al. (2019). Energy storage systems for UAVs. *Journal of Power Sources*, 613, 234860.

[11] Hassanalian, M., & Abdelkefi, A. (2017). Classifications and design challenges of UAVs. *Progress in Aerospace Sciences*, 91, 99–131.

**Recent Sources:**

[39] Oettershagen, P. et al. (2017). Design of solar-powered UAVs for endurance flight. *Journal of Field Robotics*, 34(2), 291–311.

[40] Hwang, J. et al. (2016). Aerodynamic design of solar-powered HALE UAV (EAV-3). *Journal of Aircraft*, 53(5), 1291–1303.

[41] Mermer, S., & Özgen, S. (2017). Hybrid turbofan/solar HALE UAV concept. *EUCASS Conference*, Milan.

[42] Dantsker, O. D. et al. (2020). Propulsion system optimisation for solar UAVs. *AIAA Propulsion and Energy Forum*.

[43] Łopusiewicz, Ł., & Książek, I. (2024). Photovoltaic integration on composite wing structures. *ICAS 2024*, Florence.

[44] Murua, J. et al. (2011). Stability of very flexible aircraft with wake interference. *AIAA Atmospheric Flight Mechanics Conference*, Portland.

[45] Liller, K. et al. (2025). Battery-free solar UAV with supercapacitor storage. *Scientific Reports*, 15, 90729.

---

## SLIDE 19: Q&A / Thank You
**Background:** Dark navy (`#1B2A4A`)
**Accent:** Thin cyan bar at top

**Content:**
- Title: Questions & Discussion
- Subtitle: Thank You
- Author: Parth Patil | 22BTRAS031
- Advisor: Dr Amalesh Barai, Professor, Department of Aerospace Engineering
- Institution: JAIN (Deemed-to-be University), Faculty of Engineering & Technology

---

## Appendix A: Master Data Reference

| Parameter | Value | Source |
|-----------|-------|---------|
| Wingspan | 32 m | Design sizing |
| Aspect Ratio | ~30 | Design sizing |
| Structural mass estimate | ~47–52 kg (excl. payload) | Component build-up [40] |
| Max Take-off (est.) | ~57–62 kg | With max payload |
| Energy analysis mass ref. | ~114 kg | Section 6.2 feasibility calc. |
| Endurance target | >24 hours | Mission requirement [1][2] |
| Cruise altitude | 18–22 km | Mission requirement [1][2] |
| L/D Ratio target | 25–30 | Aerodynamic sizing [6][7] |
| Cruise speed | ~80 km/h | Design sizing |
| Cruise power | ~2 kW electrical | Energy balance [10][11] |
| Solar power available | ~9 kW | Array sizing [14][15] |
| Stratospheric irradiance | ~1,360 W/m² | High-altitude flux [15] |
| Night storage required | ~23.9 kWh | 12-hr dark period [10] |
| Battery mass (if sole storage) | ~95.7 kg | At 250 Wh/kg [10][24] |
| Fuel cell system mass | ~4.3 kg | H₂ + tankage + BOP [10][11] |
| Hydrogen mass required | ~1.44 kg | LHV calc., 50% efficiency [10][11] |
| Altitude power penalty | ~3.5% per km | [10] |
| Propulsion optimisation gain | 19% efficiency improvement | Dantsker et al. [42] |
| GaAs solar efficiency | 25–30% | [14][15] |
| PV integration derating | 10–15% | Łopusiewicz & Książek [43] |
| EAV-3 static margin | 28.4% SM at 31% MAC | [40] |
| EAV-3 wing tip deflection | 404 mm at 1-G | [40] |

## Appendix B: Changes from Original Version

| Slide | Issue | Fix Applied |
|-------|-------|-------------|
| 5 | Present design mass listed as ~114 kg without qualifier, misleading vs MTOW figures | Added "(structural estimate)" note and explanatory callout |
| 8 | "Joined-wing AR ~40 possible" — unsourced claim not in report | Removed; replaced with supported span-efficiency figure of 1.4–1.5 [20] |
| 10, 14 | Empty weight ~52 kg / MTOW ~62 kg contradicted report's ~114 kg figure | Added clarification note; both figures retained with explanation of their different derivation basis |
| 3–17 | Missing inline references throughout | Added per-slide citations aligned to report reference list |
| 18 | References slide missing [41][42][43][45] cited in slide body | All four added to references slide |
| All | Encoding errors (â€", â€™, etc.) in original file | Corrected to proper Unicode throughout |
