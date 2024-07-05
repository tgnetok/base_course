import numpy as baigashov
import random

N = int(input('Введите длину массивов: '))

list_one = []
list_two = []
list_three = []

for i in range (0, N, 1) :
    values_one = random.randint (0, 100)
    list_one.append (values_one)
for i in range (0, N, 1) :
    values_two = random.randint (0, 100)
    list_two.append (values_two)
for i in range (0, N, 1) :
    values_three = random.randint (0, 100)
    list_three.append (values_three)

array_one = baigashov.array (list_one)
array_two = baigashov.array (list_two)
array_three = baigashov.array (list_three)

max_list = [max(array_one), max(array_two), max(array_three)]

print (max(max_list))