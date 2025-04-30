
import pandas as pd
from scipy.stats import mannwhitneyu

# Function to calculate Cliff's Delta
def cliffs_delta(x, y):
    m, n = len(x), len(y)
    greater = sum(i > j for i in x for j in y)
    less = sum(i < j for i in x for j in y)
    return (greater - less) / (m * n)

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