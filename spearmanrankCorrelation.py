import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load your data ---
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# --- Classify model type ---
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

# --- Define model categories ---
model_categories = ['human', 'gpt', 'gpt_opt', 'llama', 'llama_opt', 'qwen', 'qwen_opt']

# --- Plot per model ---
for model in model_categories:
    model_df = df[df['model'] == model].copy()
    if len(model_df) < 2:
        continue  # skip if not enough points

    rho, pval = spearmanr(model_df['mean_time'], model_df['mean_energy'])
    correlation_results.append({
        'Model': model.upper(),
        'Spearman’s rho (ρ)': round(rho, 4),
        'p-value': round(pval, 4)
    })

    # Plot
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=model_df, x='mean_time', y='mean_energy')
    plt.title(f"{model.upper()} — Spearmans ρ={rho:.3f}, p={pval:.4f}")
    plt.xlabel("Execution Time")
    plt.ylabel("Energy Consumption")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{model}_scatterplot.png")
    plt.show()

print("All plots saved as individual PNG files.")
