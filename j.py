def count_vowels(a):
    vowels="aeiouAEIOU"
    count=0
    for char in a:
        if char in vowels:
            count=count+1
    return count

a=input("enter the string")
print("number of vowels",count_vowels(a))
