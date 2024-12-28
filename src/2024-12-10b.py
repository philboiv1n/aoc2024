"""
Advent of code 2024
https://adventofcode.com/2024/day/10

--- Part Two ---
"""


# Config
file_path = "inputs/2024-12-10-Input.txt"
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
            row = list(line.strip())
            data.append(row)
    return data



""" 
Filter a matrix to return the location of a specific string
"""
def filter_by_char(matrix, string):

    results = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for row_index in range(rows):
        for col_index in range(cols):
            if matrix[row_index][col_index] == string:
                pos = (row_index, col_index)
                results.append(pos)
    return results


"""
Recursive function to find the path...
"""
def trekking(matrix, pos, results=None):

    if results is None:
        results = []

    paths = ((-1,0),(0,1),(1,0),(0,-1))
    height = int(matrix[pos[0]][pos[1]]) 
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for path in paths:

        # find the next possible position
        next_pos = tuple(a + b for a, b in zip(pos, path))
        
        # check if within the matrix boundaries
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) :       
            continue

        # check if different than a dot and equal to the next height
        next_value = matrix[next_pos[0]][next_pos[1]]
        if (next_value == "." or int(next_value) != height + 1) :
            continue
        
        if int(next_value) == 9 :
            results.append(next_pos)
        
        trekking(matrix,next_pos, results)
    
    return results

# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

# Create matrix from input
matrix = open_file(file_path)


# Filter the input to get a specific string (i.e 0)
zeros = filter_by_char(matrix,"0")


# For all position in the matrix
for pos in zeros :
    result = trekking(matrix, pos)
    solution = solution + len(result)
    

# Output the solution
print("\nSolution:", solution)