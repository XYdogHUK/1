print("проверяем список")
myList=[1,3+2j,True,4.0]
print("Список:",myList)
for s in myList:
    if type(s)==str:
        print("В списке есть текстовые элементы")
        break
else:
    print("В списке нет текстовых элементов")
print("Конец")