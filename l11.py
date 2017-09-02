def print_text(txt="Значение аргумента по умолчанию."):
    print(txt)


def show_args(a, b="Второй аргумент не указан."):
    print(a, b)


def my_func(x="1-й аргумент x.", y="2-й аргумент y.", ):
    print(x, y)


print_text("Явно указан.")
print_text()
show_args("Первый.", "Второй")
show_args("Первый.")
my_func()
my_func("Один из аргументовю")
my_func(y="Один из аргументовю")

