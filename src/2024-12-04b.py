"""
Advent of code 2024
https://adventofcode.com/2024/day/4

--- Part Two ---
"""


# Config
file_path = "inputs/2024-12-04-Input.txt"
solution = 0
word = "MAS"
matrix = []
middle_letter = word[int(len(word)/2)]


# Open the file and process line by line
# Store in a matrix
with open(file_path, "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

rows, cols = len(matrix), len(matrix[0])


# go through all the rows and cols
for row in range(rows):
        for col in range(cols):
            
            # Check if this cell is a potential starting point
            if matrix[row][col] == middle_letter:

                # if outside ouf the matrix
                if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                     continue
                
                # get the 4 letters to make a X
                top_left = matrix[row-1][col-1]
                bot_right = matrix[row+1][col+1]
                top_right = matrix[row-1][col+1]
                bot_left = matrix[row+1][col-1]

                # improved validation :
                if {top_left, bot_right} == {word[0], word[2]} and {top_right, bot_left} == {word[0], word[2]}:
                     solution += 1


# Output the solution
print("\nSolution:", solution)