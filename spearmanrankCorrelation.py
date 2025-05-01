import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import re

df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# --- Extract model and language from script name ---
def extract_info(script):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen)?\.(\w+)$", script)
    if match:
        base = match.group(1)
        model = match.group(2)[1:] if match.group(2) else None
        lang = match.group(3)
        return pd.Series([base, model, lang])
    return pd.Series([script, 'unknown', ''])

df[['base_task', 'model', 'lang']] = df['script'].apply(extract_info)

# --- Define models to compare ---
models = ['gpt', 'llama', 'qwen']
results = []
plot_data = []

# --- Calculate Spearman's rho for each model ---
for model in models:
    model_df = df[df['model'] == model].copy()
    rho, pval = spearmanr(model_df['mean_time'], model_df['mean_energy'])

    results.append({
        'Model': model.upper(),
        'Spearman’s rho (ρ)': round(rho, 4),
        'p-value': round(pval, 4)
    })

    model_df['Model'] = model.upper()
    plot_data.append(model_df[['mean_time', 'mean_energy', 'Model']])

# --- Combined analysis ---
all_data = pd.concat(plot_data)
rho_all, pval_all = spearmanr(all_data['mean_time'], all_data['mean_energy'])

results.append({
    'Model': 'ALL',
    'Spearmans rho (ρ)': round(rho_all, 4),
    'p-value': round(pval_all, 4)
})

# --- Create summary table ---
correlation_df = pd.DataFrame(results)
correlation_df.to_csv('./perf-energy-measurements/spearman_correlation_results.csv', index=False)
print("Saved: spearman_correlation_results.csv")

# --- Scatterplot ---
plt.figure(figsize=(8, 6))
sns.scatterplot(data=all_data, x='mean_time', y='mean_energy', hue='Model', palette='deep')
plt.title("Energy vs Execution Time (All Models)")
plt.xlabel("Execution Time")
plt.ylabel("Energy Consumption")
plt.legend(title="Model")
plt.grid(True)
plt.tight_layout()
plt.savefig('./perf-energy-measurements/energy_vs_time_scatterplot.png')
plt.show()

print("Saved: energy_vs_time_scatterplot.png")
