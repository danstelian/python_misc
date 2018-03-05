"""
Module documentation
The iterator protocol explained (also playing with classes)
Generators - Powering Iteration in Python - Luciano Ramalho
"""


class Train:
    def __init__(self, cars):
        self.cars = cars

    def __iter__(self):
        return TrainIterator(self.cars)


class TrainIterator:
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


main()
