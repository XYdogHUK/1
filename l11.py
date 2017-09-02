def my_pow(n):
    return lambda x: x ** n


for n in range(1, 4):
    for x in range(1, 11):
        print(my_pow(n)(x), end=" ")
    print()
