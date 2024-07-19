import numpy as baigashov
import matplotlib.pyplot as plt

def cicloida (R = 1) :
    t = baigashov.arange (1, 40, 0.01)

    x = R * (t - baigashov.sin (t))
    y = R * (1 - baigashov.cos (t))

    plt.plot(x, y, ls = '--')
    plt.axis('equal')
    plt.savefig('cicloida.png')

def astroida (R = 1) :
    t = baigashov.arange (1, 7.3, 0.01)

    x = R * ((baigashov.cos (t)) ** 3)
    y = R * ((baigashov.sin (t)) ** 3)

    plt.plot(x, y, ls = '--')
    plt.axis('equal')
    plt.savefig('astroida.png')

if __name__ == '__main__' :
    cicloida ()
    plt.clf()
    astroida ()