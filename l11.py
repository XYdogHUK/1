print("ax=b")
try:
    a = float(input("Введите a:"))
    b = float(input("Введите b:"))
    x = b / a
    print("решение уравнения: x=",x)
except:
    print("Вы ввели некорректные данные")
print("the end")