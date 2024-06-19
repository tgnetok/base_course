a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))

x = ()
xFirst = ()
xSecond = ()
D = (b ** 2) - (4 * a * c)

if D < 0 :
    print ('Нет действительных корней.')

if D == 0 :
    x = - b / (2 * a)
    print (f'Корень уравнения: {x}.')

if D > 0 :
    xFirst = (- b + (D ** 0.5)) / (2 * a)
    xSecond = (- b - (D ** 0.5)) / (2 * a)
    print (f'Первый корень: {xFirst}. Второй корень: {xSecond}.')