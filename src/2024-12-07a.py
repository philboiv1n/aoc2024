"""
Advent of code 2024
https://adventofcode.com/2024/day/7

--- Part One ---
"""


from itertools import product

# Config
file_path = "inputs/2024-12-07-Input.txt"
solution = 0


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

"""
Open the file and process line by line to store data
"""
def open_file(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into the part before and after the colon
            key, values = line.split(":")
            # Process the values into a tuple of integers
            values_tuple = tuple(map(int, values.split()))
            # Append a tuple of the key (as int) and the values tuple
            data.append((int(key), values_tuple))
    return data


"""
Evaluate (from left to right) for + and * operators
"""
def evaluate_left_to_right(numbers):
    n = len(numbers) 
    results = []

    # Generate all operator combinations with "+" and "*"
    operators = list(product("+*", repeat=n-1)) 
    
    for ops in operators:
        # Start with the first number and construct left-to-right evaluation
        current_value = numbers[0]
        for i in range(n-1):
            if ops[i] == "+":
                current_value += numbers[i+1]
            elif ops[i] == "*":
                current_value *= numbers[i+1]
        results.append((current_value))
    return results


data = open_file(file_path)

for set in data:

    expected_result = set[0]
    results = evaluate_left_to_right(set[1])

    for result in results:
        if result == expected_result:
            solution += result
            break

# Output the solution
print("\nSolution:", solution)