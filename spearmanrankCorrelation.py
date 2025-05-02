import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import os

# Load your data
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Classify models
def classify_model(script):
    if '_gpt_opt' in script:
        return 'gpt_opt'
    elif '_gpt' in script:
        return 'gpt'
    elif '_llama_opt' in script:
        return 'llama_opt'
    elif '_llama' in script:
        return 'llama'
    elif '_qwen_opt' in script:
        return 'qwen_opt'
    elif '_qwen' in script:
        return 'qwen'
    else:
        return 'human'

df['model'] = df['script'].apply(classify_model)
df['lang'] = df['script'].apply(lambda x: x.split('.')[-1])

# Output folder
output_dir = './perf-energy-measurements/spearman_output'
os.makedirs(output_dir, exist_ok=True)

# Group definitions: model label and members
model_groups = {
    'Human': ['human'],
    'GPT Default vs Optimized': ['gpt', 'gpt_opt'],
    'LLaMA Default vs Optimized': ['llama', 'llama_opt'],
    'Qwen Default vs Optimized': ['qwen', 'qwen_opt'],
}

# Color mapping
color_map = {
    'human': 'gray',
    'gpt': 'blue',
    'gpt_opt': 'blue',
    'llama': 'green',
    'llama_opt': 'green',
    'qwen': 'red',
    'qwen_opt': 'red',
}

correlation_results = []

# Process each group
for title, members in model_groups.items():
    group_df = df[df['model'].isin(members)].copy()
    if len(group_df) < 2:
        continue

    # Compute Spearman correlation
    rho, pval = spearmanr(group_df['mean_time'], group_df['mean_energy'])
    correlation_results.append({
        'Model': title,
        'Spearman’s rho (ρ)': round(rho, 4),
        'p-value': round(pval, 4)
    })

    # Scatterplot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=group_df,
        x='mean_time',
        y='mean_energy',
        hue='model',
        palette={m: color_map[m] for m in members}
    )
    plt.title(f"{title} — Spearman’s ρ={rho:.3f}, p={pval:.4f}")
    plt.xlabel("Execution Time")
    plt.ylabel("Energy Consumption")
    plt.grid(True)
    plt.legend(title="Prompt Type")
    plt.tight_layout()
    safe_name = title.lower().replace(' ', '_').replace('vs', 'vs_')
    plt.savefig(os.path.join(output_dir, f"{safe_name}_scatterplot.png"))
    plt.close()

# Save correlation results
correlation_df = pd.DataFrame(correlation_results)
correlation_df.to_csv('./perf-energy-measurements/spearman_per_model.csv', index=False)

print(f"✅ All grouped scatterplots and correlation results saved to: {output_dir}/")
