import time
M = int(input('Введите последнюю переменную внешнего цикла: '))
N = int(input('Введите последнюю переменную внутреннего цикла: '))

timer = time.time ()
for i in range (M+1) : 
    print (i)
    time.sleep (1)
    for i in range (N+1) : 
        print (i)
        time.sleep (1)

print (f'{time.time () - timer}, seconds')