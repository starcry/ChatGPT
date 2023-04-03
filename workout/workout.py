#!/usr/bin/python3
import datetime
import random

# get the current day of the week
today = datetime.datetime.today().weekday()

# check if it's a working day (Monday to Friday)
if today < 5:
    # define the file names
    files = ["abs_core", "arms_grip", "back", "chest_shoulders", "gluts_hamstrings_legs"]

    # choose the file to import based on the day of the week
    file_to_import = files[today]

    # read the file and store the lines in a list
    with open(file_to_import) as f:
        lines = f.readlines()

    # get 5 random lines from the list
    random_lines = random.sample(lines, k=5)

    # print the random lines to stdout
    for line in random_lines:
        print(line.strip())

