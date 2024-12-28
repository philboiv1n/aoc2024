"""
Advent of code 2024
https://adventofcode.com/2024/day/5

--- Part Two ---
"""


# Config
file_path = "inputs/2024-12-05-Input.txt"
solution = 0

# Open the file and process line by line
# Store in a matrix
with open(file_path, "r") as file:
    content = file.read()

# Split the content by blank lines
data_sets = content.strip().split("\n\n")

# Process the rules data set
rules = []
for line in data_sets[0].strip().split("\n"):
    rules.append([int(x.strip()) for x in line.split("|")])

# Process the updates data set
updates = []
for line in data_sets[1].strip().split("\n"):
    updates.append([int(x.strip()) for x in line.split(",")])

for update in updates:

    update_fixed = False  # Flag to track if this update was corrected
    rules_ok = False      # Assume there are rule violations initially

    while not rules_ok:  
        rules_ok = True

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                idx_a = update.index(rule[0])
                idx_b = update.index(rule[1])

                if idx_a > idx_b:  # Rule violated
                    # Swap to fix the order
                    update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                    rules_ok = False  # Mark as needing another pass
                    update_fixed = True  # Mark that the update was fixed

    # Add the middle page to the total only if the update was fixed
    if update_fixed:
        middle_page = update[len(update) // 2]
        solution += middle_page

# Output the solution
print("\nSolution:", solution)
