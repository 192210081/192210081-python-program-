def create_tuple_list(n):
    tuple_list = [(x, x**2) for x in range(1, n+1)]
    return tuple_list


n = 5
result = create_tuple_list(n)
print(result)
