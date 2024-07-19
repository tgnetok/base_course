import matplotlib.pyplot as plt
import numpy as baigashov

# логаифмическая спираль

def log_spiral (b = 1) :

    e = 2.718
    fi = baigashov.arange (0, 8*baigashov.pi + 1, 0.001)
    y = (e ** (b * fi)) * baigashov.sin(fi)
    x = y / baigashov.sin(fi) * baigashov.cos(fi)

    plt.plot (x,y)
    plt.axis('equal')
    plt.title ('log_spiral')
    plt.savefig ('log_spiral.png')
    
# архимедова спираль

def arch_spiral (k = 1) :

    fi = baigashov.arange (0, 8*baigashov.pi + 1, 0.1)
    r = k * fi
    y = r * baigashov.sin(fi)
    x = r * baigashov.cos(fi)

    plt.plot (x,y)
    plt.axis('equal')
    plt.title ('arch_spiral')
    plt.savefig ('arch_spiral.png')

# спираль «жезл»

def j_spiral (k = 1) :

    fi = baigashov.arange (0.01, 8*baigashov.pi + 1, 0.1)

    r = k / baigashov.sqrt(fi)
    y = r * baigashov.sin(fi)
    x = r * baigashov.cos(fi)

    plt.plot (x,y)
    plt.axis('equal')
    plt.title ('j_spiral')
    plt.savefig ('j_spiral.png')

# роза

def rose (k = 6) :

    fi = baigashov.arange (0.01, 8*baigashov.pi + 1, 0.1)
    r = baigashov.sin (k * fi)
    y = r * baigashov.sin(fi)
    x = r * baigashov.cos(fi)

    plt.plot (x,y)
    plt.axis('equal')
    plt.title ('rose')
    plt.savefig ('rose.png')

if __name__ == '__main__' :
    rose ()
    plt.clf()
    j_spiral ()
    plt.clf()
    arch_spiral ()
    plt.clf()
    log_spiral ()