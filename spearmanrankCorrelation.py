import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
import os

# Load data
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# Classify models
def classify_model(script):
    if '_gpt_opt' in script:
        return 'gpt_opt'
    elif '_gpt' in script:
        return 'gpt'
    elif '_llama_opt' in script:
        return 'llama_opt'
    elif '_llama' in script:
        return 'llama'
    elif '_qwen_opt' in script:
        return 'qwen_opt'
    elif '_qwen' in script:
        return 'qwen'
    else:
        return 'human'

# Extract info
df['model'] = df['script'].apply(classify_model)
df['lang'] = df['script'].apply(lambda x: x.split('.')[-1])
df['task'] = df['script'].apply(lambda x: x.split('_')[0].split('.')[0])

# Output folder
output_dir = './perf-energy-measurements/enhanced_spearman_scatterplots'
os.makedirs(output_dir, exist_ok=True)

# Group definitions
group_definitions = {
    'Human': ['human'],
    'GPT Default and Optimized': ['gpt', 'gpt_opt'],
    'LLaMA Default and Optimized': ['llama', 'llama_opt'],
    'Qwen Default and Optimized': ['qwen', 'qwen_opt']
}

# Colors and shapes
color_map = {
    'gpt': '#1f77b4', 'gpt_opt': '#ff7f0e',
    'llama': '#1f77b4', 'llama_opt': '#ff7f0e',
    'qwen': '#1f77b4', 'qwen_opt': '#ff7f0e',
    'human': 'green'
}
marker_map = {'py': 'o', 'js': '^', 'rs': 's'}

# Generate plots
for title, models in group_definitions.items():
    group_df = df[df['model'].isin(models)].copy()
    if len(group_df) < 2:
        continue

    plt.figure(figsize=(8, 6))

    for _, row in group_df.iterrows():
        model = row['model']
        lang = row['lang']
        plt.scatter(row['mean_time'], row['mean_energy'],
                    color=color_map[model],
                    marker=marker_map.get(lang, 'o'),
                    s=80, edgecolor='black')
        plt.text(row['mean_time'] + 0.003, row['mean_energy'],
                 row['task'], fontsize=8)

    # Custom legends
    shape_legend = [
        Line2D([0], [0], marker=marker_map[lang], color='w',
               markerfacecolor='black', label=lang, markersize=8)
        for lang in marker_map
    ]
    color_legend = [
        Line2D([0], [0], marker='o', color='w',
               markerfacecolor=color_map[m], label=m.upper(), markersize=8)
        for m in models
    ]

    plt.legend(handles=color_legend + shape_legend, title='Legend', loc='upper left')
    plt.title(title)
    plt.xlabel("Execution Time")
    plt.ylabel("Energy Consumption")
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    safe_name = title.lower().replace(' ', '_').replace('default_and_optimized', 'comparison')
    plt.savefig(os.path.join(output_dir, f"{safe_name}_scatterplot.png"))
    plt.close()

print("✅ All enhanced scatterplots saved to:", output_dir)
