import pandas as pd

file_path = './perf-energy-measurements/energy_results_wide.csv' 
energy_data = pd.read_csv(file_path)

idle_power = 0.6559 

for i in range(1, 31): 
    energy_col = f'e{i}'
    time_col = f't{i}'
    
    energy_data[energy_col] = energy_data[energy_col] - (idle_power * energy_data[time_col])

energy_data.to_csv('./perf-energy-measurements/adjusted_energy_results_wide.csv', index=False)

print("Original energy columns have been adjusted and saved to 'adjusted_energy_results_wide.csv'.")
