import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.patches import Patch

# Load the data
file_path = './perf-energy-measurements/final_energy_results_round.csv'
df = pd.read_csv(file_path)

# Preprocess
df = df[~df['file'].str.contains('_opt')]  # Remove _opt
df['source'] = df['file'].apply(lambda x: 'human' if '.' not in x else x.split('.')[-1])
df['language'] = df['file'].apply(lambda x: x.split('_')[-1].split('.')[0] if '.' in x else x.split('_')[-1])
df['task'] = df['file'].apply(lambda x: '_'.join(x.split('_')[:-1]) if '.' not in x else '_'.join(x.split('_')[:-1]).split('.')[0])

# Normalize time and energy for better comparability on boxplots
df['norm_time'] = df['time'] / df['time'].max()
df['norm_energy'] = df['energy'] / df['energy'].max()

# Create output folders
base_dir = './perf-energy-measurements/llm_comparison_plots'
llms = ['gpt', 'llama', 'gemini']
for llm in llms:
    os.makedirs(f"{base_dir}/{llm}", exist_ok=True)

# Plot function
def create_box_plots(metric: str, task: str, llm: str):
    data = df[df['task'] == task]
    data = data[data['source'].isin(['human', llm])]
    
    # Only keep languages where both human and llm data are present
    valid_langs = data.groupby(['language', 'source']).size().unstack().dropna().index
    data = data[data['language'].isin(valid_langs)]

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='language', y=metric, hue='source', data=data, showmeans=True,
                meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black"})
    plt.title(f"{metric.capitalize()} - Human vs {llm.upper()} ({task})")
    plt.ylabel(f"{'Normalized ' if 'norm' in metric else ''}{metric.capitalize()}")
    plt.xlabel("Programming Language")
    plt.legend(title='Source')
    filename = f"{base_dir}/{llm}/{task}_{metric}.png"
    plt.savefig(filename)
    plt.close()

# Generate plots
metrics = ['norm_time', 'norm_energy']
tasks = df['task'].unique()

for llm in llms:
    for task in tasks:
        for metric in metrics:
            create_box_plots(metric, task, llm)