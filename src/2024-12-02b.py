"""
Advent of code 2024
https://adventofcode.com/2024/day/2

--- Part Two ---
"""


from collections import Counter

# Config
file_path = "inputs/2024-12-02-Input.txt"
solution = 0
data = []


# Open the file and process line by line
with open(file_path, "r") as file:
    for line in file:
        values = list(map(int, line.split()))
        data.append(values)

# Helper function to validate distances
def is_distance_valid(distance):
    return -3 <= distance <= 3 and distance != 0

# Function to check if a report is safe, optionally removing one level
def is_safe_with_tolerance(report):
    for i in range(len(report)):
        # Create a copy of the report with one level removed
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# Function to check if a report is safe
def is_safe(report):
    pointer = 0
    increase = None

    while pointer < len(report) - 1:
        distance = report[pointer] - report[pointer + 1]

        # Check if the distance is valid
        if not is_distance_valid(distance):
            return False

        # Determine the trend direction at the first comparison
        if increase is None:
            increase = distance < 0

        # Validate trend consistency
        if (increase and distance > 0) or (not increase and distance < 0):
            return False

        pointer += 1

    return True

# Main processing loop
for report in data:
    if is_safe(report) or is_safe_with_tolerance(report):
        solution += 1

# Output the solution
print("\nSolution:", solution)