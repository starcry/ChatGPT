#!/usr/bin/python3
import random
import datetime
import argparse
import os

def get_filtered_filenames(directory):
    """Return filenames without digits and with underscores replaced."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    non_digit_files = [f for f in files if not f.isdigit()]
    return [subpart for f in non_digit_files for subpart in f.split('_')]

def create_formatted_title(split_files, title):
    """Create a formatted title string with the first file element prefixed."""
    if split_files:
        split_files[0] = " - " + split_files[0]
        formatted_title = ', '.join(split_files[:-1]) + ' and ' + split_files[-1]
    else:
        formatted_title = ''
    return f"{title}{formatted_title}"

def print_exercise_routine(directory, file_count, title):
    """Print a random line from each file in the specified directory and the formatted title."""
    split_files = get_filtered_filenames(directory)
    formatted_title = create_formatted_title(split_files, title)

    print(f"\n{formatted_title}")
    print("-" * len(formatted_title))

    for i in range(file_count):
        try:
            with open(f"{directory}/{i}", "r") as file:
                line = random.choice(file.readlines()).strip()
                print(line)
        except FileNotFoundError:
            print(f"File not found: {directory}/{i}")

def determine_day_of_week(args):
    """Determine the day of the week based on arguments."""
    days = ['monday', 'teusday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_of_week = datetime.datetime.today().weekday()

    if day_of_week >= 5:  # For weekends, choose a random weekday
        day_of_week = random.randint(0, 4)

    if args.day:
        day_arg = args.day.lower()
        if day_arg == "t":
            day_of_week = (day_of_week + 1) % 7
        elif day_arg == "r":
            day_of_week = random.randint(0, 4)
        elif day_arg in days:
            day_of_week = days.index(day_arg)
        else:
            raise ValueError("Invalid day argument.")
    
    return day_of_week

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Specify the day of the week.")
    args = parser.parse_args()

    try:
        day_of_week = determine_day_of_week(args)
    except ValueError as e:
        print(e)
        exit(1)

    weekly_routines = ['monday', 'teusday', 'wednesday', 'thursday', 'friday']
    print_exercise_routine("cardio", 6, "Cardio")
    print_exercise_routine(weekly_routines[day_of_week], 5, "Circuit Training")
    print_exercise_routine("mobility", 2, "Mobility and Flexibility Exercises")

if __name__ == "__main__":
    main()

