"""
Advent of code 2024
https://adventofcode.com/2024/day/4

--- Part One ---
"""


# Config
file_path = "inputs/2024-12-04-Input.txt"
solution = 0
word = "XMAS"
matrix = []


# Open the file and process line by line
# Store in a matrix
with open(file_path, "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)


word_length = len(word)
rows, cols = len(matrix), len(matrix[0])

directions = [
    (0, 1),   # Left to Right
    (0, -1),  # Right to Left
    (1, 0),   # Top to Bottom
    (-1, 0),  # Bottom to Top
    (1, 1),   # Top Left to Bottom Right
    (-1, -1), # Bottom Right to Top Left
    (1, -1),  # Top Right to Bottom Left
    (-1, 1)   # Bottom Left to Top Right
]

for row in range(rows):
        for col in range(cols):
            # Check if this cell is a potential starting point
            if matrix[row][col] == word[0]:
                # Try all directions
                for dr, dc in directions:
                    # Check if the word can fit in this direction
                    found = True
                    for i in range(word_length):
                        new_row = row + i * dr
                        new_col = col + i * dc

                        # Boundary check
                        if not (0 <= new_row < rows and 0 <= new_col < cols):
                            found = False
                            break

                        # Character match check
                        if matrix[new_row][new_col] != word[i]:
                            found = False
                            break

                    # If the word is found, record the result
                    if found:
                        # found_positions.append(((row, col), (dr, dc)))
                        solution += 1

# Output the solution
print("\nSolution:", solution)