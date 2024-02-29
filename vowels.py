def count_vowels(statement):
    vowels='aeiouAEIOU'
    count=0
    for char in statement:
        if char in vowels:
            count+=1
    return count
statement=input("enter a statement:")
print("number of vowels:",count_vowels(statement))
