#!/usr/bin/python3
import random
import datetime

# Get current day of the week as an integer (0 = Monday, 1 = Tuesday, etc.)
day_of_week = datetime.datetime.today().weekday()

# if today is a weekend day (5 = Saturday, 6 = Sunday)
if day_of_week >= 5:
    # choose a random weekday
    random_day = random.randint(0, 4)  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday
    day_of_week = random_day

# Define directory paths
dir_paths = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

# Get lines from files in relevant directory for today's day of the week
lines = []
for i in range(5):
    with open(f"{dir_paths[day_of_week]}/{i}", "r") as f:
        lines.append(random.choice(f.readlines()).strip())

# Randomize order of lines
random.shuffle(lines)

# Print out lines
for line in lines:
    print(line)

