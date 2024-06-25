import numpy as baigashov

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

list_numbers = [first_num, second_num]
array_numbers = baigashov.array (list_numbers)

def average_value (array_numbers) :
    av_val = (array_numbers[0] + array_numbers[1]) / 2
    return av_val

print (average_value (array_numbers))