def sq_sum():
    def get_n():
        n=int(input("Слагаемые в сумме:"))
        return n
    def find_sq_sum():
        s=0
        for i in range(1,n+1):
            s+=i**2
        return s
    n=get_n()
    return  find_sq_sum
z=sq_sum()()
print("Сумма квадратов равна:",z)