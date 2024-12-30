"""
Advent of code 2024
https://adventofcode.com/2024/day/11

--- Part One ---
"""

# Config
FILE_PATH = "inputs/2024-12-11-Input.txt"
BLINKS = 25


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def open_file(file_path):
    """
    Open the file and split the data in a list
    """

    with open(file_path, "r") as file:
        return file.read().split()


def update_stone(stone):
    """
    Update stone based on the 3 rules 
    """
    
    str_stone = str(stone)

    # 1 - If the stone is number 0, it is replaced by number 1.
    if str_stone == "0":
        return ["1"]

    # 2 - If the stone is even number of digits, it is replaced by two stones (with both digits)
    is_even = len(str_stone) % 2 == 0

    if is_even:

        # find middle and split in 2 stones
        mid_index = len(str_stone) // 2
        first_stone = str_stone[:mid_index]
        second_stone = str_stone[mid_index:]

        # return the string value (converted to int to remove extra 0)
        return [str(int(first_stone)), str(int(second_stone))]

    # 3 - If none of the other rules apply, the old stone's number multiplied by 2024
    return [str(int(stone) * 2024)]


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():
    # Create data list (stones) from external input.
    stones = open_file(FILE_PATH)

    # for all the blinks
    for _ in range(BLINKS):

        temp_stones = []

        # for all the stones :
        for stone in stones:
            temp_stones.extend(update_stone(stone))

        stones = temp_stones

    # Output the solution
    print("\nSolution:", len(stones))


if __name__ == "__main__":
    main()