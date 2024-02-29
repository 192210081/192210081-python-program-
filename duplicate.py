
duplicate=[]
final_list=[]
n=int(input("Enter the number"))

for i in range(n):
    a=input("Enter the {} element".format(i+1))
    duplicate.append(a)
    
print(duplicate)
for num in duplicate:
    if num not in final_list:
        final_list.append(num)
print(final_list)


    
