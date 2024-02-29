def count_value(statement):
    uppercase_count=0
    lowercase_count=0
    numbers_count=0
    for char in statement:
        if char== '*':
            break
        elif char.isupper():
            uppercase_count+=1
        elif char.islower():
            lowercase_count+=1
        elif char.isdigit():
            numbers_count+=1
    print("Total count of lower case:",lowercase_count, "total count of upper case:",uppercase_count,"total count of numbers:",numbers_count)
n=input("please enter any values")
count_value(n)
        
