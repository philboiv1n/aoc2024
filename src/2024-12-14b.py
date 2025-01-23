"""
Advent of code 2024
https://adventofcode.com/2024/day/14

--- Part Two ---

"""

import re

# Config
FILE_PATH = "inputs/2024-12-14-Input.txt"
WIDE = 101  # matrix col / x
TALL = 103  # matrix lines / y


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------


def open_file(file_path):
    """
    Open the file and process line by line to extract and store data

    Input example :
    p=4,72 v=24,-91
    p=54,28 v=82,-76
    p=2,89 v=-9,57

    Output:
    [(4,72,24,-91),(54,28,82,-7),(2,89,-9,57)]
    """

    # read file content
    with open(file_path, "r") as file:
        content = file.read()

    # split between lines
    items = content.strip().splitlines()

    # regex to extract data
    pattern = r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)"

    # go through all items, find and extract data then add to result
    result = []
    for item in items:
        matches = re.findall(pattern, item)
        item_tuples = (tuple(map(int, match)) for match in matches)
        result.extend(item_tuples)

    return result


def generate_positions(input, run, wide, tall):
    """
    return a list of all positions for a specific input and run
    """
    result = []

    for config in input:
        px = config[0]  # initial x position
        py = config[1]  # initial y position
        vx = config[2]  # velocity for x
        vy = config[3]  # velocity for y

        # calculate new X and Y value
        new_px = (px + (vx * run)) % wide
        new_py = (py + (vy * run)) % tall

        # add to result
        new_pos = (new_px, new_py)
        result.append(new_pos)

    return result


def find_pattern_in_coordinates(coordinates, pattern):
    """
    Identify occurrences of a specific pattern in a list of coordinates.
    """
    # Convert the list of coordinates into a set
    coord_set = set(coordinates)

    # Iterate over each point in the list
    for x, y in coordinates:
        # Check if all points in the pattern (relative to current point) exist
        if all((x + dx, y + dy) in coord_set for dx, dy in pattern):
            return True

    return False


def output_screen(positions, wide, tall):
    """
    Output a visuel of the position list to the screen
    """

    result = [["." for _ in range(tall)] for _ in range(wide)]

    for position in positions:
        result[position[0]][position[1]] = "x"

    for line in result:
        print("".join(line))


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------


def main():

    # running time in second
    run = 1
    max_run = 10000  # to prevent infinite loop
    result = False

    # open input data
    input = open_file(FILE_PATH)

    # I had no idea what to look for beside "a picture of a Christmas tree"
    # I tested different pattern (and output) and figured that there was a
    # frame around the tree so a horizontal line of 8 elements works for this input
    pattern = [(0, y) for y in range(8)]

    # while we cannot find the pattern (or the limit is reached)
    while not result and run <= max_run:

        # generate a list of all position for this run
        new_pos_list = generate_positions(input, run, WIDE, TALL)

        # check if the pattern exist for this list
        result = find_pattern_in_coordinates(new_pos_list, pattern)

        if result:
            output_screen(new_pos_list, WIDE, TALL)  # To see the picture :)
            # Output the solution
            print("\nSolution:", run)

        run += 1


if __name__ == "__main__":
    main()
