print("ax=b")
try:
    a = float(input("Введите a:"))
    b = float(input("Введите b:"))
    x = b / a
    print("решение уравнения: x=", x)
except ValueError:
    print("Нужно было ввести число")
except ZeroDivisionError:
    print("Внимание! На ноль делить нельзя")
print("the end")