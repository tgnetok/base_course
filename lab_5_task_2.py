name = 'Vera Ivanova'

name_name = "_".join(name)
name_up = name_name.upper ()

name_list = []

for symbol in name_up:
    name_list.append (ord(symbol))
print (name_list)