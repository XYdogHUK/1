print("Сумма натуральных чисел")
n = 100
text = "1+2+...+" + str(n) + " ="
i = 1
s = 0
while i <= n:
    s = s + i
    i=i+1
print(text,s)