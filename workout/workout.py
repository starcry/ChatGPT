#!/usr/bin/python3
import random
import datetime
import argparse
import os

def print_random_lines(directory, file_count, title, delimiter=None):
    """Print a random line from each file in the specified directory."""
    print(f"\n{title}")
    print("-" * len(title))

    for i in range(file_count):
        with open(f"{directory}/{i}", "r") as f:
            line = random.choice(f.readlines()).strip()
            print(line)

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Specify the day of the week.")
    args = parser.parse_args()

    day_of_week = datetime.datetime.today().weekday()
    if day_of_week >= 5:
        day_of_week = random.randint(0, 4)

    if args.day:
        day_arg = args.day.lower()
        days = ['monday', 'teusday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        if day_arg == "t":
            day_of_week = (day_of_week + 1) % 7
        elif day_arg == "r":
            day_of_week = random.randint(0, 4)
        elif day_arg in days:
            day_of_week = days.index(day_arg)
        else:
            print("Invalid day argument.")
            exit(1)

    dir_paths = ['monday', 'teusday', 'wednesday', 'thursday', 'friday']
    print_random_lines("cardio", 6, "Cardio")
    print_random_lines(dir_paths[day_of_week], 5, "Circuit Training")
    print_random_lines("mobility", 2, "Mobility and Flexibility Exercises")

if __name__ == "__main__":
    main()

