import pandas as pd
import re
from scipy.stats import mannwhitneyu

# --- Cliff's delta function ---
def cliffs_delta(x, y):
    n = len(x)
    m = len(y)
    more = sum(i > j for i in x for j in y)
    less = sum(i < j for i in x for j in y)
    return (more - less) / (n * m)

def interpret_cliffs_delta(delta):
    abs_delta = abs(delta)
    if abs_delta < 0.147:
        return 'negligible'
    elif abs_delta < 0.33:
        return 'small'
    elif abs_delta < 0.474:
        return 'medium'
    else:
        return 'large'

# --- Load data ---
df = pd.read_csv('./perf-energy-measurements/final_energy_results_round.csv')

# --- Extract model, task, language ---
def extract_info(script):
    match = re.match(r"^(.*?)(_gpt|_llama|_qwen|_gpt_opt|_llama_opt|_qwen_opt)?\.(\w+)$", script)
    if match:
        base = match.group(1)
        suffix = match.group(2)[1:] if match.group(2) else None
        lang = match.group(3)
        return pd.Series([base, suffix, lang])
    return pd.Series([script, 'unknown', ''])

df[['base_task', 'model', 'lang_ext']] = df['script'].apply(extract_info)

# --- Define model pairs ---
llm_versions = ['gpt', 'llama', 'qwen']
opt_versions = ['gpt_opt', 'llama_opt', 'qwen_opt']

# --- Run tests ---
results = []

for model, opt_model in zip(llm_versions, opt_versions):
    llm_data = df[df['model'] == model]
    opt_data = df[df['model'] == opt_model]

    merged = llm_data.merge(opt_data, on=['base_task', 'lang_ext'], suffixes=('_llm', '_opt'))

    if merged.empty:
        print(f"No matched samples for {model.upper()} vs {opt_model.upper()}")
        continue

    # Mann–Whitney for energy
    u_energy = mannwhitneyu(merged['mean_energy_llm'], merged['mean_energy_opt'], alternative='two-sided')
    d_energy = cliffs_delta(merged['mean_energy_llm'].values, merged['mean_energy_opt'].values)
    e_energy = interpret_cliffs_delta(d_energy)

    # Mann–Whitney for time
    u_time = mannwhitneyu(merged['mean_time_llm'], merged['mean_time_opt'], alternative='two-sided')
    d_time = cliffs_delta(merged['mean_time_llm'].values, merged['mean_time_opt'].values)
    e_time = interpret_cliffs_delta(d_time)

    # Save results
    results.append({
        'Model': model.upper(),
        'Metric': 'Energy',
        'U-statistic': round(u_energy.statistic, 4),
        'p-value': round(u_energy.pvalue, 4),
        "Cliff's delta": round(d_energy, 4),
        'Effect size': e_energy
    })
    results.append({
        'Model': model.upper(),
        'Metric': 'Time',
        'U-statistic': round(u_time.statistic, 4),
        'p-value': round(u_time.pvalue, 4),
        "Cliff's delta": round(d_time, 4),
        'Effect size': e_time
    })

# --- Output to CSV ---
results_df = pd.DataFrame(results)
results_df.to_csv('./perf-energy-measurements/mannwhitney_llm_vs_opt_results.csv', index=False)
print("Results saved to 'mannwhitney_llm_vs_opt_results.csv'")
