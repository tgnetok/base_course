import matplotlib.pyplot as plt
import numpy as baigashov

x1 = int(input('Введите первое значение x: '))
x2 = int(input('Введите последнее значение x: '))
N = int(input('Введите количество точек: '))

def hyperbola_plotter (k = 3) :

    x = baigashov.linspace (x1, x2, N)
    y = k / x

    plt.plot (x, y) 
    plt.title ('hyperbola')

    plt.savefig ('yay_hyperbola.png')