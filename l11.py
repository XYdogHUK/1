def solve_eqn(f,x0,n):
    x=x0
    for k in range(1,n+1):
        x=f(x)
    return x
def eqn_1(x):
    return (x**2+5)/6
def eqn_2(x):
    return (6*x-5)**0.5
x=solve_eqn(eqn_1,0,10)
print("1-e yravnenie: x=",x)
x=solve_eqn(eqn_2,4,10)
print("2-e yravnenie: x=",x)