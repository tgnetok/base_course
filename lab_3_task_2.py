import numpy as baigashov

h = 100
alpha = baigashov.pi / 3
beta = 30 / 180 * baigashov.pi
from lab_3_task_1 import g 

v = baigashov.sqrt ((g * h * baigashov.tan(beta) ** 2) / (2 * (baigashov.cos(alpha)) ** 2 * (1 - baigashov.tan(beta) * baigashov.tan(alpha))))
print (v)

from lab_3_task_1 import k
from lab_3_task_1 import e
from lab_3_task_1 import h
T = 200 
epsilon = 300 # otsosi u traktorista

N = (2 / baigashov.sqrt (baigashov.pi)) * (h / (k * T) ** 3/2) * e ** (-epsilon/k * T) * epsilon ** (T/2)
print (N)

