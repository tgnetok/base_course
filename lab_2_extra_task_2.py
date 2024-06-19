a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

if a + b < c or a + c < b or c + b < a :
    print ('Такого треугольника не существует.')
elif (a == b and a != c and b != c) or (a == c and c != b and a != b) or (b == c and b != a and c != a) :
    print ('Треугольник равнобедренный.') 
elif a == b == c :
    print ('Треугольник равносторонний.')
elif a != b != c :
    print ('Треугольник разносторонний.')