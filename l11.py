print("поиск совпадающих элементов")
A=[2,False,9.1,2-1j,"hello",5,"Python"]
B=[5,3,"HELLO",7,12.5,"Python",True,False]
print("1-й список:",A)
print("2-й список:",B)
print("Совпадают:")
i=0
for a in A:
    i+=1
    j=0
    for b in B:
        j+=1
        if a==b:
            txt=str(i)+"-й элемент из 1-ого списка и "
            txt=txt+str(j)+"-й элемент из 2-ого списка"
            print(txt)
print("Поиск закончен")