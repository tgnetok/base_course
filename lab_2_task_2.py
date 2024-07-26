def decorator (a, b, c) :
    if c == '*' :
        result = a * b
    elif c == '/' :
        result = a / b
    elif c == '+' :
        result = a + b
    elif c == '-' :
        result = a - b

    print (result)

decorator (3, 3, '/')