import math
from functools import reduce

# Function to find the LCM of two numbers
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function to find the GCD of a list of numbers
def gcd_of_list(numbers):
    return reduce(math.gcd, numbers)

# Main function
def main():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Input the numbers
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
    
    # Calculate the LCM
    lcm_result = reduce(lcm, numbers)
    
    # Calculate the GCD
    gcd_result = gcd_of_list(numbers)
    
    # Output the results
    print("LCM of the numbers:", lcm_result)
    print("GCD of the numbers:", gcd_result)

# Run the program
if __name__ == "__main__":
    main()
