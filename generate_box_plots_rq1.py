import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Load full 30-run results
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Exclude optimized versions (i.e., _opt suffixes)
df = df[~df['script'].str.contains('_opt')]

# Extract task and language
df['task'] = df['script'].apply(lambda x: x.split('.')[0])
df['language'] = df['script'].apply(lambda x: x.split('.')[-1])

# Extract base task and model (human, gpt, llama, qwen)
def parse_task_info(task):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen)?$", task)
    if match:
        base_task = match.group(1)
        model = match.group(2)[1:] if match.group(2) else 'human'
        return pd.Series([base_task, model])
    return pd.Series([task, 'unknown'])

df[['base_task', 'model']] = df['task'].apply(parse_task_info)

# Filter to valid models only
df = df[df['model'].isin(['human', 'gpt', 'llama', 'qwen'])]

# Create output directory
output_dir = './perf-energy-measurements/plots_box_rq1'
os.makedirs(output_dir, exist_ok=True)

# Plot settings
llms = ['gpt', 'llama', 'qwen']
metrics = ['energy', 'time']
base_tasks = df['base_task'].unique()

# Generate box plots
for model in llms:
    for metric in metrics:
        for task in base_tasks:
            subset = df[
                (df['base_task'] == task) &
                (df['model'].isin(['human', model]))
            ]

            if subset.empty:
                continue

            for lang in subset['language'].unique():
                lang_data = subset[subset['language'] == lang]

                if lang_data['model'].nunique() < 2:
                    continue

                ax = lang_data.boxplot(
                    column=metric,
                    by='model',
                    showmeans=True,
                    grid=False,
                    figsize=(8, 5),
                    meanline=True,
                    notch=True,
                    patch_artist=True
                )

                title_metric = "Energy Consumption" if metric == 'energy' else "Execution Time"
                ax.set_title(f"{title_metric} - {lang.upper()} ({task})")
                ax.set_ylabel("Joules" if metric == 'energy' else "Seconds")
                ax.set_xlabel("Source")
                plt.suptitle("")  # Remove default Pandas title
                plt.tight_layout()

                filename = f"{task}_{model}_vs_human_{metric}_{lang}.png"
                plt.savefig(os.path.join(output_dir, filename))
                plt.close()

print(f"✅ Box plots saved to '{output_dir}' — Total: {len(os.listdir(output_dir))} plots.")
