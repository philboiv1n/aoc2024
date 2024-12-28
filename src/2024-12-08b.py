"""
Advent of code 2024
https://adventofcode.com/2024/day/8

--- Part Two ---
"""


# Config
file_path = "inputs/2024-12-08-Input.txt"
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
Find the other antennas with the same character in a matrix.
Return a list of antennas and position
"""
def find_other_antennas(matrix, antenna):

    results = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for row_index in range(rows):
        for col_index in range(cols):
            char = matrix[row_index][col_index]
            pos = (row_index, col_index)

            if char != "." and char == antenna[0] and pos != antenna[1]:
                result = [None,None]
                result[0] = char  
                result[1] = pos   
                results.append(result)

    return results


# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

matrix = open_file(file_path)
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0
antinode_lake = []


# For all the characters in the matrix
for row_index in range(rows):
    for col_index in range(cols):
        char = matrix[row_index][col_index]
        pos = (row_index,col_index)

        # if char is not . , it's antenna
        if char != ".":
            antenna = [None,None]
            antenna[0] = char
            antenna[1] = pos

            antinode_lake.append(pos)

            # Get a list of all the other antennas with the same character
            antennas = find_other_antennas(matrix, antenna)
            
            # Calcultate the distance (row-col) from that occurence
            for new_antenna in antennas:
                cur_row = pos[0]
                cur_col = pos[1]
                new_row = new_antenna[1][0]
                new_col = new_antenna[1][1]

                distance = [new_row-cur_row, new_col-cur_col]

                i = 0
                while i < rows:
                    i += 1
                    antinode = (new_row+(distance[0]*i), new_col+(distance[1]*i))

                    if (antinode[0] >= 0 and antinode[0] <= rows-1) and (antinode[1] >= 0 and antinode[1] <= cols-1):
                        antinode_lake.append(antinode)   

solution = len(set(antinode_lake))

# Output the solution
print("\nSolution:", solution)