def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack == []


input_string = input("Enter a string containing only the characters '(', ')', '{', '}', '[' and ']': ")

result = isValid(input_string)


if result:
    print("true.")
else:
    print("false.")
