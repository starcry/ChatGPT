#!/bin/bash

# Get current day of the week as an integer (0 = Monday, 1 = Tuesday, etc.)
day_of_week=$(date +%u)

# if today is a weekend day (6 = Saturday, 7 = Sunday)
if (( day_of_week >= 6 )); then
    # choose a random weekday
    random_day=$(( ( RANDOM % 5 ) ))
    day_of_week=$random_day
fi

# Define directory paths
dir_paths=('monday' 'tuesday' 'wednesday' 'thursday' 'friday')

# Get lines from files in relevant directory for today's day of the week
lines=()
for i in {0..4}; do
    while read -r line; do
        lines+=("$line")
    done < <(shuf -n1 "${dir_paths[$day_of_week]}/$i")
done

# Randomize order of lines
shuf -e "${lines[@]}"

# Print out lines
printf '%s\n' "${shuf_lines[@]}"
