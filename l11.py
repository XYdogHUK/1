def find_value(f, x):
    print("x=", x, "->f(x)=", f(x))


my_func = lambda x: 1 / (1 + x ** 2)
find_value(my_func, 2.0)
find_value(lambda x: x * (1 - x), 0.5)
z=1+(lambda x,y: x*y-x**2) (2,3)**2
print("z=",z)