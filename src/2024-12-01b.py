"""
Advent of code 2024
https://adventofcode.com/2024/day/1

--- Part Two ---
"""


from collections import Counter

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

counter_list1 = Counter(list1)
counter_list2 = Counter(list2)

# Iterate through unique values in list1
for ref_num in counter_list1.keys():
    sum_ref_num = ref_num * counter_list1[ref_num]
    amount_ref_num_list2 = counter_list2.get(ref_num, 0)
    solution += sum_ref_num * amount_ref_num_list2

# Output the solution
print("\nSolution:", solution)