"""
optimiser.py — Propulsion Optimisation Orchestrator & Visualisation

Runs the full Dantsker motor-propeller matching sweep for the HALE UAV
design point and generates a 4-panel results figure.

Usage:
    cd propulsion_optimisation/
    python optimiser.py

Output:
    - propulsion_optimisation_results.png (4-panel figure)
    - propulsion_results_summary.md (Markdown results table)
    - Console summary

Reference:
    Dantsker, O.D. et al. (2020). AIAA Propulsion and Energy Forum [42]
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap

# Import local modules
from propeller_database import load_database
from motor_model import load_motor_database, ESC
from matching_algorithm import (
    DesignPoint, MatchResult, run_parametric_sweep
)


# ===================================================================
# HALE UAV DESIGN PARAMETERS
# ===================================================================

HALE_UAV = {
    'name': 'HALE UAV (Present Design)',
    'weight_kg': 114.0,
    'weight_N': 114.0 * 9.81,       # ~1118 N
    'cruise_speed_kmh': 80.0,
    'cruise_speed_ms': 80.0 / 3.6,  # ~22.2 m/s
    'altitude_km': 20.0,
    'air_density': 0.0889,           # kg/m³ at 20 km
    'L_over_D': 27.5,               # Target L/D (midpoint of 25-30)
    'battery_voltage': 96.0,         # High-voltage HALE bus (24S equiv.)
    'baseline_power': 1994.0,        # Watts — baseline from report
    'avionics_power': 80.0,          # Watts
    'payload_power': 50.0,           # Watts
}

# Derived
HALE_UAV['thrust_required'] = HALE_UAV['weight_N'] / HALE_UAV['L_over_D']


def create_design_point() -> DesignPoint:
    """Create the HALE UAV cruise design point."""
    return DesignPoint(
        thrust_required=HALE_UAV['thrust_required'],
        cruise_speed=HALE_UAV['cruise_speed_ms'],
        air_density=HALE_UAV['air_density'],
        battery_voltage=HALE_UAV['battery_voltage'],
        esc=ESC(efficiency=0.96),
    )


def generate_results_figure(results: list,
                            motors: list,
                            propellers: list,
                            design: DesignPoint):
    """
    Generate a 4-panel results figure:
        1. System efficiency heatmap (motor × propeller)
        2. Power consumption bar chart (top 10)
        3. Baseline vs optimised power budget
        4. Propeller efficiency curves (top 5)
    """

    feasible = [r for r in results if r.feasible]
    if not feasible:
        print("ERROR: No feasible combinations found!")
        return

    fig = plt.figure(figsize=(18, 14))
    fig.patch.set_facecolor('#0d1117')
    gs = gridspec.GridSpec(2, 2, hspace=0.35, wspace=0.30,
                           left=0.07, right=0.95, top=0.92, bottom=0.06)

    # Title
    fig.suptitle('HALE UAV Propulsion Optimisation — Dantsker Framework',
                 fontsize=18, fontweight='bold', color='white', y=0.97)

    # Color palette
    accent = '#58a6ff'
    accent2 = '#f78166'
    accent3 = '#7ee787'
    bg = '#161b22'
    grid_color = '#30363d'

    # ---------------------------------------------------------------
    # PANEL 1: System Efficiency Heatmap
    # ---------------------------------------------------------------
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor(bg)

    # Build efficiency matrix
    n_motors = len(motors)
    n_props = len(propellers)
    eta_matrix = np.full((n_motors, n_props), np.nan)

    for r in results:
        if r.feasible:
            mi = motors.index(r.motor)
            pi = propellers.index(r.propeller)
            eta_matrix[mi, pi] = r.eta_system * 100

    # Custom colormap: dark purple → blue → green → yellow
    cmap = LinearSegmentedColormap.from_list(
        'efficiency',
        ['#1a1a2e', '#16213e', '#0f3460', '#1a936f', '#88d498', '#f6d55c'],
        N=256
    )

    im = ax1.imshow(eta_matrix, aspect='auto', cmap=cmap,
                    interpolation='nearest')
    cbar = plt.colorbar(im, ax=ax1, pad=0.02, shrink=0.85)
    cbar.set_label('System Efficiency (%)', color='white', fontsize=10)
    cbar.ax.tick_params(colors='white', labelsize=8)

    # Labels
    prop_labels = [f"{p.label.split()[1]}" for p in propellers]
    motor_labels = [f"{m.name.split()[-1]}\nKV{m.KV:.0f}" for m in motors]

    ax1.set_xticks(range(n_props))
    ax1.set_xticklabels(prop_labels, rotation=55, ha='right',
                        fontsize=7, color='#c9d1d9')
    ax1.set_yticks(range(n_motors))
    ax1.set_yticklabels(motor_labels, fontsize=7, color='#c9d1d9')
    ax1.set_xlabel('Propeller', color='#c9d1d9', fontsize=10)
    ax1.set_ylabel('Motor', color='#c9d1d9', fontsize=10)
    ax1.set_title('System Efficiency Heatmap', color='white',
                  fontsize=13, fontweight='bold', pad=10)

    # Mark best cell
    best = feasible[0]
    bi = motors.index(best.motor)
    bj = propellers.index(best.propeller)
    ax1.plot(bj, bi, marker='*', color='white', markersize=18,
             markeredgecolor='yellow', markeredgewidth=1.5)

    # ---------------------------------------------------------------
    # PANEL 2: Power Consumption Bar Chart (Top 10)
    # ---------------------------------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor(bg)

    top_n = min(10, len(feasible))
    top = feasible[:top_n]
    labels = [f"{r.propeller.label.split()[1]}\n{r.motor.name.split()[-1]}"
              for r in top]
    powers = [r.power_elec for r in top]
    etas = [r.eta_system * 100 for r in top]

    # Gradient bars
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, top_n))
    bars = ax2.barh(range(top_n), powers, color=colors, edgecolor='#30363d',
                    height=0.7, alpha=0.9)
    ax2.set_yticks(range(top_n))
    ax2.set_yticklabels(labels, fontsize=8, color='#c9d1d9')
    ax2.invert_yaxis()
    ax2.set_xlabel('Electrical Power (W)', color='#c9d1d9', fontsize=10)
    ax2.set_title(f'Top {top_n} Combinations by Power', color='white',
                  fontsize=13, fontweight='bold', pad=10)
    ax2.tick_params(colors='#8b949e', labelsize=8)

    # Annotate with efficiency
    for i, (p, eta) in enumerate(zip(powers, etas)):
        ax2.text(p + 20, i, f'{p:.0f}W  η={eta:.1f}%',
                 va='center', fontsize=8, color=accent3, fontweight='bold')

    # Baseline power line
    ax2.axvline(x=HALE_UAV['baseline_power'], color=accent2, linewidth=2,
                linestyle='--', alpha=0.8, label=f"Baseline: {HALE_UAV['baseline_power']:.0f}W")
    ax2.legend(loc='lower right', fontsize=9, facecolor=bg,
               edgecolor='#30363d', labelcolor='white')

    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_color(grid_color)
    ax2.spines['left'].set_color(grid_color)
    ax2.grid(axis='x', color=grid_color, alpha=0.3)

    # ---------------------------------------------------------------
    # PANEL 3: Baseline vs Optimised Power Budget
    # ---------------------------------------------------------------
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_facecolor(bg)

    best_power = best.power_elec
    baseline_prop = HALE_UAV['baseline_power']
    avionics = HALE_UAV['avionics_power']
    payload = HALE_UAV['payload_power']

    categories = ['Baseline\nDesign', 'Optimised\n(Dantsker)']
    propulsion = [baseline_prop, best_power]
    avionics_vals = [avionics, avionics]
    payload_vals = [payload, payload]

    x = np.arange(len(categories))
    width = 0.45

    bars1 = ax3.bar(x, propulsion, width, label='Propulsion',
                    color='#f78166', edgecolor='#30363d', alpha=0.9)
    bars2 = ax3.bar(x, avionics_vals, width, bottom=propulsion,
                    label='Avionics', color='#58a6ff', edgecolor='#30363d',
                    alpha=0.9)
    bars3 = ax3.bar(x, payload_vals, width,
                    bottom=[p+a for p, a in zip(propulsion, avionics_vals)],
                    label='Payload', color='#7ee787', edgecolor='#30363d',
                    alpha=0.9)

    # Total labels
    for i, (p, a, pl) in enumerate(zip(propulsion, avionics_vals, payload_vals)):
        total = p + a + pl
        ax3.text(i, total + 30, f'{total:.0f} W',
                 ha='center', fontsize=12, color='white', fontweight='bold')

    # Reduction annotation
    reduction_pct = (1 - best_power / baseline_prop) * 100
    night_baseline = (baseline_prop + avionics + payload) * 12 / 1000
    night_optimised = (best_power + avionics + payload) * 12 / 1000

    ax3.annotate(
        f'↓ {reduction_pct:.0f}% propulsion\n'
        f'Night: {night_baseline:.1f}→{night_optimised:.1f} kWh',
        xy=(1, best_power/2), fontsize=10, color=accent3,
        fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=bg,
                  edgecolor=accent3, alpha=0.9)
    )

    ax3.set_xticks(x)
    ax3.set_xticklabels(categories, fontsize=11, color='#c9d1d9')
    ax3.set_ylabel('Power (W)', color='#c9d1d9', fontsize=10)
    ax3.set_title('Power Budget Comparison', color='white',
                  fontsize=13, fontweight='bold', pad=10)
    ax3.legend(loc='upper right', fontsize=9, facecolor=bg,
               edgecolor='#30363d', labelcolor='white')
    ax3.tick_params(colors='#8b949e')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['bottom'].set_color(grid_color)
    ax3.spines['left'].set_color(grid_color)
    ax3.grid(axis='y', color=grid_color, alpha=0.3)

    # ---------------------------------------------------------------
    # PANEL 4: Propeller Efficiency Curves (Top 5)
    # ---------------------------------------------------------------
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor(bg)

    # Get unique top propellers
    seen_props = set()
    top_props = []
    top_ops = []  # Operating J for each
    for r in feasible:
        pid = r.propeller.label
        if pid not in seen_props and len(top_props) < 5:
            seen_props.add(pid)
            top_props.append(r.propeller)
            top_ops.append(r.advance_ratio)

    colors_line = ['#f78166', '#58a6ff', '#7ee787', '#d2a8ff', '#f0e68c']

    for i, (prop, J_op) in enumerate(zip(top_props, top_ops)):
        J_fine = np.linspace(prop.J_data[0], prop.J_data[-1], 100)
        eta_fine = [prop.eta(j) for j in J_fine]
        color = colors_line[i % len(colors_line)]

        ax4.plot(J_fine, eta_fine, color=color, linewidth=2.2,
                 label=f'{prop.label}', alpha=0.9)

        # Mark operating point
        eta_at_op = prop.eta(J_op)
        ax4.plot(J_op, eta_at_op, 'o', color=color, markersize=10,
                 markeredgecolor='white', markeredgewidth=1.5, zorder=5)
        ax4.annotate(f'J={J_op:.2f}\nη={eta_at_op:.0%}',
                     xy=(J_op, eta_at_op),
                     xytext=(J_op + 0.04, eta_at_op - 0.06),
                     fontsize=7, color=color, fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=color, lw=0.8))

    ax4.set_xlabel('Advance Ratio J', color='#c9d1d9', fontsize=10)
    ax4.set_ylabel('Propeller Efficiency η', color='#c9d1d9', fontsize=10)
    ax4.set_title('Propeller η vs J — Top Candidates', color='white',
                  fontsize=13, fontweight='bold', pad=10)
    ax4.set_xlim(0, 1.1)
    ax4.set_ylim(0, 1.0)
    ax4.legend(loc='upper left', fontsize=8, facecolor=bg,
               edgecolor='#30363d', labelcolor='white', ncol=1)
    ax4.tick_params(colors='#8b949e')
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['bottom'].set_color(grid_color)
    ax4.spines['left'].set_color(grid_color)
    ax4.grid(color=grid_color, alpha=0.3)

    # Save
    out_path = os.path.join(os.path.dirname(__file__),
                            'propulsion_optimisation_results.png')
    fig.savefig(out_path, dpi=200, facecolor=fig.get_facecolor(),
                bbox_inches='tight')
    print(f"\n  Figure saved: {out_path}")
    plt.close(fig)


def generate_markdown_summary(results: list, design: DesignPoint):
    """Generate a Markdown summary table of results."""

    feasible = [r for r in results if r.feasible]
    if not feasible:
        return

    best = feasible[0]
    baseline = HALE_UAV['baseline_power']
    reduction_pct = (1 - best.power_elec / baseline) * 100

    lines = []
    lines.append("# Propulsion Optimisation Results")
    lines.append("")
    lines.append("## Design Point")
    lines.append(f"- **Aircraft**: {HALE_UAV['name']}")
    lines.append(f"- **Weight**: {HALE_UAV['weight_kg']:.0f} kg "
                 f"({HALE_UAV['weight_N']:.1f} N)")
    lines.append(f"- **Cruise speed**: {HALE_UAV['cruise_speed_kmh']:.0f} km/h "
                 f"({HALE_UAV['cruise_speed_ms']:.1f} m/s)")
    lines.append(f"- **Altitude**: {HALE_UAV['altitude_km']:.0f} km "
                 f"(ρ = {HALE_UAV['air_density']:.4f} kg/m³)")
    lines.append(f"- **Target L/D**: {HALE_UAV['L_over_D']:.1f}")
    lines.append(f"- **Thrust required**: {design.thrust_required:.1f} N")
    lines.append(f"- **Battery voltage**: {HALE_UAV['battery_voltage']:.0f} V (12S LiPo)")
    lines.append("")
    lines.append("## Optimisation Result")
    lines.append("")
    lines.append(f"**Baseline electrical power**: {baseline:.0f} W")
    lines.append(f"**Optimised electrical power**: {best.power_elec:.0f} W")
    lines.append(f"**Efficiency improvement**: {reduction_pct:.1f}%")
    lines.append("")

    # Night storage impact
    P_total_base = baseline + HALE_UAV['avionics_power'] + HALE_UAV['payload_power']
    P_total_opt = best.power_elec + HALE_UAV['avionics_power'] + HALE_UAV['payload_power']
    E_night_base = P_total_base * 12 / 1000
    E_night_opt = P_total_opt * 12 / 1000

    lines.append("### Night-Time Storage Impact")
    lines.append(f"- Baseline night storage: {E_night_base:.1f} kWh")
    lines.append(f"- Optimised night storage: {E_night_opt:.1f} kWh")
    lines.append(f"- Reduction: {E_night_base - E_night_opt:.1f} kWh "
                 f"({(1-E_night_opt/E_night_base)*100:.1f}%)")
    lines.append(f"- Battery mass saved (at 250 Wh/kg): "
                 f"{(E_night_base-E_night_opt)*1000/250:.1f} kg")
    lines.append("")

    # Best combination details
    lines.append("### Optimal Combination")
    lines.append(f"- **Motor**: {best.motor.name} (KV={best.motor.KV:.0f}, "
                 f"Ra={best.motor.Ra:.3f}Ω, mass={best.motor.mass_g:.0f}g)")
    lines.append(f"- **Propeller**: {best.propeller.label} "
                 f"({best.propeller.diameter*100:.1f} cm diameter)")
    lines.append(f"- **Operating point**: {best.rpm:.0f} RPM, "
                 f"J = {best.advance_ratio:.3f}")
    lines.append(f"- **Motor current**: {best.motor_current:.1f} A at "
                 f"{best.motor_voltage:.0f} V")
    lines.append(f"- **Efficiencies**: η_prop={best.eta_prop:.1%}, "
                 f"η_motor={best.eta_motor:.1%}, η_ESC={best.eta_esc:.1%}, "
                 f"η_sys={best.eta_system:.1%}")
    lines.append("")

    # Top 10 table
    lines.append("## Rankings (Top 10)")
    lines.append("")
    lines.append("| Rank | Motor | Propeller | η_sys (%) | P_elec (W) | "
                 "RPM | J | η_prop (%) | η_motor (%) |")
    lines.append("|------|-------|-----------|-----------|------------|"
                 "-----|---|------------|-------------|")

    for i, r in enumerate(feasible[:10]):
        lines.append(
            f"| {i+1} | {r.motor.name} | {r.propeller.label} | "
            f"{r.eta_system*100:.1f} | {r.power_elec:.0f} | "
            f"{r.rpm:.0f} | {r.advance_ratio:.3f} | "
            f"{r.eta_prop*100:.1f} | {r.eta_motor*100:.1f} |"
        )

    lines.append("")
    lines.append("## Infeasible Combinations")
    infeasible = [r for r in results if not r.feasible]
    if infeasible:
        lines.append(f"\n{len(infeasible)} combinations were infeasible:")
        reasons = {}
        for r in infeasible:
            reasons[r.reason] = reasons.get(r.reason, 0) + 1
        for reason, count in sorted(reasons.items(), key=lambda x: -x[1]):
            lines.append(f"- {reason}: {count}")
    lines.append("")
    lines.append("---")
    lines.append("*Generated by Dantsker Framework Propulsion Optimiser*")
    lines.append(f"*Reference: Dantsker, O.D. et al. (2020), AIAA [42]*")

    out_path = os.path.join(os.path.dirname(__file__),
                            'propulsion_results_summary.md')
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"  Summary saved: {out_path}")


def main():
    """Run the full propulsion optimisation."""

    print("\n" + "=" * 70)
    print("  HALE UAV PROPULSION OPTIMISATION")
    print("  Method: Dantsker Motor-Propeller Matching Framework")
    print("  Reference: Dantsker et al. (2020), AIAA [42]")
    print("=" * 70)
    print(f"\n  Aircraft: {HALE_UAV['name']}")
    print(f"  Weight: {HALE_UAV['weight_kg']:.0f} kg "
          f"({HALE_UAV['weight_N']:.1f} N)")
    print(f"  Cruise: {HALE_UAV['cruise_speed_kmh']:.0f} km/h at "
          f"{HALE_UAV['altitude_km']:.0f} km altitude")
    print(f"  L/D: {HALE_UAV['L_over_D']:.1f} → Thrust: "
          f"{HALE_UAV['thrust_required']:.1f} N")
    print(f"  Baseline power: {HALE_UAV['baseline_power']:.0f} W")

    # Load databases
    print("\n--- Loading databases ---")
    propellers = load_database()
    motors = load_motor_database()
    print(f"  Propellers: {len(propellers)}")
    print(f"  Motors: {len(motors)}")

    # Create design point
    design = create_design_point()

    # Run parametric sweep
    results = run_parametric_sweep(motors, propellers, design)

    # Generate outputs
    print("\n--- Generating results ---")
    generate_results_figure(results, motors, propellers, design)
    generate_markdown_summary(results, design)

    # Final summary
    feasible = [r for r in results if r.feasible]
    if feasible:
        best = feasible[0]
        baseline = HALE_UAV['baseline_power']
        improvement = (1 - best.power_elec / baseline) * 100

        print(f"\n{'='*70}")
        print(f"  ✓ OPTIMISATION COMPLETE")
        print(f"{'='*70}")
        print(f"  Best combination: {best.label}")
        print(f"  System efficiency: {best.eta_system*100:.1f}%")
        print(f"  Electrical power: {best.power_elec:.0f} W "
              f"(baseline: {baseline:.0f} W)")
        print(f"  Improvement: {improvement:.1f}%")
        print(f"  Operating: {best.rpm:.0f} RPM, J = {best.advance_ratio:.3f}")
        print(f"{'='*70}\n")
    else:
        print("\n  ✗ No feasible combinations found. Check design parameters.")


if __name__ == "__main__":
    main()
