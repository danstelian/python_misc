import sys


def decorator_func(original_func):

    def wrapper_func(*args):
        print('wrapper executed this before', original_func.__name__)
        return original_func(*args)

    return wrapper_func


@decorator_func
def display():
    print('display ran')


@decorator_func
def display_info(name, age):
    print(sys._getframe().f_code.co_name, 'ran with arguments:', name, age)


display_info('John', 25)
