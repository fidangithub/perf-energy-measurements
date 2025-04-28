import pandas as pd

def load_and_prepare_data(filepath):
    # Load CSV
    data = pd.read_csv(filepath)

    # Filter out samples that have '_opt' in the script name
    data = data[~data['script'].str.contains('_opt')]

    # Prepare base names for matching
    def get_base_name(script):
        for tag in ['_gpt', '_llama', '_qwen']:
            script = script.replace(tag, '')
        return script

    data['base_name'] = data['script'].apply(get_base_name)

    # Split human and LLMs
    human_data = data[~data['script'].str.contains('_gpt|_llama|_qwen')]
    gpt_data = data[data['script'].str.contains('_gpt')]
    llama_data = data[data['script'].str.contains('_llama')]
    qwen_data = data[data['script'].str.contains('_qwen')]

    # Match based on base_name
    def match_groups(human_df, llm_df):
        common_bases = set(human_df['base_name']).intersection(set(llm_df['base_name']))
        human_matched = human_df[human_df['base_name'].isin(common_bases)].copy()
        llm_matched = llm_df[llm_df['base_name'].isin(common_bases)].copy()
        return human_matched, llm_matched

    human_gpt, gpt_matched = match_groups(human_data, gpt_data)
    human_llama, llama_matched = match_groups(human_data, llama_data)
    human_qwen, qwen_matched = match_groups(human_data, qwen_data)

    return human_gpt, gpt_matched, human_llama, llama_matched, human_qwen, qwen_matched

if __name__ == "__main__":
    # File path
    filepath = "./perf-energy-measurements/final_energy_results_wide.csv"

    # Load and generate groups
    human_gpt, gpt_matched, human_llama, llama_matched, human_qwen, qwen_matched = load_and_prepare_data(filepath)

    # Add group labels
    human_gpt['group'] = 'human_gpt'
    gpt_matched['group'] = 'gpt'
    human_llama['group'] = 'human_llama'
    llama_matched['group'] = 'llama'
    human_qwen['group'] = 'human_qwen'
    qwen_matched['group'] = 'qwen'

    # Combine all into one dataframe
    final_combined = pd.concat([
        human_gpt[['script', 'mean_energy', 'mean_time', 'group']],
        gpt_matched[['script', 'mean_energy', 'mean_time', 'group']],
        human_llama[['script', 'mean_energy', 'mean_time', 'group']],
        llama_matched[['script', 'mean_energy', 'mean_time', 'group']],
        human_qwen[['script', 'mean_energy', 'mean_time', 'group']],
        qwen_matched[['script', 'mean_energy', 'mean_time', 'group']],
    ], ignore_index=True)

# Save to a single CSV
final_combined.to_csv('./perf-energy-measurements/rq1_matched_groups.csv', index=False)