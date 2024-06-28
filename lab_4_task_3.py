# массу тела, высоту полета и скорость

import numpy as baigashov

m = int(input("Введите массу тела: "))
h = int(input("Введите высоту полета: "))
v = int(input("Введите скорость тела: "))
gravity_constant = 9.8

def energy_func (m, v, h, gravity_constant) :
    E = (m * (v ** 2) / 2) + (m * gravity_constant * h)
    return E

print (energy_func (m, v, h, gravity_constant))