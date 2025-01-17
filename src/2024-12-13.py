"""
Advent of code 2024
https://adventofcode.com/2024/day/13

--- Part One and Two ---

Special thanks to AI for the help with the math. 
Part One took much more time to figure out (without brute forcing),
Then part two was already done (see below).

"""

import re

# Config
FILE_PATH = "inputs/2024-12-13-Input.txt"


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def open_file(file_path):

    """
    Open the file and process line by line to extract and store data
 
    Input example : 
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Output:
    [(94,34),(22,67),(8400,5400), ((26, 66), (67, 21), (12748, 12176))]
    """
    
    # read file content
    with open(file_path, "r") as file:
        content = file.read() 

    # split between empty line
    items = content.strip().split("\n\n")

    # regex to extract data (anything after X=, X+, Y=, Y+)
    pattern = r"X[+=](\d+), Y[+=](\d+)"
   
    # go through all items, find and extract data then add to result
    result = []
    for item in items:
        matches = re.findall(pattern, item)  
        item_tuples = [tuple(map(int, match)) for match in matches]  
        result.append(tuple(item_tuples))
        
    return result



def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients x, y."""
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a, x = 1, y = 0
    gcd, x1, y1 = extended_gcd(b, a % b) 
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y



def solve_diophantine(a1, b1, c1, a2, b2, c2):
    """
    Solve the system of two linear Diophantine equations:
    a1 * x + b1 * y = c1
    a2 * x + b2 * y = c2
    """

    # Step 1: Solve the first equation for x and y
    gcd1, x1, y1 = extended_gcd(a1, b1)
    
    # Check if the first equation is solvable
    if c1 % gcd1 != 0:
        raise ValueError("No solution for equation 1.")
    
    # Scale the solution to match c1
    x1 *= c1 // gcd1
    y1 *= c1 // gcd1
    
    # General solution for the first equation
    k1_factor = b1 // gcd1
    k2_factor = -a1 // gcd1

    # Step 2: Substitute the general solution into the second equation
    a2k = a2 * k1_factor + b2 * k2_factor  # Coefficient of k
    c2_adj = c2 - (a2 * x1 + b2 * y1) # Adjusted constant term

    # Ensure that the coefficient of k divides the adjusted constant term
    if c2_adj % a2k != 0:
        raise ValueError("No solution for equation 2.")
    
    # Solve for k
    k = c2_adj // a2k

    # Step 3: Compute the particular solution
    x = x1 + k * k1_factor
    y = y1 + k * k2_factor 

    return x, y



# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    solution = 0
    input = open_file(FILE_PATH)

    for config in input:
        """
        config example
        (94,34),(22,67),(8400,5400)
        """
        a1 = config[0][0] # ie 94
        b1 = config[1][0] # ie 22
        a2 = config[0][1] # ie 34
        b2 = config[1][1] # ie 67

        # For part One 
        c1 = config[2][0] 
        c2 = config[2][1]
       
        # For part Two (add distance for prize)
        # c1 = config[2][0] + 10000000000000
        # c2 = config[2][1] + 10000000000000
        
        try:
            x, y = solve_diophantine(a1, b1, c1, a2, b2, c2)
            solution += (x*3)+y # calculate price
        except ValueError :
            pass


    # Output the solution
    print("\nSolution:", solution)


if __name__ == "__main__":
    main()