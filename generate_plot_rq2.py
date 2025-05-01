        # --- Energy Plot ---
        fig, ax = plt.subplots(figsize=(10, 5))
        bars1 = ax.bar(x - width/2, task_data['mean_energy'], width, label='Default Prompt')
        bars2 = ax.bar(x + width/2, task_data['opt_energy'], width, label='Optimized Prompt')

        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, rotation=45, ha='right')
        ax.set_ylabel("Mean Energy")
        ax.set_title(f"{model.upper()} - Mean Energy Consumption Comparison for {task} (Samples: {sample_count})")
        ax.legend()

        # Add value labels
        for bar in bars1:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', 
                    ha='center', va='bottom', fontsize=8)
        for bar in bars2:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', 
                    ha='center', va='bottom', fontsize=8)

        fig.tight_layout()
        fig.savefig(os.path.join(plot_dir, f"{model}_{task}_energy_comparison.png"))
        plt.close()

        # --- Time Plot ---
        fig, ax = plt.subplots(figsize=(10, 5))
        bars1 = ax.bar(x - width/2, task_data['mean_time'], width, label='Default Prompt')
        bars2 = ax.bar(x + width/2, task_data['opt_time'], width, label='Optimized Prompt')

        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, rotation=45, ha='right')
        ax.set_ylabel("Mean Time")
        ax.set_title(f"{model.upper()} - Mean Execution Time Comparison for {task} (Samples: {sample_count})")
        ax.legend()

        # Add value labels
        for bar in bars1:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', 
                    ha='center', va='bottom', fontsize=8)
        for bar in bars2:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', 
                    ha='center', va='bottom', fontsize=8)

        fig.tight_layout()
        fig.savefig(os.path.join(plot_dir, f"{model}_{task}_time_comparison.png"))
        plt.close()
