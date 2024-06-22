import numpy as baigashov

N = int(input('Введите N: '))
M = int(input('Введите M: '))

trigonometry_array = baigashov.array ([N, M], int)

[N, M] = [i, j]

for N in range (0, N, 1) :
    for M in range (0, M, 1) :
        trigonometry_array[i, j] = baigashov.sin (N * i + M * j + 1) 
        if trigonometry_array[N] < 0 :
            trigonometry_array[N] == 0
        if trigonometry_array[M] < 0 :
            trigonometry_array[M] == 0

print (trigonometry_array)