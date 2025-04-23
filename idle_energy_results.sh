#!/bin/bash

OUTFILE="idle_energy_results.csv"
echo "run_id,energy_joules,time_seconds" > "$OUTFILE"

for i in $(seq 1 30); do
    echo "Measuring idle #$i"
    perf_output=$(sudo perf stat -e power/energy-pkg/ sleep 60 2>&1)
    energy=$(echo "$perf_output" | grep "power/energy-pkg/" | awk '{print $1}')
    time=$(echo "$perf_output" | grep "seconds time elapsed" | awk '{print $1}')
    echo "$i,$energy,$time" >> "$OUTFILE"
    sleep 2
done
