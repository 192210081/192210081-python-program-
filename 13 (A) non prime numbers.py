#13a

def print_non_prime_numbers(A, B):
    for num in range(A + 1, B): 
        if num > 1:  
            for i in range(2, int(num ** 0.5) + 1): 
                if num % i == 0:
                    print(num, end=', ')
                    break
    print()  

print_non_prime_numbers(12, 19)
