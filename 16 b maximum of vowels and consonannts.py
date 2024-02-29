

#16 Qb
def maximum(statement):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels_count=0
    cons_count=0
    for char in statement:
        if char in vowels:
            vowels_count+=1
        elif char in consonants:
            cons_count+=1
    print("vowels:",vowels_count,"consonants:",cons_count)
    
    if vowels_count>cons_count:
        print("The Maximum is in:vowels")
    if vowels_count<cons_count:
        print("The Maximum is in:consonants")
   
statement=input("Enter the statement")
maximum(statement)
