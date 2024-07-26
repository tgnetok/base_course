def decorator (func) :
    return func

@decorator
def decorate_example () :
    print('Привет Вселенная!')
    
decorate_example()

decorate_example = decorator(decorate_example)
decorate_example()         

def decorator(func):
    def new_func():
        print('Казнить нельзя, помиловать!')
    return new_func

@decorator
def decorate_example():
    print('Казнить, нельзя помиловать.')
 
decorate_example()

print (decorate_example.__class__)
print (decorate_example.__name__)