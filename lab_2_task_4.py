a = int(input())
b = 1
c = 1
for i in range (0, a, 1) :
    d = c + b
    b = c
    c = d
    print (b)