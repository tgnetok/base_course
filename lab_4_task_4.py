import numpy as baigashov


def function_function (a, b, N) :
    x = baigashov.linspace (a, b, N+2)
    x = baigashov.delete (x, [0, -1])
    y = x ** 2
    return y

a = int(input("Введите начальную координату x: "))
b = int(input("Введите введите конечную координату x: "))
N = int(input("Введите количество полученных точек: "))

print (function_function (a, b, N))
