
def find_MSD(number):
    
    while number >= 10:
        number = number // 10
    return number


def find_LSD(number):
    
    return number % 10


num = int(input("Enter a number: "))


msd = find_MSD(num)
lsd = find_LSD(num)


print("Most Significant Digit:", msd)
print("Least Significant Digit:",lsd)
