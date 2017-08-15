res = eval(input('Введите что-нибудь:'))
resType = type(res)
if resType == int:
    print('Это целое число')
elif resType == float:
    print("Это действительное число ")
else:
    print("Наверное это текст")
print("Работа завершена")