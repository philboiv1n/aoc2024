"""
Advent of code 2024
https://adventofcode.com/2024/day/5

--- Part One ---
"""


# Config
file_path = "inputs/2024-12-05-Input.txt"

# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

"""
Parse the rules section into a list of tuples.
"""
def parse_rules(rules_section):
    return [tuple(map(int, line.split("|"))) for line in rules_section.strip().split("\n")]

"""
Parse the updates section into a list of lists.
"""
def parse_updates(updates_section):
    return [list(map(int, line.split(","))) for line in updates_section.strip().split("\n")]

"""
Check if the update satisfies the rules.
"""
def is_update_valid(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

"""
Calculate the total sum of middle pages of valid updates.
"""
def calculate_middle_page_sum(updates, rules):
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            middle_index = len(update) // 2
            total += update[middle_index]
    return total

# Main logic
with open(file_path, "r") as file:
    content = file.read()

# Split the content into rules and updates
rules_section, updates_section = content.strip().split("\n\n")

# Parse the input data
rules = parse_rules(rules_section)
updates = parse_updates(updates_section)

# Calculate the solution
solution = calculate_middle_page_sum(updates, rules)

# Output the solution
print("\nSolution:", solution)