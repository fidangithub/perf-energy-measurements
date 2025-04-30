
import pandas as pd
from scipy.stats import mannwhitneyu

# Function to calculate Cliff's Delta
def cliffs_delta(x, y):
    x = list(map(float, x))
    y = list(map(float, y))
    m, n = len(x), len(y)
    greater = sum(1 for xi in x for yj in y if xi > yj)
    less = sum(1 for xi in x for yj in y if xi < yj)
    delta = (greater - less) / (m * n)
    print(f"Cliff's Delta Debug - len(x): {m}, len(y): {n}, greater: {greater}, less: {less}, delta: {delta}")
    return round(delta, 4)

# Load your CSV file
df = pd.read_csv("./perf-energy-measurements/rq1_matched_groups.csv")

# Define model comparisons
models = ['gpt', 'llama', 'qwen']
results = []

# Perform tests
for model in models:
    human_group = df[df['group'] == f'human_{model}']
    model_group = df[df['group'] == model]
    
    for metric in ['mean_energy', 'mean_time']:
        # Mann-Whitney U Test
        u_stat, p_val = mannwhitneyu(human_group[metric], model_group[metric], alternative='two-sided')
        # Cliff's Delta
        delta = cliffs_delta(human_group[metric].values, model_group[metric].values)
        
        
        results.append({
            'Comparison': f'human_{model} vs {model}',
            'Metric': metric,
            'U-Statistic': u_stat,
            'p-Value': p_val,
            'Cliffs Delta': delta
        })

# Output results
results_df = pd.DataFrame(results)
results_df.to_csv("./perf-energy-measurements/statistical_test_results.csv", index=False)
print("Results saved to statistical_test_results.csv")