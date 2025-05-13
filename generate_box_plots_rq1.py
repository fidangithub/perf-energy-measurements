import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Load the detailed measurement data
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Exclude optimized outputs (_opt)
df = df[~df['script'].str.contains('_opt')]

# Extract task and language from script name
df['task'] = df['script'].apply(lambda x: x.split('.')[0])
df['language'] = df['script'].apply(lambda x: x.split('.')[-1])

# Extract base task and model
def parse_task_info(task):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen)?$", task)
    if match:
        base_task = match.group(1)
        model = match.group(2)[1:] if match.group(2) else 'human'
        return pd.Series([base_task, model])
    return pd.Series([task, 'unknown'])

df[['base_task', 'model']] = df['task'].apply(parse_task_info)

# Output folder
output_dir = './perf-energy-measurements/box_plots_by_model'
os.makedirs(output_dir, exist_ok=True)

# Define metrics and LLMs
metrics = ['energy', 'time']
llms = ['gpt', 'llama', 'qwen']
base_tasks = df['base_task'].unique()

# Plot boxplots comparing human vs LLM for each task and metric
for model in llms:
    for metric in metrics:
        for task in base_tasks:
            task_df = df[df['base_task'] == task]

            for lang in task_df['language'].unique():
                subset = task_df[(task_df['language'] == lang) & (task_df['model'].isin(['human', model]))]

                if subset['model'].nunique() < 2:
                    continue  # Skip if one of the models is missing

                # Create boxplot
                plt.figure(figsize=(8, 6))
                subset.boxplot(column=metric, by='model', grid=False, showmeans=True,
                               meanprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "black"})

                plt.title(f"{metric.capitalize()} - {task} ({lang})\nHuman vs {model.upper()}")
                plt.suptitle("")  # Remove default suptitle
                plt.xlabel("Source")
                plt.ylabel(f"{metric.capitalize()} (rounded)")
                plt.tight_layout()

                file_name = f"{task}_{model}_vs_human_{metric}_{lang}.png"
                plt.savefig(os.path.join(output_dir, file_name))
                plt.close()
