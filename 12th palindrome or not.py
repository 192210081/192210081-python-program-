import random

def is_palindrome(input_str):
    return input_str == input_str[::-1]

def main():
    choice = random.choice(["string", "number"])
    if choice == "string":
        result_type = "string"
        input_value = input("Enter a string: ")
    else:
        result_type = "number"
        input_value = input("Enter a number: ")
    result = "palindrome" if is_palindrome(str(input_value)) else "not a palindrome"
    print(f"The {result_type} is {result}.")

if __name__ == "__main__":
    main()
