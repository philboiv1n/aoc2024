"""
Advent of code 2024
https://adventofcode.com/2024/day/9

--- Part Two ---
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
   #  result = ""
    result = []
    id = 0
    for index, char in enumerate(input):
        # Block - Fill with id x char : ie : 
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


"""
Count the amount of occurence for an item in a list
"""
def get_count(id, list):
    count = 0
    for item in list:
        if item == id:
            count += 1
    return count




"""
Find empty space
"""
def find_empty_space(position, amount, list):
    
    count = 0
    write_pointer = -1

    for pos, item in enumerate(list):

        if item == ".":
            if count == 0 :
                write_pointer = pos
            count += 1
        else :
            count = 0
        
        if count >= amount :
            return write_pointer
        
        if pos >= position : 
            return -1



# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------


# Read input
input = open_file(file_path)


# Transform to blocks
blocks = convert_to_blocks(input)

last_block = len(blocks)-1
id = int(blocks[last_block])


# Go through all the list, start from the end
while id >= 0:

    print(id) # to show progression

    if id != "." :

        # identify block position
        position = blocks.index(str(id))
        
        # count occurence
        id_count = get_count(str(id), blocks)

        # Find if there is space before the current block position
        space = find_empty_space(position, id_count, blocks)

        # move if possible
        if space >= 0 :
            for i in range(id_count):
                blocks[space + i] = str(id)
                blocks[position + i] = "."
    
    id -= 1


# Calculate checksum
solution = checksum(blocks)

# Output the solution
print("\nSolution:", solution)