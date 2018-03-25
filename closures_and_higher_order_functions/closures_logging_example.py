import logging


logging.basicConfig(filename='closures_example.log', level=logging.INFO)


def logger(func):

    def logging_func(*args):
        logging.info(f'Running {func.__name__}{args}')
        return func(*args)

    return logging_func


def mul(x, y):
    return x * y


mul = logger(mul)
print(mul(2, 3))


# or using decorators
@logger
def add(x, y):
    return x + y


print(add(2, 3))
