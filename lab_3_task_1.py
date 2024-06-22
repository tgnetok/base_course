import numpy as baigashov

G = 6.674 * 10 ** -11
c = 2.99792458 * 10 ** 8
h = 6.626 * 10 ** -34
e = 2.71828
k = 1.380 * 10 ** -23
n = 6.022140 * 10 ** 24
F = 96485.332
R = 8.314462
V = 22.413969
g = 9.806

phys_const = [f'{G}, {c}, {h}, {e}, {k}, {n}, {F}, {R}, {V}, {g}']

phys_const_array = baigashov.array (phys_const)