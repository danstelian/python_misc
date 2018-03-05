"""
Module documentation
The iterator protocol explained (also playing with classes)
Generators - Powering Iteration in Python - Luciano Ramalho
"""


class Train:
    def __init__(self, cars):
        self.cars = cars

    # def __iter__(self):
    #     return TrainIterator(self.cars)
    # obsolete

    def __iter__(self):
        for index in range(self.cars):
            yield f'car {index}'


class TrainIterator:  # unused
    def __init__(self, cars):
        self.next = 0
        self.last = cars - 1

    def __next__(self):  # rewrite this to start with 0? is that a thing?
        if self.next <= self.last:
            self.next += 1
            return f'car {self.next}'
        else:
            raise StopIteration()

    def __iter__(self):
        return self


def main():
    t = Train(5)
    for car in t:
        print(car)

    print('\n###################\n')

    t2 = Train(5)  # t2 is an iterable
    # automatically done by 'for'
    t2_iter = iter(t2)  # t2_iter is an iterator
    # iterable - an object from which the iter() function (or the .__iter__ method) can build an iterator
    print(next(t2_iter))
    print(next(t2_iter))
    ...  # until StopIteration exception


main()
