import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re

# Load the dataset
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Extract task, model, and language
def extract_info(script):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen|_gpt_opt|_llama_opt|_qwen_opt)?\.(\w+)$", script)
    if match:
        base = match.group(1)
        suffix = match.group(2)[1:] if match.group(2) else None
        lang = match.group(3)
        return pd.Series([base, suffix, lang])
    return pd.Series([script, 'unknown', ''])

df[['base_task', 'model', 'lang_ext']] = df['script'].apply(extract_info)

# Define LLMs and corresponding optimized versions
llm_versions = ['gpt', 'llama', 'qwen']
opt_versions = ['gpt_opt', 'llama_opt', 'qwen_opt']

# Create output directory
plot_dir = './perf-energy-measurements/llm_vs_opt_taskwise_barplots'
os.makedirs(plot_dir, exist_ok=True)

# Generate plots by LLM and task
for model, opt_model in zip(llm_versions, opt_versions):
    llm_df = df[df['model'] == model]
    opt_df = df[df['model'] == opt_model][['base_task', 'lang_ext', 'mean_energy', 'mean_time']]
    opt_df = opt_df.rename(columns={'mean_energy': 'opt_energy', 'mean_time': 'opt_time'})

    merged = llm_df.merge(opt_df, on=['base_task', 'lang_ext'], how='inner')
    merged['sample'] = merged['base_task'] + '-' + merged['lang_ext']

    # Group by task
    for task in merged['base_task'].unique():
        task_data = merged[merged['base_task'] == task].sort_values('sample')
        if task_data.empty:
            continue

        x_labels = task_data['sample'].tolist()
        x = np.arange(len(x_labels))
        width = 0.35
        sample_count = len(task_data)

        # --- Energy Plot ---
        plt.figure(figsize=(10, 5))
        plt.bar(x - width/2, task_data['mean_energy'], width, label='Default Prompt')
        plt.bar(x + width/2, task_data['opt_energy'], width, label='Optimized Prompt')
        plt.xticks(x, x_labels, rotation=45, ha='right')
        plt.ylabel("Mean Energy")
        plt.title(f"{model.upper()} - Energy Comparison for {task} (Samples: {sample_count})")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"{model}_{task}_energy_comparison.png"))
        plt.close()

        # --- Time Plot ---
        plt.figure(figsize=(10, 5))
        plt.bar(x - width/2, task_data['mean_time'], width, label='Default Prompt')
        plt.bar(x + width/2, task_data['opt_time'], width, label='Optimized Prompt')
        plt.xticks(x, x_labels, rotation=45, ha='right')
        plt.ylabel("Mean Time")
        plt.title(f"{model.upper()} - Time Comparison for {task} (Samples: {sample_count})")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"{model}_{task}_time_comparison.png"))
        plt.close()

print(f"All task-separated plots saved in: {plot_dir}")
