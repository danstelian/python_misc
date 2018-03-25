# simple memoization example

from functools import wraps


def memoize(original_func):

    cache = {}

    @wraps(original_func)
    def wrapper(*args):
        print(f'Called memoize on {original_func.__name__}{args}')
        if args in cache:
            print('Cache hit!')
            result = cache[args]
        else:
            result = original_func(*args)
            cache[args] = result
        return result

    return wrapper


@memoize
def add(x, y):
    return x + y


print(add(2, 3))
print(add(99, 1))
print(add(2, 3))

print()
print(add)
print(add.__name__)
print(add.__qualname__)
print(add.__code__.co_name)
