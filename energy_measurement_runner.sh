#!/bin/bash

# Number of perf repetitions
PERF_REPEATS=10

# Valid scripts (original and optimized)
SCRIPTS=(
    "mergearrays.js"
    "mergearrays_opt.js"
    "mergearrays.py"
    "mergearrays_opt.py"
    "mergearrays.rs"
    "mergearrays_opt.rs"
    
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
    "queuetime_opt.js"
    "queuetime.py"
    "queuetime.rs"
    "queuetime_opt.rs"

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
    "sjf_opt.js"
    "sjf.py"
    "sjf_opt.py"
    "sjf.rs"
    "sjf_opt.rs"

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
    "treebylevels_opt.js"
    "treebylevels.py"
    "treebylevels_opt.py"
    "treebylevels.rs"
    "treebylevels_opt.rs"

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

# Output log file
LOG_FILE="energy_results.log"
SCRIPT_DIR="perf-energy-measurements"

measure_energy() {
    local label=$1
    local language=$2
    local command=$3

    echo "Running [$label] ($language) with perf -r $PERF_REPEATS..." | tee -a "$LOG_FILE"
    sudo perf stat -r $PERF_REPEATS -e power/energy-pkg/ $command 2>&1 | tee -a "$LOG_FILE"
}

# Initialize log
echo "Energy Measurement Results - $(date)" > "$LOG_FILE"
echo "-------------------------------------" >> "$LOG_FILE"

for script_file in "${SCRIPTS[@]}"; do
    script="$SCRIPT_DIR/$script_file"
    basefile=$(basename -- "$script")
    extension="${basefile##*.}"
    label="${basefile%.*}"

    case $extension in
        js)
            language="JavaScript"
            command="node $script"
            ;;
        py)
            language="Python"
            command="python3 $script"
            ;;
        rs)
            language="Rust"
            rustc "$script" -o temp_exec || { echo "Rust compilation failed for $script" | tee -a "$LOG_FILE"; continue; }
            command="./temp_exec"
            ;;
        *)
            echo "Unknown extension for $script — skipping." | tee -a "$LOG_FILE"
            continue
            ;;
    esac

    echo "======================================" | tee -a "$LOG_FILE"
    echo "Measuring: $basefile" | tee -a "$LOG_FILE"
    echo "--------------------------------------" | tee -a "$LOG_FILE"

    measure_energy "$basefile" "$language" "$command"

    # Clean up Rust build
    if [[ $extension == "rs" && -f "./temp_exec" ]]; then
        rm ./temp_exec
    fi

    echo "Waiting 5 minutes before the next script..." | tee -a "$LOG_FILE"
    sleep 300
done

echo "All measurements complete!" | tee -a "$LOG_FILE"
