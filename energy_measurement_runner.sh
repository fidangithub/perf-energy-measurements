#!/bin/bash

set -u

# Number of runs per script
RUNS_PER_SCRIPT=30

# Script list (original + all variants)
SCRIPTS=(
    "mergearrays.js"
    "mergearrays.py"
    "mergearrays.rs"
    
    "mergearrays_gpt.js"
    "mergearrays_gpt_opt.js"
    "mergearrays_gpt.py"

    "mergearrays_llama.js"
    "mergearrays_llama_opt.js"
    "mergearrays_llama.py"
    "mergearrays_llama_opt.py"

    "mergearrays_qwen.js"
    "mergearrays_qwen.py"

    "queuetime.js"
    "queuetime.py"
    "queuetime.rs"

    "queuetime_gpt.js"
    "queuetime_gpt_opt.js"
    "queuetime_gpt.py"
    "queuetime_gpt_opt.py"

    "queuetime_llama.js"
    "queuetime_llama_opt.js"
    "queuetime_llama.py"
    "queuetime_llama_opt.py"

    "queuetime_qwen.js"
    "queuetime_qwen.py"
    "queuetime_qwen_opt.py"

    "sjf.js"
    "sjf.py"
    "sjf.rs"

    "sjf_gpt.js"
    "sjf_gpt_opt.js"
    "sjf_gpt.py"

    "sjf_llama.js"
    "sjf_llama_opt.js"
    "sjf_llama.py"
    "sjf_llama_opt.py"

    "sjf_qwen.js"
    "sjf_qwen_opt.js"
    "sjf_qwen.py"
    "sjf_qwen.rs"
    "sjf_qwen_opt.rs"

    "treebylevels.js"
    "treebylevels.py"
    "treebylevels.rs"

    "treebylevels_gpt.js"
    "treebylevels_gpt_opt.js"
    "treebylevels_gpt.py"
    "treebylevels_gpt_opt.py"

    "treebylevels_llama.js"
    "treebylevels_llama_opt.js"
    "treebylevels_llama.py"
    "treebylevels_llama_opt.py"

    "treebylevels_qwen.js"
    "treebylevels_qwen_opt.js"
    "treebylevels_qwen.py"
    "treebylevels_qwen_opt.py"
    "treebylevels_qwen.rs"
    "treebylevels_qwen_opt.rs"
)

SCRIPT_DIR="perf-energy-measurements"
LOG_FILE="perf-energy-measurements/energy_results.log"

# Initialize CSV header once
echo "script,language,run_id,energy_joules,time_seconds" > "$LOG_FILE"

# Create list of [script,run_id] entries
entries=()
for script in "${SCRIPTS[@]}"; do
    for i in $(seq 1 $RUNS_PER_SCRIPT); do
        entries+=("$script:$i")
    done
done

# Shuffle the entries
shuffled_entries=($(printf "%s\n" "${entries[@]}" | shuf))

measure_energy() {
    local label=$1
    local language=$2
    local command=$3
    local run_id=$4

    echo "[$label][$language] Run #$run_id" | tee -a "$LOG_FILE"

    perf_output=$(sudo perf stat -e power/energy-pkg/ $command 2>&1)

    energy_joules=$(echo "$perf_output" | grep "power/energy-pkg/" | awk '{print $1}')
    time_seconds=$(echo "$perf_output" | grep "seconds time elapsed" | awk '{print $1}')

    energy_joules=${energy_joules:-"N/A"}
    time_seconds=${time_seconds:-"N/A"}

    echo "$label,$language,$run_id,$energy_joules,$time_seconds" >> "$LOG_FILE"
}

# Loop through randomized list
for entry in "${shuffled_entries[@]}"; do
    IFS=":" read -r script_file run_id <<< "$entry"

    script="$SCRIPT_DIR/$script_file"
    basefile=$(basename -- "$script_file")
    extension="${basefile##*.}"
    label="${basefile%.*}"

    case $extension in
        js)
            language="JavaScript"
            node --expose-gc "$script" > /dev/null
            command="taskset -c 2 env MEASURE=true node --expose-gc $script"
            ;;
        py)
            language="Python"
            command="taskset -c 2 python3 $script"
            ;;
        rs)
            language="Rust"
            rustc "$script" -o temp_exec || { echo "Rust compilation failed for $script_file" | tee -a "$LOG_FILE"; continue; }
            command="taskset -c 2 ./temp_exec"
            ;;
        *)
            echo "Unknown extension for $script_file — skipping." | tee -a "$LOG_FILE"
            continue
            ;;
    esac

    echo "======================================"
    echo "Run #$run_id for: $basefile"
    echo "--------------------------------------"


    if ! measure_energy "$basefile" "$language" "$command" "$run_id"; then
        echo "ERROR: Measurement failed for $label (Run #$run_id)" | tee -a "$LOG_FILE"
    else
        echo "SUCCESS: $label Run #$run_id completed" | tee -a "$LOG_FILE"
    fi

    if [[ $extension == "rs" && -f "./temp_exec" ]]; then
        rm ./temp_exec
    fi

    echo "Sleeping 1 minute before next run..." | tee -a "$LOG_FILE"
    sleep 60
done

echo "All measurements complete!" | tee -a "$LOG_FILE"
