"""
Advent of code 2024
https://adventofcode.com/2024/day/11

--- Part Two ---

For this part, code had to be refactored to handle 75 blinks, which would generate a huge list (15 digits number)
A dictionary (Counter) is used to optimize count.

"""

from collections import Counter

# Config
FILE_PATH = "inputs/2024-12-11-Input.txt"
BLINKS = 75

# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------


def open_file(file_path):
    """
    Open the file and split the data in a list
    """

    with open(file_path, "r") as file:
       return list(map(int, file.read().split()))


def update_stone(stone):
    """
    Update stone based on the 3 rules
    """

    str_stone = str(stone)

    # 1 - If the stone is number 0, it is replaced by number 1.
    if stone == 0:
        return [1]

    # 2 - If the stone is even number of digits, it is replaced by two stones (with both digits)
    is_even = len(str_stone) % 2 == 0

    if is_even:

        # find middle and split in 2 stones
        mid_index = len(str_stone) // 2
        first_stone = str_stone[:mid_index]
        second_stone = str_stone[mid_index:]

        # return the string value (converted to int to remove extra 0)
        return [int(first_stone), int(second_stone)]

    # 3 - If none of the other rules apply, the old stone's number multiplied by 2024
    return [int(stone) * 2024]


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():
    # Create data list (stones) from external input
    stones = open_file(FILE_PATH)

    # Initialize stone counts
    stone_counts = Counter(stones)

    # for all the blinks, store values & count in dictionary
    for _ in range(BLINKS):
        new_counts = Counter()

        for stone, count in stone_counts.items():
            for new_stone in update_stone(stone): 
                new_counts[new_stone] += count
        stone_counts = new_counts

    # Total count of stones
    solution_count = sum(stone_counts.values())

    # Output the solution
    print("\nSolution:", solution_count)


if __name__ == "__main__":
    main()
