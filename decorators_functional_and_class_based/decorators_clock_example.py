from functools import wraps, reduce
import time


def clockit(func):

    @wraps(func)
    def wrapper(*args):
        t0 = time.time()
        result = func(*args)
        t1 = time.time() - t0
        print(f'[{t1:.8f}s]: {func.__name__}{args} -> {result}')
        return result

    return wrapper


@clockit
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


@clockit
def snooze(sec):
    time.sleep(sec)


snooze(1)
print('-' * 33)
for i in range(1, 7):
    factorial(i)
