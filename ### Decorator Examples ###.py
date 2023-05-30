### Decorator Examples ###

def decorator_func(function):
    def wrapper_func():
        print("This is Wrapper Function")
        return function()
    print("This is Decorator Function")
    return wrapper_func

@decorator_func

def show():
    print("show working")

show()  