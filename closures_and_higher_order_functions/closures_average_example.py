"""
def Averager:
    def __init__(self):
        seq = []
    def __call__(self, new):
        self.seq.append(new)
        return sum(self.seq) / len(self.seq)
"""


def make_averager():
    # this is where the closure starts - it includes the free variable / lexical scope
    seq = []  # free variable

    def averager(new):
        # nonlocal seq
        # seq += [new]
        seq.append(new)
        return sum(seq) / len(seq)
    # this is where the closure ends

    return averager


avg = make_averager()

print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0
print()

print(avg.__name__)
print(avg.__code__.co_name)
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)  # the names of the free variables
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)  # we can inspect the content of the free variable
print('-' * 50)


# different implementation of averager()
def make_averager():
    count = 0
    total = 0

    def averager(new):
        nonlocal total, count
        total += new
        count += 1
        return total / count

    return averager


new_avg = make_averager()
print(new_avg(10))  # 10.0
print(new_avg(11))  # 10.5
print(new_avg(12))  # 11.0
