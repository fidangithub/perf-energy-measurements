#!/bin/bash

# Valid scripts (original and optimized)
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

# Output log file
LOG_FILE="perf-energy-measurements/energy_results.log"
SCRIPT_DIR="perf-energy-measurements"

measure_energy() {
    local label=$1
    local language=$2
    local command=$3

    echo "$label" | tee -a "$LOG_FILE"

    perf_output=$(sudo perf stat -e power/energy-pkg/ $command 2>&1)
    # perf_output=$(sudo perf stat -e power/energy-pkg/,instructions,cycles,cache-misses $command 2>&1)

    # Extract values
    energy_joules=$(echo "$perf_output" | grep "power/energy-pkg/" | awk '{print $1}')
    time_seconds=$(echo "$perf_output" | grep "seconds time elapsed" | awk '{print $1}')

    # Fallbacks
    energy_joules=${energy_joules:-"N/A"}
    time_seconds=${time_seconds:-"N/A"}

    # Output to CSV
    echo "$label,$language,$energy_joules,$time_seconds" >> "$LOG_FILE"
}

# Initialize log
echo "script,language,energy_joules,time_seconds" > "$LOG_FILE"

echo "---------------------------------------------------------------" >> "$LOG_FILE"

for script_file in "${SCRIPTS[@]}"; do
    script="$SCRIPT_DIR/$script_file"
    basefile=$(basename -- "$script")
    extension="${basefile##*.}"
    label="${basefile%.*}"

    case $extension in
        js)
            language="JavaScript"

            # Run warmup (not measured)
            node --expose-gc "$script"

            # Now run measured part (MEASURE=true) inside perf
            command="taskset -c 2 node --expose-gc $script"
            export MEASURE=true
            ;;
        py)
            language="Python"
            command="taskset -c 2 python3 $script"
            ;;
        rs)
            language="Rust"
            rustc "$script" -o temp_exec || { echo "Rust compilation failed for $script" | tee -a "$LOG_FILE"; continue; }
            command="taskset -c 2 ./temp_exec"
            ;;
        *)
            echo "Unknown extension for $script — skipping." | tee -a "$LOG_FILE"
            continue
            ;;
    esac

    echo "======================================"
    echo "Measuring: $basefile"
    echo "--------------------------------------"

    measure_energy "$basefile" "$language" "$command"

    # Clean up Rust build
    if [[ $extension == "rs" && -f "./temp_exec" ]]; then
        rm ./temp_exec
    fi

    echo "Waiting 1 minutes before the next script..." | tee -a "$LOG_FILE"
    sleep 3
done

echo "All measurements complete!" | tee -a "$LOG_FILE"
