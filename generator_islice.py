from itertools import islice, count


# generate fibonacci sequence
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(islice(fib(), 0, 10)))
print(list(islice(fib(), 5, 11)))


# generate prime numbers
def gen_primes():
    found_primes = set()
    for num in count(2):
        if not any(num % i == 0 for i in found_primes):
            found_primes.add(num)
            yield num


print(list(islice(gen_primes(), 0, 10)))
