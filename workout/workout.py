#!/usr/bin/python3
import random
import datetime
import argparse

def print_random_lines(directory, file_count, title):
    """
    Get a random line from each file in the specified directory and print them.
    """
    print(f"\n{title}")
    print("-" * len(title))

    for i in range(file_count):
        with open(f"{directory}/{i}", "r") as f:
            print(random.choice(f.readlines()).strip())

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", help="Specify the day of the week (monday, tuesday, ..., sunday, t=tomorrow, r=random)")

# Parse arguments
args = parser.parse_args()

# Get current day of the week as an integer (0 = Monday, 1 = Tuesday, etc.)
day_of_week = datetime.datetime.today().weekday()

# If today is a weekend day (5 = Saturday, 6 = Sunday), choose a random weekday
if day_of_week >= 5:
    day_of_week = random.randint(0, 4)  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday

# Check if a day was passed as an argument
if args.day:
    if str(args.day).lower() == "t":
        day_of_week = (day_of_week + 1) % 7
    elif str(args.day).lower() == "r":
        day_of_week = random.randint(0, 4)  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday
    else:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if args.day.lower() in days:
            day_of_week = days.index(args.day.lower())
        else:
            print("Invalid day argument. Please enter a day of the week, 't' for tomorrow, or 'r' for random.")
            exit(1)

# Define directory paths
dir_paths = ['monday', 'teusday', 'wednesday', 'thursday', 'friday']

# Get and print lines from cardio directory
print_random_lines("cardio", 6, "cardio")

# Get and print lines from today's directory
print_random_lines(dir_paths[day_of_week], 5, "circuit training")

