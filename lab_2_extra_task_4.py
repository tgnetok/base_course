a = int(input('Введите число: '))
b = 2

while a > 1 :
    if a % b == 0 :
        print (b)
        a / b
        b = b + 1
    else :
        b = b + 1