a = int(input('Первое число: '))
b = int(input('Второе число: '))

if b == 0 :
    print ('Второе число не может быть равно нулю.')
elif a % b == 0 :
    print ('Делится', a / b)
else :
    print ('Не делится', a % b, a / b)