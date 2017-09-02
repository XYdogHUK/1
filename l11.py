x = 100


def test_vars():
    global x, y
    print("В теле функ x=", x)
    y = 200
    print("В теле функ y=", y)
    x = 300
    test_vars()
    print("Вне фун x=", x)
    print("Вне фун y=", y)
