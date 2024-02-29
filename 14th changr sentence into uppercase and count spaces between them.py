def process_string(string):
    
    uppercase_string = string.upper()
    
    
    space_count = string.count(" ")
    
    return uppercase_string, space_count


input_string = "Python is the interpreted language"


uppercase_string, space_count = process_string(input_string)


print("Uppercase String:", uppercase_string)
print("Number of Spaces:", space_count)
