def maximum(statement):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    v_count=0
    c_count=0
    for char in statement:
        if char in vowels:
            v_count+=1
        if char in consonants:
            c_count+=1
    print("Number of vowels:",v_count)
    print("Number of consonants:",c_count)
    if v_count>c_count:
        print("Maximum are vowels")
    else:
        print("Maximum are consonants")
a=input("Enter the statement")
maximum(a)
