res = eval(input('Введите что-нибудь:'))
resType = type(res)
if resType == int:
    print('Это целое число')
if resType == float:
    print("Это действительное число")
if resType != int and resType != float:
    print("Тут точно не цифры")
print("Всё, отстань")
