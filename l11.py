x = 100


def test_vars():
    x = "local numb"
    print("in the body func x=", x)
    test_vars()
    print("out func x=", x)
