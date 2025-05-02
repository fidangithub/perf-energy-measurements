import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import os

# Load your data
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Classify model
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

# Create output directory
output_dir = './perf-energy-measurements/spearman_output'
os.makedirs(output_dir, exist_ok=True)

# Analyze model categories
model_categories = ['human', 'gpt', 'gpt_opt', 'llama', 'llama_opt', 'qwen', 'qwen_opt']
correlation_results = []

# Run Spearman correlation and save plots
for model in model_categories:
    model_df = df[df['model'] == model].copy()
    if len(model_df) < 2:
        continue

    rho, pval = spearmanr(model_df['mean_time'], model_df['mean_energy'])
    correlation_results.append({
        'Model': model.upper(),
        'Spearmans rho (ρ)': round(rho, 4),
        'p-value': round(pval, 4)
    })

    # Save scatterplot
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=model_df, x='mean_time', y='mean_energy')
    plt.title(f"{model.upper()} — Spearmans ρ={rho:.3f}, p={pval:.4f}")
    plt.xlabel("Execution Time")
    plt.ylabel("Energy Consumption")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{model}_scatterplot.png"))
    plt.close()

# Save all results to a single CSV
correlation_df = pd.DataFrame(correlation_results)
correlation_df.to_csv('./perf-energy-measurements/spearman_per_model.csv', index=False)

print(f"✅ All scatterplots and Spearman results saved to: {output_dir}/")
