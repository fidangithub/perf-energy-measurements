import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Load the data
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Extract base task, model name, and language from 'script' column
def extract_info(script):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen|_gpt_opt|_llama_opt|_qwen_opt)?\.(\w+)$", script)
    if match:
        base = match.group(1)
        suffix = match.group(2)[1:] if match.group(2) else None
        lang = match.group(3)
        return pd.Series([base, suffix, lang])
    return pd.Series([script, 'unknown', ''])

df[['base_task', 'model', 'lang_ext']] = df['script'].apply(extract_info)

# Models and their opt versions
llm_versions = ['gpt', 'llama', 'qwen']
opt_versions = ['gpt_opt', 'llama_opt', 'qwen_opt']

# Output directory
plot_dir = './perf-energy-measurements/llm_vs_opt_barplots'
os.makedirs(plot_dir, exist_ok=True)

# Generate plots
for model, opt_model in zip(llm_versions, opt_versions):
    llm_df = df[df['model'] == model]
    opt_df = df[df['model'] == opt_model][['base_task', 'lang_ext', 'mean_energy', 'mean_time']]
    opt_df = opt_df.rename(columns={'mean_energy': 'opt_energy', 'mean_time': 'opt_time'})

    merged = llm_df.merge(opt_df, on=['base_task', 'lang_ext'], how='inner')
    merged['sample'] = merged['base_task'] + '-' + merged['lang_ext']
    sample_count = len(merged)

    # Sort by sample for consistent bar order
    merged = merged.sort_values('sample')
    x = merged['sample']
    x_indexes = range(len(x))

    # --- Energy Bar Plot ---
    plt.figure(figsize=(12, 6))
    plt.bar(x_indexes, merged['mean_energy'], label='Default Prompt')
    plt.bar(x_indexes, merged['opt_energy'], label='Optimized Prompt', alpha=0.7)
    plt.xticks(x_indexes, x, rotation=45, ha='right')
    plt.ylabel("Mean Energy")
    plt.title(f"{model.upper()} - Energy Comparison (Samples: {sample_count})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, f"{model}_energy_comparison.png"))
    plt.close()

    # --- Time Bar Plot ---
    plt.figure(figsize=(12, 6))
    plt.bar(x_indexes, merged['mean_time'], label='Default Prompt')
    plt.bar(x_indexes, merged['opt_time'], label='Optimized Prompt', alpha=0.7)
    plt.xticks(x_indexes, x, rotation=45, ha='right')
    plt.ylabel("Mean Time")
    plt.title(f"{model.upper()} - Time Comparison (Samples: {sample_count})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, f"{model}_time_comparison.png"))
    plt.close()

print(f"All plots saved in '{plot_dir}'")
