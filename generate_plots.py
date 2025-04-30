import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Load the dataset
df = pd.read_csv('./perf-energy-measurements/rq1_matched_groups.csv')

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

# Filter to only the relevant models
df = df[df['model'].isin(['human', 'gpt', 'llama', 'qwen'])]

# Output folder
output_dir = './perf-energy-measurements/plots_by_model'
os.makedirs(output_dir, exist_ok=True)

# Define models to compare against human
llms = ['gpt', 'llama', 'qwen']
metrics = ['mean_energy', 'mean_time']
base_tasks = df['base_task'].unique()

# Generate graphs for each LLM vs Human
for model in llms:
    for metric in metrics:
        for task in base_tasks:
            task_data = df[df['base_task'] == task]
            
            # Filter to just human and current model
            sub_data = task_data[task_data['model'].isin(['human', model])]
            
            # Pivot the data
            pivot = sub_data.pivot_table(index='language', columns='model', values=metric)

            # Only keep rows where both human and current LLM are present
            if 'human' in pivot.columns and model in pivot.columns:
                pivot = pivot.dropna(subset=['human', model])
                
                if not pivot.empty:
                    ax = pivot[['human', model]].plot(kind='bar', figsize=(10, 6))
                    title = "Energy Consumption" if metric == 'mean_energy' else "Execution Time"
                    ax.set_title(f"{title} - Human vs {model.upper()} ({task})")
                    ax.set_ylabel("Mean " + ("Energy" if metric == 'mean_energy' else "Time"))
                    ax.set_xlabel("Programming Language")
                    plt.xticks(rotation=0)
                    plt.legend(title="Source")
                    plt.tight_layout()
                    
                    # Save the plot
                    file_name = f"{task}_{model}_vs_human_{metric}.png"
                    plt.savefig(os.path.join(output_dir, file_name))
                    plt.close()

print(f"All plots saved in '{output_dir}' folder.")
