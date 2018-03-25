import logging
import time
from functools import wraps


def logger_decorator(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args):
        logging.info(f'ran with args: {args}')
        return func(*args)

    return wrapper


def timer_decorator(func):

    @wraps(func)
    def wrapper(*args):
        t0 = time.time()
        result = func(*args)
        t = time.time() - t0
        print(func.__name__, f'ran in: {t:.8f} sec')
        return result

    return wrapper


@timer_decorator
@logger_decorator
def display_info(name, age):
    print('display_info ran with args:', name, age)


display_info('Tom', 22)

print(display_info.__name__)
print(display_info.__code__.co_name)
