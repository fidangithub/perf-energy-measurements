import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("./perf-energy-measurements/final_energy_results_round.csv")

# Remove _opt rows
df = df[~df['script'].str.contains('_opt')].copy()

# Extract metadata
df['source'] = df['script'].apply(lambda x: 'human' if '.' not in x else x.split('.')[-1])
df['language'] = df['script'].apply(lambda x: x.split('_')[-1].split('.')[0] if '.' in x else x.split('_')[-1])
df['task'] = df['script'].apply(lambda x: '_'.join(x.split('_')[:-1]) if '.' not in x else '_'.join(x.split('_')[:-1]).split('.')[0])

# Melt time and energy
energy_cols = [f"e{i}" for i in range(1, 31)]
time_cols = [f"t{i}" for i in range(1, 31)]

df_energy = df.melt(id_vars=['script', 'source', 'language', 'task'], value_vars=energy_cols,
                    var_name='measurement', value_name='value')
df_energy['metric'] = 'energy'

df_time = df.melt(id_vars=['script', 'source', 'language', 'task'], value_vars=time_cols,
                  var_name='measurement', value_name='value')
df_time['metric'] = 'time'

# Combine and normalize
df_long = pd.concat([df_energy, df_time], ignore_index=True)
df_long = df_long.dropna()
df_long['norm_value'] = df_long.groupby('metric')['value'].transform(lambda x: x / x.max())

# Create folders
output_base = "./perf-energy-measurements/llm_comparison_rq1_plots"
llms = ['gpt', 'llama', 'gemini']
for llm in llms:
    os.makedirs(f"{output_base}/{llm}", exist_ok=True)

# Plotting
for llm in llms:
    tasks = df_long[df_long['source'] == llm]['task'].unique()
    for task in tasks:
        for metric in ['energy', 'time']:
            valid_langs = df_long[
                (df_long['source'] == llm) &
                (df_long['task'] == task) &
                (df_long['metric'] == metric)
            ]['language'].unique()

            # Keep only if human + llm data exist for a language
            comp = df_long[
                (df_long['task'] == task) &
                (df_long['metric'] == metric) &
                (df_long['language'].isin(valid_langs)) &
                (df_long['source'].isin(['human', llm]))
            ]

            # Filter languages where both versions exist
            paired_langs = comp.groupby(['language', 'source']).size().unstack().dropna().index
            comp = comp[comp['language'].isin([lang for lang, _ in paired_langs])]

            if comp.empty:
                continue

            plt.figure(figsize=(10, 6))
            sns.boxplot(x='language', y='norm_value', hue='source', data=comp, showmeans=True,
                        meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black"})
            plt.title(f'{metric.capitalize()} - Task: {task} - Human vs {llm.upper()}')
            plt.ylabel(f'Normalized {metric.capitalize()}')
            plt.xlabel('Programming Language')
            plt.legend(title='Source')
            plt.tight_layout()

            save_path = f"{output_base}/{llm}/{task}_{metric}_boxplot.png"
            plt.savefig(save_path)
            plt.close()
