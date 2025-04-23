import pandas as pd

# Load your long-format result log
df = pd.read_csv("perf-energy-measurements/energy_results.log")

# Sort to ensure runs are in order
df = df.sort_values(by=["script", "run_id"])

# Initialize result structure
rows = {}

for _, row in df.iterrows():
    key = (row["script"], row["language"])
    run_id = int(row["run_id"])

    if key not in rows:
        rows[key] = {}

    rows[key][f"e{run_id}"] = row["energy_joules"]
    rows[key][f"t{run_id}"] = row["time_seconds"]

# Convert to wide-format DataFrame
final_rows = []
for (script, language), data in rows.items():
    row = {"script": script, "language": language}
    row.update(data)
    final_rows.append(row)

out_df = pd.DataFrame(final_rows)

# Save it
out_df.to_csv("perf-energy-measurements/energy_results_wide.csv", index=False)
print("✅ Wide-format results saved.")
