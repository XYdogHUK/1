n = 500
dz = 1 / n;
pts = 0
i = 0
while i <= n:
    x = dz * i
    j = 0
    while j <= n:
        y = dz * j
        if y <= x and y >= x ** 2:
            pts = pts + 1
        j += 1
    i += 1
s = pts / (n + 1) ** 2
print("Площадь фигуры:",s)
