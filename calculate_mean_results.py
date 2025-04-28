import pandas as pd

file_path = './perf-energy-measurements/adjusted_energy_results_wide.csv' 
energy_data = pd.read_csv(file_path)

energy_cols = [f'e{i}' for i in range(1, 31)]
time_cols = [f't{i}' for i in range(1, 31)]

energy_data['mean_energy'] = energy_data[energy_cols].mean(axis=1)
energy_data['mean_time'] = energy_data[time_cols].mean(axis=1)

energy_data.to_csv('./perf-energy-measurements/final_energy_results_wide.csv', index=False)

print("Mean energy and mean time have been added and saved to 'final_energy_results_wide.csv'.")
