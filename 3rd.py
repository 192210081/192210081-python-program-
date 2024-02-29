def contains_digit(number, digit_to_exclude):
    return str(digit_to_exclude) not in str(number)
def print_numbers_except_digit(P, Q, R):
    for number in range(P, Q + 1):
        if contains_digit(number, R):
            print(number)
P = int(input("Enter the starting number (P): "))
Q = int(input("Enter the ending number (Q): "))
R = int(input("Enter the digit to exclude (R): "))
print(f"Numbers from {P} to {Q} except those containing the digit {R}:")
print_numbers_except_digit(P, Q, R)
