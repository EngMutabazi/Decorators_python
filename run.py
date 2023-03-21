def decorator_function(original_function):
    print("i am here")
    def wrapper_func(*args,**kwargs):
        return original_function(*args,**kwargs)
    return wrapper_func
@decorator_function
def display_func():
    print("Display function run!")
display_func()

@decorator_function
def display_info(name,age):
    print('Its run with the following args:({} {})'.format(name,age))

display_info("jacky", 36)
display_func()