"""
Advent of code 2024
https://adventofcode.com/2024/day/12

--- Part One ---
"""


# Config
FILE_PATH = "inputs/2024-12-12-Input.txt"


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------


"""
Open the file and process line by line to store data
"""
def open_file(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file]



"""
Recursive fonction to search for garden type in a region
"""
def searching(matrix, pos, visited, results=None):

    # create results list if empty and append current position
    if results is None:
        results = []
    results.append(pos)

    visited[pos[0]][pos[1]] = True
    garden_type = matrix[pos[0]][pos[1]]
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Loop through all posible direction
    for path in ((-1,0),(0,1),(1,0),(0,-1)):

        # find the next possible position
        next_pos = tuple(a + b for a, b in zip(pos, path))
        
        # check if within the matrix boundaries, otherwise continue
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) :       
            continue

        # check if already visited or if next value is the same type
        if visited[next_pos[0]][next_pos[1]] or matrix[next_pos[0]][next_pos[1]] != garden_type:
            continue
        
        # keep searching
        searching(matrix, next_pos, visited, results)
    
    return results



"""
Fonction to count all the fences required for a position
"""
def count_fences(matrix, pos):

    # Init fences counter
    fences = 4

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Loop through all posible direction
    for path in ((-1,0),(0,1),(1,0),(0,-1)):

        # find the next possible position
        next_pos = tuple(a + b for a, b in zip(pos, path))
        
        # check if within the matrix boundaries, otherwise continue
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) :       
            continue

        # check if next value is the same type (don't need a fence)
        if matrix[next_pos[0]][next_pos[1]] ==  matrix[pos[0]][pos[1]]:
            fences -= 1
        
    return fences



# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    # Create a matrix (garden) from external input
    gardens = open_file(FILE_PATH)

    # Get size of the gardens
    rows = len(gardens)
    cols = len(gardens[0]) if rows > 0 else 0

    # Create a visited space list
    visited = [[False for _ in range(cols)] for _ in range(rows)]


    # For all the space in the gardens
    regions = []

    for row_index, row in enumerate(gardens):
        for col_index, pos in enumerate(row):

            # if space already visited, continue to next space
            if visited[row_index][col_index] == True:
                continue

            # Start searching for gardens
            regions.append(searching(gardens, (row_index, col_index), visited))


    
    # Calculte the amount of fences for all regions
    fences = []
    fences_region = 0

    for row_index, row in enumerate(regions):
        for col_index, pos in enumerate(row):
           fences_region += count_fences(gardens,pos)
        fences.append(fences_region)
        fences_region = 0

    
    # Calculate the fence price (amount of garden x amount of fence)
    solution = 0
    for index, value in enumerate(fences):
        solution += (len(regions[index]) * value)
        

    # Output the solution
    print("\nSolution:", solution)


if __name__ == "__main__":
    main()
