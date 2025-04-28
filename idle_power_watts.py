# Python example:
import pandas as pd

df = pd.read_csv("./perf-energy-measurements/idle_energy_results.csv")
avg_joules = df["energy_joules"].mean()
avg_time = df["time_seconds"].mean()
idle_power_watts = avg_joules / avg_time

print(f"Average Idle Power: {idle_power_watts:.4f} Watts")


# Average Idle Power: 0.6559 Watts