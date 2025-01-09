"""
Advent of code 2024
https://adventofcode.com/2024/day/12

--- Part Two ---
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
Fonction to count all the fences for a regions
"""
def count_fences_region(region):

    fences = 0
    for garden in region:

        # Init fences counter at 4, will remove unwanted fence
        fences += 4
       
        # Loop through all posible direction
        for path in ((-1,0),(0,1),(1,0),(0,-1)): # top, right, bottom, left

            # find the next position to investigate
            next_pos = tuple(a + b for a, b in zip(garden, path))

            # if next to the same type, remove fence
            if next_pos in region:
                fences -= 1
            else :    
                if path[1] == 0 :
                    # if looking top or down
                    side_fence = ((garden[0]),garden[1]-1)
                    next_side_fence = ((next_pos[0]),next_pos[1]-1)    
                else :
                    # if looking left and right
                    side_fence = ((garden[0]-1),garden[1])
                    next_side_fence = ((next_pos[0]-1),next_pos[1])
            
                # if fence is already started
                if side_fence in region and next_side_fence not in region:
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


    # Calculate the fence price (amount of garden x amount of fence)
    solution = 0
    for region in regions:
        solution += len(region) * (count_fences_region(region))


    # Output the solution
    print("\nSolution:", solution)


if __name__ == "__main__":
    main()
