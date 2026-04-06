import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_solar_irradiance(time_hours, day_of_year=172, latitude_deg=47.38, k_c=0.0):
    """
    Calculates the solar irradiance hitting a horizontal surface.
    
    Parameters:
    - time_hours (float or np.array): Time of day in hours (0 to 24).
    - day_of_year (int): Day of the year (1-365). 172 represents the summer solstice.
    - latitude_deg (float): Latitude of the location in degrees (Default: 47.38 for Zurich).
    - k_c (float or np.array): Cloud cover disturbance factor (0.0 = clear sky, 1.0 = total block).
    
    Returns:
    - I_horizontal (np.array): Solar irradiance in W/m^2.
    """
    # Constants
    S_0 = 1361.0  # Solar constant (W/m^2)
    rho_at = 0.7  # Average atmospheric transmittance

    # Conversions
    lat_rad = np.radians(latitude_deg)
    
    # Solar declination angle calculation (approximate)
    declination_deg = 23.45 * np.sin(np.radians(360.0 / 365.0 * (day_of_year + 284)))
    decl_rad = np.radians(declination_deg)
    
    # Hour angle calculation
    # Define solar noon as time = 12.0
    hour_angle_deg = 15.0 * (time_hours - 12.0)
    hour_angle_rad = np.radians(hour_angle_deg)
    
    # Solar elevation angle
    sin_eval = np.sin(lat_rad) * np.sin(decl_rad) + np.cos(lat_rad) * np.cos(decl_rad) * np.cos(hour_angle_rad)
    elevation_rad = np.arcsin(np.clip(sin_eval, -1.0, 1.0))
    
    # Initialize irradiance arrays
    I_horizontal = np.zeros_like(time_hours, dtype=float)
    
    # Daytime check
    daytime_mask = elevation_rad > 0
    
    # Clear sky irradiance component (using AM1.5 generic atmospheric model)
    # AM (Air Mass) approximation
    AM = 1.0 / np.sin(elevation_rad[daytime_mask])
    
    # Direct irradiance normal to sun
    I_direct = S_0 * (rho_at ** AM)
    
    # Projected onto a horizontal plane (like a top-mounted flat solar wing)
    I_horizontal[daytime_mask] = I_direct * np.sin(elevation_rad[daytime_mask])
    
    # Apply Cloud Cover Disturbance (k_c)
    # k_c reduces the irradiance directly. k_c = 0 means fully clear.
    # Note: k_c could be a scalar or an array matching time_hours shape.
    I_disturbed = I_horizontal * (1.0 - k_c)
    
    # Ensure no negative irradiance
    I_disturbed = np.clip(I_disturbed, 0, None)
    
    return I_disturbed

def run_simulation_and_plot():
    # Simulation span: 24 hours at 0.1 hour increments
    time_span = np.linspace(0, 24, 241)
    
    # Case 1: Ideal clear sky (k_c = 0)
    ideal_irradiance = calculate_solar_irradiance(time_span, k_c=0.0)
    
    # Case 2: Uniform mild cloud cover (k_c = 0.3)
    mild_cloud_cover = calculate_solar_irradiance(time_span, k_c=0.3)
    
    # Case 3: Dynamic weather disturbance (e.g., storms roll in afternoon)
    # 0% clouds morning, building up to 80% around 15:00-18:00
    dynamic_kc = np.zeros_like(time_span)
    for i, t in enumerate(time_span):
        if t < 10.0:
            dynamic_kc[i] = 0.0
        elif 10.0 <= t < 14.0:
            dynamic_kc[i] = 0.4 * (t - 10.0) / 4.0 # Ramp up to 40%
        elif 14.0 <= t < 19.0:
            dynamic_kc[i] = 0.8  # Heavy cloud disturbance
        else:
            dynamic_kc[i] = 0.2  # Clearing up slightly at sunset
            
    dynamic_irradiance = calculate_solar_irradiance(time_span, k_c=dynamic_kc)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    plt.plot(time_span, ideal_irradiance, 'k--', label='Ideal Clear Sky ($k_c = 0.0$)')
    plt.plot(time_span, mild_cloud_cover, 'b-.', label='Uniform Cloud Disturbance ($k_c = 0.3$)')
    plt.plot(time_span, dynamic_irradiance, 'r-', linewidth=2, label='Dynamic Afternoon Disturbance')
    
    plt.axhline(0, color='grey', linewidth=0.5)
    plt.title('24-Hour Solar Irradiance Model')
    plt.xlabel('Time of Day (Hours)')
    plt.ylabel('Horizontal Irradiance ($W/m^2$)')
    plt.xlim(0, 24)
    plt.ylim(0, 1000)
    plt.xticks(np.arange(0, 25, 2))
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('solar_irradiance_model.png', dpi=300)
    print("Simulation complete. Plot saved as 'solar_irradiance_model.png'")

if __name__ == "__main__":
    run_simulation_and_plot()
