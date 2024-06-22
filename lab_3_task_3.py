import numpy as baigashov
from lab_3_task_1 import g 

x_start = int(input('Введите начальную координату x: '))
y_start = int(input('Введите начальную координату y: '))
v_start = int(input('Введите начальную скорость тела: '))
list = []
for t in range (0, 6, 1) :
    x = x_start + (v_start * t)
    y = y_start + (v_start * t) - ((g * t ** 2) / 2)
    list.append ([t, x, y])
array_results = baigashov.array (list)
print (array_results)
    