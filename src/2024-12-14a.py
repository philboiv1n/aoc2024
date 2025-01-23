"""
Advent of code 2024
https://adventofcode.com/2024/day/14

--- Part One ---

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


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------


def main():

    # running time
    run = 100

    # find the middle lines
    mid_x = WIDE // 2
    mid_y = TALL // 2

    # init counter
    quad_counter = [0, 0, 0, 0]

    # open input data
    input = open_file(FILE_PATH)

    for config in input:
        px = config[0]  # initial x position
        py = config[1]  # initial y position
        vx = config[2]  # velocity for x
        vy = config[3]  # velocity for y

        # calculate new X and Y value
        new_px = (px + (vx * run)) % WIDE
        new_py = (py + (vy * run)) % TALL

        # check if value is in a quadrant (not on a middle line)
        if new_px != mid_x and new_py != mid_y:
            if new_px < mid_x:
                if new_py < mid_y:
                    quad_counter[0] += 1  # Quad 1
                else:
                    quad_counter[2] += 1  # Quad 3
            else:
                if new_py < mid_y:
                    quad_counter[1] += 1  # Quad 2
                else:
                    quad_counter[3] += 1  # Quad 4

    # Calculate safety factor
    safety_factor = 1
    for num in quad_counter:
        safety_factor *= num

    # Output the solution
    print("\nSolution:", safety_factor)


if __name__ == "__main__":
    main()
