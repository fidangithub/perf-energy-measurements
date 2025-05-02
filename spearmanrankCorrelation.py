import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
import re

# --- Load your dataset ---
df = pd.read_csv('final_energy_results_round.csv')

# --- Classify models ---
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

# --- Models to analyze ---
model_categories = ['human', 'gpt', 'gpt_opt', 'llama', 'llama_opt', 'qwen', 'qwen_opt']
correlation_results = []
plot_data = []

# --- Compute Spearman correlation for each model ---
for model in model_categories:
    model_df = df[df['model'] == model].copy()
    if len(model_df) >= 2:
        rho, pval = spearmanr(model_df['mean_time'], model_df['mean_energy'])
        correlation_results.append({
            'Model': model.upper(),
            'Spearmans rho (ρ)': round(rho, 4),
            'p-value': round(pval, 4)
        })
        model_df['Model'] = model.upper()
        plot_data.append(model_df[['mean_time', 'mean_energy', 'Model']])

# --- Combined correlation ---
all_data = pd.concat(plot_data)
rho_all, pval_all = spearmanr(all_data['mean_time'], all_data['mean_energy'])
correlation_results.append({
    'Model': 'ALL',
    'Spearmans rho (ρ)': round(rho_all, 4),
    'p-value': round(pval_all, 4)
})

# --- Create results table ---
correlation_df = pd.DataFrame(correlation_results)
correlation_df.to_csv('spearman_correlation_results.csv', index=False)
print("Saved: spearman_correlation_results.csv")

# --- Scatterplot ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=all_data, x='mean_time', y='mean_energy', hue='Model', palette='tab10')
plt.title("Energy vs Execution Time Across All Models")
plt.xlabel("Execution Time")
plt.ylabel("Energy Consumption")
plt.legend(title="Model", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('energy_vs_time_scatterplot.png')
plt.show()

print("Saved: energy_vs_time_scatterplot.png")
