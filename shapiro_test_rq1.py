import pandas as pd
from scipy.stats import shapiro

def load_data(filepath):
    return pd.read_csv(filepath)

def apply_shapiro(group_data, group_name, variable_name):
    stat, p = shapiro(group_data)
    print(f"Shapiro-Wilk Test for {group_name} - {variable_name}")
    print(f"  Test Statistic: {stat:.4f}, p-value: {p:.4f}")
    if p > 0.05:
        print(f"  Result: Data looks Gaussian (fail to reject H0)\n")
    else:
        print(f"  Result: Data does not look Gaussian (reject H0)\n")

def main():
    filepath = "./perf-energy-measurements/rq1_matched_groups.csv"  # The combined CSV you generated earlier
    data = load_data(filepath)

    comparisons = {
        'Human vs GPT': ('human_gpt', 'gpt'),
        'Human vs LLaMA': ('human_llama', 'llama'),
        'Human vs Qwen': ('human_qwen', 'qwen'),
    }

    for comp_name, (group1, group2) in comparisons.items():
        print(f"\n===== {comp_name} =====")

        group1_data = data[data['group'] == group1]
        group2_data = data[data['group'] == group2]

        # Apply Shapiro test for mean_energy
        apply_shapiro(group1_data['mean_energy'], group1, 'mean_energy')
        apply_shapiro(group2_data['mean_energy'], group2, 'mean_energy')

        # Apply Shapiro test for mean_time
        apply_shapiro(group1_data['mean_time'], group1, 'mean_time')
        apply_shapiro(group2_data['mean_time'], group2, 'mean_time')

if __name__ == "__main__":
    main()
