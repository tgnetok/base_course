import matplotlib.pyplot as plt
import numpy as baigashov

x1 = int(input('Введите первое значение x: '))
x2 = int(input('Введите последнее значение x: '))
N = int(input('Введите количество точек: '))

def ellipse_plotter (a = 6, b = 2) :

    x = baigashov.linspace (x1, x2, N)
    y = baigashov.linspace (x1, x2, N)
    X, Y = baigashov.meshgrid(x, y)

    fxy = X ** 2 / a **2 + Y ** 2 / b ** 2 - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')

    plt.savefig ('yay_ellipse.png')

if __name__ == '__main__':
    ellipse_plotter () 