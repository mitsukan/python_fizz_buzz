def decorator(input_function):
    def wrapper():
        prefix_printer('This is the prefix!')
        input_function()
        suffix_printer('This is the suffix!')

    def prefix_printer(string):
        print(string)

    def suffix_printer(string):
        print(string)

    return wrapper

def outer_function():
    print('This is the original function!')

construction = decorator(outer_function)

construction()

@decorator
def new_function():
    print("this is a new function!")

new_function()