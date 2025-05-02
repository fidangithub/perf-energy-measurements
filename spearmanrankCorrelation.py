import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import os

# Load your dataset
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

# Spearman table for each model individually
model_types = ['human', 'gpt', 'gpt_opt', 'llama', 'llama_opt', 'qwen', 'qwen_opt']
spearman_rows = []

for model in model_types:
    model_df = df[df['model'] == model]
    if len(model_df) < 2:
        continue
    rho, pval = spearmanr(model_df['mean_time'], model_df['mean_energy'])
    spearman_rows.append({
        'Model': model.upper(),
        'Spearmans rho (ρ)': round(rho, 4),
        'p-value': round(pval, 4)
    })

# Save Spearman correlation results
correlation_df = pd.DataFrame(spearman_rows)
correlation_df.to_csv('./perf-energy-measurements/spearman_per_model.csv', index=False)

# Grouped plots (visual only, no stats shown)
group_definitions = {
    'Human': ['human'],
    'GPT Default and Optimized': ['gpt', 'gpt_opt'],
    'LLaMA Default and Optimized': ['llama', 'llama_opt'],
    'Qwen Default and Optimized': ['qwen', 'qwen_opt']
}

color_map = {
    'human': 'green',
    'gpt': 'blue',
    'gpt_opt': 'red',
    'llama': 'blue',
    'llama_opt': 'red',
    'qwen': 'blue',
    'qwen_opt': 'red'
}

# Generate scatterplots
for title, models in group_definitions.items():
    group_df = df[df['model'].isin(models)].copy()
    if len(group_df) < 2:
        continue

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=group_df,
        x='mean_time',
        y='mean_energy',
        hue='model',
        palette={m: color_map[m] for m in models}
    )
    plt.title(title)
    plt.xlabel("Execution Time")
    plt.ylabel("Energy Consumption")
    plt.grid(True)
    plt.legend(title="Prompt Type")
    plt.tight_layout()

    safe_name = title.lower().replace(' ', '_')
    plt.savefig(os.path.join(output_dir, f"{safe_name}_scatterplot.png"))
    plt.close()

