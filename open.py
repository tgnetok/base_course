#f = open("путь к файлу", режим открытия)
f = open('data.txt', mode='w')

def logger (func) :
    # def wrapper_function(*args, **kwargs):
    def wrapper_function(list_of_num):
        # result = func(*args, **kwargs)
        result = func(list_of_num)
        f = open("demofile.txt", "w")
        f.write(str(result))
        return result
    return wrapper_function   

@logger
def summator (list_of_num) :
    return sum (list_of_num)

summator ([1, 2, 3, 4])
f.close ()