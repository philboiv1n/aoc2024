"""
Advent of code 2024
https://adventofcode.com/2024/day/3

--- Part Two ---
"""


import re

# Config
file_path = "inputs/2024-12-03-Input.txt"
solution = 0


# Init go variable - Default to True
go = True

# Define regex pattern to match and extract x and y (0 to 3-digit numbers)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

# Open and process the file line by line
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):

        # Find all matches and extract numbers
        matches = re.finditer(pattern, line)

        for match in matches:
            if match.group(1) and match.group(2) and go:  # Match for `mul(x,y)`
                x, y = match.group(1), match.group(2)
                result = int(x) * int(y)
                solution += result
            elif match.group(0) == "do()":
                go = True
            elif match.group(0) == "don't()":
                go = False

# Output the solution
print("\nSolution:", solution)