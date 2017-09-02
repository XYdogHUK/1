import math


def solve_deqn(f, x0, y0, x):
    n = 1000
    dx = (x - x0) / n
    x = x0
    y = y0
    for k in range(1, n + 1):
        y = y + dx * f(x, y)
        x = x + dx
    return y


def diff_eqn(x, y):
    return 2 * x - y


def y(x):
    return 2 * (x - 1) + 5 * math.exp(-x)


h = 0.5
for k in range(0, 6):
    x = k * h
    print("Числовое решение:")
    print("x=", x, "-> y(x)=", solve_deqn(diff_eqn, 0, 3, x))
    print("Точное решение:")
    print("x=", x, "-> y(x)=", y(x))
