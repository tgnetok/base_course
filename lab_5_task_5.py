my_name = 'Vera Ivanova'

name_up = my_name.upper () 
name_low = my_name.lower () 

up_ascii = [ord(symbol) for symbol in name_up]
low_ascii = [ord(symbol) for symbol in name_low]

sum_list = []

for i in range (0, len(low_ascii), 1) :
    sum_up_low = up_ascii[i] + low_ascii[i]
    sum_list.append (sum_up_low)

print (sum_list)