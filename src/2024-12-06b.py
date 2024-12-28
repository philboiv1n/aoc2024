"""
Advent of code 2024
https://adventofcode.com/2024/day/6

--- Part Two ---

P.S : This bruteforce solution is super slow and could be improved...
"""


import copy

# Config
file_path = "inputs/2024-12-06-Input.txt"
solution = 0
guard_direction = "^"
guard_position = [0,0]


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

"""
Open the file and process line by line to store in a matrix
"""
def open_file(file_path, matrix):
    with open(file_path, "r") as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix



"""
Find the guard initial position and initialize - assuming it starts with ^
"""
def init_guard(matrix):
    list = [0,0]
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col == "^":
                list[0], list[1] = row_index, col_index
                return (list)  # Return position as a tuple
    



""" 
Count the amount of character for a matrix
"""
def count_char(char, matrix):
    count = 0
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == char:
                count += 1
    return count



"""
Return the next direction from the directions tuple.
"""
def update_directions(guard_direction):
    directions = ("^", ">", "v", "<") 
    current_index = directions.index(guard_direction) 
    next_index = (current_index + 1) % len(directions) 
    return directions[next_index] 



"""
Check if the guard next move is out of bound
"""
def out_of_bound(matrix, guard_direction, guard_position):
    rows, cols = len(matrix), len(matrix[0])
    boundary_checks = {
        "^": guard_position[0] <= 0,
        ">": guard_position[1] >= cols-1,
        "v": guard_position[0] >= rows-1,
        "<": guard_position[1] <= 0
    }
    return boundary_checks.get(guard_direction, False)



"""
Check for obstacle
"""
def obstacle(matrix,guard_position, guard_direction):

    next_row = guard_position[0]
    next_col = guard_position[1]

    if guard_direction == "^" :
        next_row -= 1
    elif guard_direction == ">" :
        next_col += 1
    elif guard_direction == "v" :
        next_row += 1
    elif guard_direction == "<" :
        next_col -= 1

    if matrix[next_row][next_col] == "#":
        return True
    
    return False
    


"""
Move the guard
"""
def move(guard_direction, guard_position, ):

    if guard_direction == "^" :
        guard_position[0] -= 1
    elif guard_direction == ">" :
        guard_position[1] += 1
    elif guard_direction == "v" :
        guard_position[0] += 1
    elif guard_direction == "<" :
        guard_position[1] -= 1

    return guard_position



# -------------------------------------------------------------

# Open the input data and create a matrix
matrix_source = open_file(file_path, [])
matrix = copy.deepcopy(matrix_source)

# Find guard starting point and mark with X
guard_position = init_guard(matrix)
original_guard_position = tuple(copy.deepcopy(guard_position))


# Go through all the possible obstacle placement
for row_index, row in enumerate(matrix):
    for col_index, col in enumerate(row):

        test_matrix = copy.deepcopy(matrix_source)
        if (row_index,col_index) != original_guard_position:
            test_matrix[row_index][col_index] = "#"

        guard_position = list(original_guard_position)
        guard_direction = "^"
        loop_counter = 0

        while not out_of_bound(test_matrix, guard_direction, guard_position) :
            
            if loop_counter > len(matrix_source) ** 2:
                solution += 1
                print(solution) # To show progression
                break

            loop_counter += 1
            
            if obstacle(test_matrix, guard_position, guard_direction) :
                guard_direction = update_directions(guard_direction)
            else :
                guard_position = move(guard_direction, guard_position)

# Output the solution
print("\nSolution:", solution)