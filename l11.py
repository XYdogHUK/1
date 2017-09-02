def solve(f, x0, n):
    if n == 0:
        return x0
    else:
        return solve(f, f(x0), n - 1)


def eqn(x):
    return (x ** 2 + 5) / 6


x = solve(eqn, 0, 10)
print("решение: x=", x)
