## HALE UAV PROPULSION OPTIMISATION
Method: Dantsker Motor-Propeller Matching Framework
Reference: Dantsker et al. (2020), AIAA [42]

Aircraft: HALE UAV (Present Design) \
Weight: 114 kg (1118.3 N) \
Cruise: 80 km/h at 20 km altitude \
L/D: 27.5 → Thrust: 40.7 N \
Baseline power: 1994 W 

--- Loading databases ---
Propellers: 12 \
Motors: 8 


  DANTSKER PROPULSION OPTIMISATION — PARAMETRIC SWEEP \
  Design Point: T=40.7N, V=22.2m/s, ρ=0.0889kg/m³, Vbat=96V \
  Motor candidates: 8 \
  Propeller candidates: 12 \
  Total combinations: 96 

  Feasible combinations: 10 / 96 (10%)

##  Failure breakdown:
    Motor outside operating limits: 74 \
    Cannot produce 40.7N thrust: 12 \
###  BEST:  HALE-Direct D80 + HALE-M 72x40 \
         η_sys = 58.6%, P_elec = 1543 W \
         RPM = 1499, J = 0.487 \
         η_prop = 79.5%, η_motor = 76.7% \
###  WORST: T-Motor U15 XXL + HALE-HP 48x36 \
         η_sys = 47.6%, P_elec = 1897 W \

  Efficiency improvement (best vs worst): 18.7%

## Generating results
Figure saved: [Results](propulsion_optimisation_results.png)  
Summary saved: [Results](propulsion_results_summary.md)

  OPTIMISATION COMPLETE

  Best combination: HALE-Direct D80 + HALE-M 72x40  \
  System efficiency: 58.6% \
  Electrical power: 1543 W (baseline: 1994 W) \
  Improvement: 22.6% \
  Operating: 1499 RPM, J = 0.487
