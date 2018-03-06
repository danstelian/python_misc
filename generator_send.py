"""
Getting blown away by David Beazley's talk
Generators - The Final Frontier - PyCon 2014
(scratching the surface)
"""
from time import sleep


def gen_start(n):
    while n:  # countdown, n = 0 means False
        yield n
        n -= 1


def gen_send():
    while True:
        item = yield
        value = type(item)  # for example
        yield value


def gen_from(x, y):
    yield from x
    yield from y


def main():
    for x in gen_start(10):
        print(x)
        sleep(1)

    g = gen_send()
    next(g)
    print(g.send(33))
    next(g)  # do not forget
    print(g.send('spam'))

    a, b = [1, 2, 3], [4, 5, 6]
    c = (b[:] + a[:])
    c.sort(reverse=True)
    c.pop(0)
    for i in gen_from(gen_from(a, b), c):
        print(i, end=' ')


main()
