import os
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Prepare the output directory for box plots
box_output_dir = '/mnt/data/box_plots_by_model'
os.makedirs(box_output_dir, exist_ok=True)

# Extract task and model info
def parse_task_info(script_name):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen)?\..+$", script_name)
    if match:
        base_task = match.group(1)
        model = match.group(2)[1:] if match.group(2) else 'human'
        return pd.Series([base_task, model])
    return pd.Series([script_name, 'unknown'])

df_final[['base_task', 'model']] = df_final['script'].apply(parse_task_info)

# Reshape the data for plotting
records = []
for _, row in df_final.iterrows():
    for i in range(1, 31):
        records.append({
            'task': row['base_task'],
            'model': row['model'],
            'language': row['language'],
            'energy': row[f'e{i}'],
            'time': row[f't{i}']
        })

df_long = pd.DataFrame.from_records(records)

# Plotting box plots for energy and time
llms = ['gpt', 'llama', 'qwen']
metrics = ['energy', 'time']
base_tasks = df_long['task'].unique()

for model in llms:
    for metric in metrics:
        for task in base_tasks:
            task_data = df_long[df_long['task'] == task]
            sub_data = task_data[task_data['model'].isin(['human', model])]

            if not sub_data.empty:
                plt.figure(figsize=(10, 6))
                ax = sns.boxplot(
                    x='language', y=metric, hue='model', data=sub_data,
                    showmeans=True, meanline=True
                )
                ax.set_title(f"{'Energy' if metric == 'energy' else 'Time'} - Human vs {model.upper()} ({task})")
                ax.set_ylabel("Energy (J)" if metric == 'energy' else "Time (s)")
                ax.set_xlabel("Programming Language")
                plt.legend(title="Source")
                plt.tight_layout()

                filename = f"{task}_{model}_vs_human_{metric}_boxplot.png"
                plt.savefig(os.path.join(box_output_dir, filename))
                plt.close()

box_output_dir
