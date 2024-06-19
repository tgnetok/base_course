a = int(input('Введите число: '))
c = len(str(a))

for i in range (0, c, 1) :
    b = a // 10
    a = a % 10
    print (a) 
    a = b