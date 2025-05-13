import pandas as pd

def load_and_prepare_full_data(filepath):
    # Load CSV
    data = pd.read_csv(filepath)

    # Filter out optimized versions
    data = data[~data['script'].str.contains('_opt')]

    # Extract base name for matching
    def get_base_name(script):
        for tag in ['_gpt', '_llama', '_qwen']:
            script = script.replace(tag, '')
        return script

    data['base_name'] = data['script'].apply(get_base_name)

    # Split datasets
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

    # Add group labels
    human_gpt['group'] = 'human_gpt'
    gpt_matched['group'] = 'gpt'
    human_llama['group'] = 'human_llama'
    llama_matched['group'] = 'llama'
    human_qwen['group'] = 'human_qwen'
    qwen_matched['group'] = 'qwen'

    # Drop mean values and base_name
    cols_to_drop = ['mean_energy', 'mean_time', 'base_name']
    final_combined = pd.concat([
        human_gpt.drop(columns=cols_to_drop),
        gpt_matched.drop(columns=cols_to_drop),
        human_llama.drop(columns=cols_to_drop),
        llama_matched.drop(columns=cols_to_drop),
        human_qwen.drop(columns=cols_to_drop),
        qwen_matched.drop(columns=cols_to_drop),
    ], ignore_index=True)

    return final_combined

if __name__ == "__main__":
    filepath = "./perf-energy-measurements/final_energy_results_wide.csv"  # Update this if the path differs
    full_grouped_data = load_and_prepare_full_data(filepath)
    full_grouped_data.to_csv("rq1_matched_groups_all_values.csv", index=False)
