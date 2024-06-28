import numpy as baigashov

figure = input("Введите фигуру: ")

if figure == 'круг' :
    def circle_square (r) :
        crc_sqr = baigashov.pi * (r ** 2)
        return crc_sqr
    r = int(input("Введите радиус круга: "))
    print (f'Площадь круга: {circle_square (r)}')


if figure == 'прямоугольник' :
    def rectangle_square (a, b) :
        rct_sqr = a * b
        return rct_sqr
    a = int(input("Введите первую сторону прямоугольника: "))
    b = int(input("Введите вторую сторону прямоугольника: "))
    print (f'Площадь прямоугольника: {rectangle_square (a, b)}')

if figure == 'треугольник' :
    def triangle_square (a, h) :
        trng_sqr = (a * h) / 2
        return trng_sqr
    a = int(input("Введите сторону треугольника: "))
    h = int(input("Введите высоту треугольника: "))
    print (f'Площадь треугольника: {triangle_square (a, h)}')