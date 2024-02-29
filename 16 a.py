def count(statement):
    special_characters="!@#$%^&*()_+"
    s_count=0
    for char in statement:
        if char in special_characters:
            s_count+=1
    print("Number of special characters:",s_count)
a=input("Enter the statement")
count(a)
