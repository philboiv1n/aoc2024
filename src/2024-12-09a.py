"""
Advent of code 2024
https://adventofcode.com/2024/day/9

--- Part One ---
"""


# Config
file_path = "inputs/2024-12-09-Input.txt"
solution = 0


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

"""
Open the file and process line by line to store data
"""
def open_file(file_path):
    with open(file_path, "r") as file:
        content = file.read() 
    return content


"""
Convert input to individual blocks
Return a string array
"""
def convert_to_blocks(input):
    result = []
    id = 0
    for index, char in enumerate(input):
        # Block - Fill with id x char :
        if not index % 2: 
            for i in range(int(char)):
                result.append(str(id))
            id += 1
        # Free Space - Fill with dots
        else : 
           for i in range(int(char)):
                result.append(".")
    return result


"""
Compact block to remove empty space at the end of the file
"""
def compact(blocks):
    for index,char in enumerate(blocks):
        print(index) # to show progression

    # if not a dot, continue to the next character
        if char != "." :
            continue
    
        # Counter that starts at the end of the string
        reverse_counter = len(blocks)-1

        # Go from the end until the index is reached
        while reverse_counter > index:

            # if it's a number, swap
            if blocks[reverse_counter] != "." :
                blocks[index] = blocks[reverse_counter]
                blocks[reverse_counter] = "." 
                break

            reverse_counter -= 1
    
    return blocks


"""
Calculate checksum
"""
def checksum(compacted):
    solution = 0
    for key,value in enumerate(compacted):
        if value != ".":
            solution += int(key) * int(value)
    
    return solution


# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

# Read input
input = open_file(file_path)

# Transform to blocks
blocks = convert_to_blocks(input)

# Compact blocks
compacted = compact(blocks)

# Calculate checksum
solution = checksum(compacted)

# Output the solution
print("\nSolution:", solution)