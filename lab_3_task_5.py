import numpy as baigashov

N = int(input('Введите N: '))
M = int(input('Введите M: '))

trigonometry_array = baigashov.zeros ((N, M))

for i in range (0, N, 1) :
    for j in range (0, M, 1) :
        trigonometry_array[i, j] = baigashov.sin (N * i + M * j + 1) 
        if trigonometry_array [i, j] < 0 :
            trigonometry_array [i, j] = 0

print (trigonometry_array)


a = trigonometry_array [:, 1]
b = trigonometry_array [:, 2]
trigonometry_array [:, 1] = b
trigonometry_array [:, 2] = a

print (trigonometry_array)