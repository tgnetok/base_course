import numpy as baigashov

list_one = [1, 45, 75, 8, 4, 12]
list_two = [5, 6, 34, 38, 2]
list_three = [23, 94, 25, 4, 8, 36]

array_one = baigashov.array (list_one)
array_two = baigashov.array (list_two)
array_three = baigashov.array (list_three)

max_list = [max(array_one), max(array_two), max(array_three)]

print (max(max_list))