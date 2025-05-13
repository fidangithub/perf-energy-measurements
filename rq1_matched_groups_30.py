import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

df = pd.read_csv('./perf-energy-measurements/rq1_matched_groups_all_values.csv')

# Setup color map
model_colors = {
    'gpt': '#ff7f0e',    # orange
    'llama': '#2ca02c',  # red
    'qwen': '#d62728',   # green
    'Human': '#1f77b4'   # blue
}

# Create output folder
output_dir = './perf-energy-measurements/boxplots_rq1'
os.makedirs(output_dir, exist_ok=True)

# Get all relevant LLMs
llms = ['gpt', 'llama', 'qwen']

# Get 30 measurement columns
e_cols = [f'e{i}' for i in range(1, 31)]
t_cols = [f't{i}' for i in range(1, 31)]

# Loop through all rows with human vs LLM
for _, row in df[df['group'].str.startswith('human_')].iterrows():
    task = row['script']
    llm = row['group'].split('_')[1]

    # Get the matching LLM row
    llm_script = f"{task.split('.')[0]}_{llm}.{task.split('.')[-1]}"
    llm_row = df[(df['group'] == llm) & (df['script'] == llm_script)]

    if llm_row.empty:
        continue

    # Extract energy and time values
    human_energy = row[e_cols].values
    llm_energy = llm_row[e_cols].values.flatten()

    human_time = row[t_cols].values
    llm_time = llm_row[t_cols].values.flatten()

    lang = task.split('.')[-1]
    taskname = task.split('.')[0].lower()
    modelname = llm.upper()

    ### ENERGY BOXPLOT
    df_energy = pd.DataFrame({
        'Energy': np.concatenate([human_energy, llm_energy]),
        'Model': ['Human'] * 30 + [modelname] * 30
    })

    plt.figure(figsize=(6, 5))
    sns.boxplot(data=df_energy, x='Model', y='Energy',
                palette={'Human': model_colors['Human'], modelname: model_colors[llm]},
                showmeans=True,
                meanprops={"marker": "o", "markerfacecolor": "black", "markeredgecolor": "black", "markersize": 6})
    plt.title(f"{task} – Energy Comparison (Human vs {modelname})")
    plt.ylabel("Energy Consumption")
    plt.grid(axis='y')
    plt.tight_layout()
    fname = f"{llm}/{taskname}_{lang}_energy.png"
    os.makedirs(os.path.join(output_dir, llm), exist_ok=True)
    plt.savefig(os.path.join(output_dir, fname))
    plt.close()

    ### TIME BOXPLOT
    df_time = pd.DataFrame({
        'Time': np.concatenate([human_time, llm_time]),
        'Model': ['Human'] * 30 + [modelname] * 30
    })

    plt.figure(figsize=(6, 5))
    sns.boxplot(data=df_time, x='Model', y='Time',
                palette={'Human': model_colors['Human'], modelname: model_colors[llm]},
                showmeans=True,
                meanprops={"marker": "o", "markerfacecolor": "black", "markeredgecolor": "black", "markersize": 6})
    plt.title(f"{task} – Time Comparison (Human vs {modelname})")
    plt.ylabel("Execution Time")
    plt.grid(axis='y')
    plt.tight_layout()
    fname = f"{llm}/{taskname}_{lang}_time.png"
    plt.savefig(os.path.join(output_dir, fname))
    plt.close()

print("✅ All box plots generated and saved in:", output_dir)
