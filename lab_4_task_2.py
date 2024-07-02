import numpy as baigashov

arg_numbers_list = [1, 2, 3, 4]
arg_numbers_array = baigashov.array (arg_numbers_list)


def arr_func (arg_numbers_array) :
    # multiply = arg_numbers_array[0] * arg_numbers_array[1] * arg_numbers_array[2] * arg_numbers_array[3]
    P = 1
    for i in arg_numbers_list : 
        P *= i

    return multiply




print (arr_func (arg_numbers_array))