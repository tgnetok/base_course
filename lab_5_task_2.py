name = 'Vera Ivanova'

name_name = "_".join(name)
name_up = name_name.upper ()

name_list = []

for symbol in name_up:
    name_list.append (ord(symbol))
print (name_list)
print (max(name_list))

name_name = "_".join(name)
name_low = name_name.lower ()

name_list = []

for symbol in name_low:
    name_list.append (ord(symbol))
print (name_list)
print (max(name_list))