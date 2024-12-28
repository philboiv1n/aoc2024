"""
Advent of code 2024
https://adventofcode.com/2024/day/3

--- Part One ---
"""


import re

# Config
file_path = "inputs/2024-12-03-Input.txt"
solution = 0


# Define the regex pattern to match and extract x and y (0 to 3-digit numbers)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Open and process the file line by line
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        # Find all matches and extract numbers
        matches = re.findall(pattern, line)
        for match in matches:
            x, y = map(int, match)  # Convert extracted strings to integers
            result = x * y
            solution += result

# Output the solution
print("\nSolution:", solution)