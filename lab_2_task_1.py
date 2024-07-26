def plus_number (number) :
    def decorator (func) :
        def result_func (number_two):
            result = number + number_two
            print (result)
            return  result
        return result_func
    return decorator
    
@plus_number(666)
def number_func (yay) :
    return yay

number_func (666)