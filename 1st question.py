n=int(input("Enter the rows"))

a=input("Enter the character to be printed")

for i in range(n+1):
    for j in range(i):
        print(a ,end=" ")
    print()
   
