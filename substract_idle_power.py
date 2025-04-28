import pandas as pd

# Load your data
file_path = './perf-energy-measurements/energy_results_wide.csv'  
energy_data = pd.read_csv(file_path)

idle_power = 0.6559  # in watts

adjusted_energy_data = energy_data.copy()

for i in range(1, 31): 
    energy_col = f'e{i}'
    time_col = f't{i}'
    adjusted_col = f'adjusted_e{i}'
    
    adjusted_energy_data[adjusted_col] = energy_data[energy_col] - (idle_power * energy_data[time_col])

adjusted_energy_data.to_csv('./perf-energy-measurements/adjusted_energy_results_wide.csv', index=False)

print("Adjusted energy data has been calculated and saved to 'adjusted_energy_results_wide.csv'.")
