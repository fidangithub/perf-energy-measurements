import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import re

# Load detailed data file
df = pd.read_csv('./perf-energy-measurements/final_energy_results_wide.csv')

# Extract base task, model type, and language
def extract_info(script):
    match = re.match(r"^(.*?)(_gpt_opt|_llama_opt|_qwen_opt|_gpt|_llama|_qwen)?\.(\w+)$", script)
    if match:
        base = match.group(1)
        model = match.group(2)[1:] if match.group(2) else 'unknown'
        lang = match.group(3)
        return pd.Series([base, model, lang])
    return pd.Series([script, 'unknown', ''])

df[['base_task', 'model', 'lang']] = df['script'].apply(extract_info)

# Define default vs optimized pairs
llm_pairs = [('gpt', 'gpt_opt'), ('llama', 'llama_opt'), ('qwen', 'qwen_opt')]

# Measurement columns
e_cols = [f'e{i}' for i in range(1, 31)]
t_cols = [f't{i}' for i in range(1, 31)]

# Output folder
output_dir = './perf-energy-measurements/boxplots_rq2'
os.makedirs(output_dir, exist_ok=True)

# Color map
colors = {
    'Default': '#1f77b4',   # blue
    'Optimized': '#ff7f0e'  # orange
}

# Generate plots for each model pair
for default_model, opt_model in llm_pairs:
    model_folder = os.path.join(output_dir, default_model)
    os.makedirs(model_folder, exist_ok=True)

    # Get dataframes for each model version
    df_default = df[df['model'] == default_model]
    df_opt = df[df['model'] == opt_model]

    # Merge them on task + language
    merged = pd.merge(df_default, df_opt, on=['base_task', 'lang'], suffixes=('_default', '_opt'))

    for _, row in merged.iterrows():
        task = row['base_task']
        lang = row['lang']

        ### ENERGY BOX PLOT ###
        default_energy = row[[col + '_default' for col in e_cols]].values
        opt_energy = row[[col + '_opt' for col in e_cols]].values

        df_energy = pd.DataFrame({
            'Energy': np.concatenate([default_energy, opt_energy]),
            'Prompt': ['Default'] * 30 + ['Optimized'] * 30
        })

        plt.figure(figsize=(6, 5))
        sns.boxplot(data=df_energy, x='Prompt', y='Energy',
                    palette=colors,
                    showmeans=True,
                    meanprops={"marker": "o", "markerfacecolor": "black",
                               "markeredgecolor": "black", "markersize": 6})
        plt.title(f"{task}.{lang} – Energy (Default vs Optimized)")
        plt.ylabel("Energy Consumption")
        plt.grid(axis='y')
        plt.tight_layout()
        energy_path = os.path.join(model_folder, f"{task}_{lang}_energy.png")
        plt.savefig(energy_path)
        plt.close()

        ### TIME BOX PLOT ###
        default_time = row[[col + '_default' for col in t_cols]].values
        opt_time = row[[col + '_opt' for col in t_cols]].values

        df_time = pd.DataFrame({
            'Time': np.concatenate([default_time, opt_time]),
            'Prompt': ['Default'] * 30 + ['Optimized'] * 30
        })

        plt.figure(figsize=(6, 5))
        sns.boxplot(data=df_time, x='Prompt', y='Time',
                    palette=colors,
                    showmeans=True,
                    meanprops={"marker": "o", "markerfacecolor": "black",
                               "markeredgecolor": "black", "markersize": 6})
        plt.title(f"{task}.{lang} – Time (Default vs Optimized)")
        plt.ylabel("Execution Time")
        plt.grid(axis='y')
        plt.tight_layout()
        time_path = os.path.join(model_folder, f"{task}_{lang}_time.png")
        plt.savefig(time_path)
        plt.close()

print(f"✅ All box plots saved in: {output_dir}/")
