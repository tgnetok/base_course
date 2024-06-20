import numpy as np

h = 100
alpha = np.pi / 3
beta = 30 / 180 * np.pi
from lab_3_task_1 import g 

v = np.sqrt ((g * h * np.tan(beta) ** 2) / (2 * (np.cos(alpha)) ** 2 * (1 - np.tan(beta) * np.tan(alpha))))
print (v)

from lab_3_task_1 import k
from lab_3_task_1 import e
from lab_3_task_1 import h
T = 200 
epsilon = 300 # otsosi u traktorista

N = (2 / np.sqrt (np.pi)) * (h / (k * T) ** 3/2) * e ** (-epsilon/k * T) * epsilon ** (T/2)
print (N)