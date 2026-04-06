
## DANTSKER PROPULSION OPTIMISATION — PARAMETRIC SWEEP

Design Point: T=40.7N, V=22.2m/s, ρ=0.0889kg/m³, Vbat=96V \
Motor candidates: 8 \
Propeller candidates: 12 \
Total combinations: 96 

## Feasible combinations: 13 / 96 (14%)

## Failure breakdown:
    - Insufficient torque: 39
    - Motor outside operating limits: 32
    - Cannot produce 40.7N thrust: 12

## BEST:  T-Motor AT5220 + HALE-ST 40x18
         η_sys = 34.5%, P_elec = 2622 W
         RPM = 4144, J = 0.316
         η_prop = 63.3%, η_motor = 56.7%

## WORST: Scorpion HALE-4030 + HALE-HP 72x54
         η_sys = 18.7%, P_elec = 4828 W

  Efficiency improvement (best vs worst): 45.7%


##  TOP 10 COMBINATIONS
Rank | Combination                               |         η_sys(%) |  P_elec(W) | RPM    |  J      |  η_prop |  η_motor |
-----|-------------------------------------------|------------------|------------|--------|---------|---------|----------|
1    | T-Motor AT5220 + HALE-ST 40x18            |         34.5     |  2622      | 4144   |  0.316  |  63.3   |  56.7    |
2    | Scorpion HALE-4030 + HALE-ST 48x22        |         34.4     |  2629      | 2993   |  0.365  |  70.1   |  51.1    |
3    | T-Motor U13 HALE + HALE-ST 60x27          |         32.7     |  2763      | 2038   |  0.429  |  78.2   |  43.6    |
4    | Scorpion HALE-4030 + HALE-M 48x28         |         31.7     |  2849      | 2971   |  0.368  |  65.2   |  50.7    |
5    | Scorpion HALE-4030 + HALE-HP 48x36        |         30.0     |  3010      | 2731   |  0.400  |  67.0   |  46.7    |
6    | T-Motor AT5220 + HALE-ST 48x22            |         27.7     |  3265      | 2993   |  0.365  |  70.1   |  41.1    |
7    | Scorpion HALE-4030 + HALE-ST 60x27        |         26.2     |  3447      | 2038   |  0.429  |  78.2   |  34.9    |
8    | T-Motor AT5220 + HALE-M 48x28             |         25.5     |  3538      | 2971   |  0.368  |  65.2   |  40.8    |
9    | Scorpion HALE-4030 + HALE-M 60x33         |         24.4     |  3708      | 2024   |  0.432  |  73.2   |  34.7    |
10   | T-Motor AT5220 + HALE-HP 48x36            |         24.2     |  3741      | 2731   |  0.400  |  67.0   |  37.6    |