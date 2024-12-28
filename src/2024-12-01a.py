"""
Advent of code 2024
https://adventofcode.com/2024/day/1

--- Part One ---
"""


# Config
file_path = "inputs/2024-12-01-Input.txt"
solution = 0
list1, list2 = [], []


# Open the file and process line by line
with open(file_path, "r") as file:
    for line in file:
        val1, val2 = map(int, line.split())
        list1.append(val1)
        list2.append(val2)

list1.sort()
list2.sort()

for val1, val2 in zip(list1,list2):
    solution += abs(val1-val2)

# Output the solution
print("\nSolution:", solution)