"""
visualization.py — Plotting Utilities

Generates time-series plots for simulation results.
Uses matplotlib for visualization.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional, Union


# Set style for publication-quality plots
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})


def plot_atmosphere(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Plot atmospheric properties vs time.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    # Temperature
    axes[0].plot(df['time_hours'], df['temperature_K'], 'b-', linewidth=2)
    axes[0].set_ylabel('Temperature (K)')
    axes[0].set_title('Atmospheric Properties vs Time')
    axes[0].grid(True, alpha=0.3)

    # Pressure
    axes[1].plot(df['time_hours'], df['pressure_Pa'] / 1000, 'g-', linewidth=2)
    axes[1].set_ylabel('Pressure (kPa)')
    axes[1].grid(True, alpha=0.3)

    # Density
    axes[2].plot(df['time_hours'], df['density_kgm3'], 'r-', linewidth=2)
    axes[2].set_ylabel('Density (kg/m³)')
    axes[2].set_xlabel('Time (hours)')
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


def plot_solar(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Plot solar irradiance and power generation.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # Irradiance
    axes[0].fill_between(df['time_hours'], df['solar_irradiance_Wm2'],
                          alpha=0.3, color='orange')
    axes[0].plot(df['time_hours'], df['solar_irradiance_Wm2'], 'orange', linewidth=2)
    axes[0].set_ylabel('Solar Irradiance (W/m²)')
    axes[0].set_title('Solar Conditions vs Time')
    axes[0].set_ylim(0, max(df['solar_irradiance_Wm2']) * 1.1)
    axes[0].grid(True, alpha=0.3)

    # Power generated
    axes[1].fill_between(df['time_hours'], df['power_generated_W'],
                          alpha=0.3, color='gold')
    axes[1].plot(df['time_hours'], df['power_generated_W'], 'gold', linewidth=2)
    axes[1].set_ylabel('Power Generated (W)')
    axes[1].set_xlabel('Time (hours)')
    axes[1].set_ylim(0, max(df['power_generated_W']) * 1.1)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


def plot_aerodynamics(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Plot aerodynamic forces and coefficients.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Lift
    axes[0, 0].plot(df['time_hours'], df['lift_N'], 'b-', linewidth=2)
    axes[0, 0].set_ylabel('Lift (N)')
    axes[0, 0].set_title('Aerodynamic Forces')
    axes[0, 0].grid(True, alpha=0.3)

    # Drag
    axes[0, 1].plot(df['time_hours'], df['drag_N'], 'r-', linewidth=2)
    axes[0, 1].set_ylabel('Drag (N)')
    axes[0, 1].set_title('Drag Force')
    axes[0, 1].grid(True, alpha=0.3)

    # CL
    axes[1, 0].plot(df['time_hours'], df['CL'], 'b--', linewidth=1.5)
    axes[1, 0].set_ylabel('$C_L$')
    axes[1, 0].set_xlabel('Time (hours)')
    axes[1, 0].set_title('Lift Coefficient')
    axes[1, 0].grid(True, alpha=0.3)

    # CD
    axes[1, 1].plot(df['time_hours'], df['CD'], 'r--', linewidth=1.5)
    axes[1, 1].set_ylabel('$C_D$')
    axes[1, 1].set_xlabel('Time (hours)')
    axes[1, 1].set_title('Drag Coefficient')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


def plot_power(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Plot power required vs power generated.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    # Power comparison
    axes[0].plot(df['time_hours'], df['power_required_W'], 'r-',
                 linewidth=2, label='Power Required')
    axes[0].plot(df['time_hours'], df['power_generated_W'], 'gold',
                 linewidth=2, label='Power Generated')
    axes[0].fill_between(df['time_hours'], df['power_generated_W'],
                          df['power_required_W'],
                          where=df['power_generated_W'] >= df['power_required_W'],
                          alpha=0.3, color='green', label='Surplus')
    axes[0].fill_between(df['time_hours'], df['power_generated_W'],
                          df['power_required_W'],
                          where=df['power_generated_W'] < df['power_required_W'],
                          alpha=0.3, color='red', label='Deficit')
    axes[0].set_ylabel('Power (W)')
    axes[0].set_title('Power Balance')
    axes[0].legend(loc='upper right')
    axes[0].grid(True, alpha=0.3)

    # Energy balance
    axes[1].plot(df['time_hours'], df['energy_balance_Wh'], 'k-', linewidth=2)
    axes[1].axhline(0, color='gray', linestyle='--', linewidth=1)
    axes[1].set_ylabel('Cumulative Energy (Wh)')
    axes[1].set_xlabel('Time (hours)')
    axes[1].set_title('Energy Balance')
    axes[1].grid(True, alpha=0.3)

    # Fill regions
    pos_mask = df['energy_balance_Wh'] >= 0
    axes[1].fill_between(df['time_hours'], df['energy_balance_Wh'],
                          where=pos_mask, alpha=0.3, color='green')
    axes[1].fill_between(df['time_hours'], df['energy_balance_Wh'],
                          where=~pos_mask, alpha=0.3, color='red')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


def plot_energy(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Plot detailed energy analysis.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    # Energy balance
    ax.plot(df['time_hours'], df['energy_balance_Wh'], 'k-', linewidth=2)
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)

    # Mark positive and negative regions
    pos_mask = df['energy_balance_Wh'] >= 0
    ax.fill_between(df['time_hours'], df['energy_balance_Wh'],
                    where=pos_mask, alpha=0.3, color='green', label='Energy Surplus')
    ax.fill_between(df['time_hours'], df['energy_balance_Wh'],
                    where=~pos_mask, alpha=0.3, color='red', label='Energy Deficit')

    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Cumulative Energy (Wh)')
    ax.set_title('Mission Energy Balance')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


def plot_all(
    df: pd.DataFrame,
    save_dir: str = "."
) -> None:
    """
    Generate all plots and save to directory.

    Parameters:
        df: Simulation results DataFrame
        save_dir: Directory to save figures
    """
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    plot_atmosphere(df, save_path=str(save_dir / "atmosphere.png"), show=False)
    plot_solar(df, save_path=str(save_dir / "solar.png"), show=False)
    plot_aerodynamics(df, save_path=str(save_dir / "aerodynamics.png"), show=False)
    plot_power(df, save_path=str(save_dir / "power.png"), show=False)
    plot_energy(df, save_path=str(save_dir / "energy.png"), show=False)

    print(f"All plots saved to {save_dir}")


def plot_summary_dashboard(
    df: pd.DataFrame,
    save_path: Optional[str] = None,
    show: bool = True
) -> plt.Figure:
    """
    Create a comprehensive summary dashboard.

    Parameters:
        df: Simulation results DataFrame
        save_path: Path to save figure (optional)
        show: Display figure

    Returns:
        matplotlib Figure
    """
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    # 1. Atmospheric properties (top left, spans 2 cols)
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(df['time_hours'], df['density_kgm3'], 'b-', linewidth=2, label='Density')
    ax1.set_ylabel('Density (kg/m³)')
    ax1.set_title('Atmospheric Conditions')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    ax1.set_xlabel('Time (hours)')

    # Temperature on secondary axis
    ax1b = ax1.twinx()
    ax1b.plot(df['time_hours'], df['temperature_K'], 'r--', linewidth=1.5)
    ax1b.set_ylabel('Temperature (K)', color='r')
    ax1b.tick_params(axis='y', labelcolor='r')

    # 2. Solar (top right)
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.fill_between(df['time_hours'], df['solar_irradiance_Wm2'],
                      alpha=0.3, color='orange')
    ax2.plot(df['time_hours'], df['solar_irradiance_Wm2'], 'orange', linewidth=2)
    ax2.set_ylabel('Irradiance (W/m²)')
    ax2.set_title('Solar Irradiance')
    ax2.set_xlabel('Time (hours)')
    ax2.grid(True, alpha=0.3)

    # 3. Aerodynamics (middle left)
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.plot(df['time_hours'], df['lift_N'], 'b-', linewidth=2, label='Lift')
    ax3.plot(df['time_hours'], df['drag_N'], 'r-', linewidth=2, label='Drag')
    ax3.set_ylabel('Force (N)')
    ax3.set_title('Forces')
    ax3.legend(loc='upper right')
    ax3.set_xlabel('Time (hours)')
    ax3.grid(True, alpha=0.3)

    # 4. CL/CD (middle center)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.plot(df['time_hours'], df['CL'], 'b-', linewidth=2, label='$C_L$')
    ax4.plot(df['time_hours'], df['CD'] * 10, 'r-', linewidth=2, label='$C_D \\times 10$')
    ax4.set_ylabel('Coefficient')
    ax4.set_title('Aerodynamic Coefficients')
    ax4.legend(loc='upper right')
    ax4.set_xlabel('Time (hours)')
    ax4.grid(True, alpha=0.3)

    # 5. Power (middle right)
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.plot(df['time_hours'], df['power_required_W'], 'r-', linewidth=2, label='Required')
    ax5.plot(df['time_hours'], df['power_generated_W'], 'gold', linewidth=2, label='Generated')
    ax5.set_ylabel('Power (W)')
    ax5.set_title('Power Balance')
    ax5.legend(loc='upper right')
    ax5.set_xlabel('Time (hours)')
    ax5.grid(True, alpha=0.3)

    # 6. Energy (bottom, spans full width)
    ax6 = fig.add_subplot(gs[2, :])
    ax6.plot(df['time_hours'], df['energy_balance_Wh'], 'k-', linewidth=2)
    ax6.axhline(0, color='gray', linestyle='--', linewidth=1)
    pos_mask = df['energy_balance_Wh'] >= 0
    ax6.fill_between(df['time_hours'], df['energy_balance_Wh'],
                      where=pos_mask, alpha=0.3, color='green')
    ax6.fill_between(df['time_hours'], df['energy_balance_Wh'],
                      where=~pos_mask, alpha=0.3, color='red')
    ax6.set_ylabel('Cumulative Energy (Wh)')
    ax6.set_xlabel('Time (hours)')
    ax6.set_title('Energy Balance')
    ax6.grid(True, alpha=0.3)

    plt.suptitle('HALE UAV Mission Simulation Dashboard', fontsize=14, fontweight='bold')

    if save_path:
        plt.savefig(save_path)
        print(f"Saved: {save_path}")

    if show:
        plt.show()

    return fig


# Test function
if __name__ == "__main__":
    print("=== Visualization Test ===\n")

    from simulation import run_default_simulation

    results, summary = run_default_simulation()
    df = results.to_dataframe()

    print("Generating plots...")
    plot_summary_dashboard(df, save_path="simulation_dashboard.png", show=False)
    print("Dashboard saved to simulation_dashboard.png")