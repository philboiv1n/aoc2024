"""
Advent of code 2024
https://adventofcode.com/2024/day/2

--- Part One ---
"""


from collections import Counter

# Config
file_path = "inputs/2024-12-02-Input.txt"
solution = 0 
data = []


# Open the file and process line by line
with open(file_path, "r") as file:
    for line in file:
        values = tuple(map(int, line.split()))
        data.append(values)

# Helper function to validate distances
def is_distance_valid(distance):
    return -3 <= distance <= 3 and distance != 0

for report in data:

    pointer = 0
    report_is_safe = True
    increase = None

    while pointer < len(report) - 1:
        distance = report[pointer] - report[pointer+1]
     
        # Check if the distance is valid
        if not is_distance_valid(distance):
            report_is_safe = False
            break

        # Determine the trend direction at the first comparison
        if increase is None:
            increase = distance > 0

        # Validate trend consistency
        if (increase and distance < 0) or (not increase and distance > 0):
            report_is_safe = False
            break

        pointer += 1
    
    if report_is_safe:
        solution += 1

# Output the solution
print("\nSolution:", solution)