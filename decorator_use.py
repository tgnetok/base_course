def decorator_1 (func) :
    def f () :
        print ('Декоратор 1 до функции')
        func ()
        print ('Декоратор 1 после функции')
    return f

def decorator_2 (func) :
    def f () :
        print ('Декоратор 2 до функции')
        func ()
        print ('Декоратор 2 после функции')
    return f

@decorator_1
@decorator_2
def func_1 () :
    print ('Функция началав свою работу')
    x = 1 + 1
    print ('Функция завершила свою работу')

func_1 ()