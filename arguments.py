def decorator (func) :
    #def wrapper_function(*args, **kwargs):
    def wrapper_function(str):
      	#func(*args, **kwargs)
        func(str) 

@decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Анастасия")