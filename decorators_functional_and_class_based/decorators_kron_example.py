# Inspired by Luciano Ramalho - Decorators and Descriptors Decoded - PyCon 2017

import time
import calendar
from datetime import datetime
import sys
import os


options = {}


def commands(func):
    option = func.__name__[0]
    options[option] = func

    def wrapper():
        return func()
    return wrapper


"""
A simpler way to write the decorator is:

def commands(func):
    option = func.__name__[0]
    options[option] = func
    return func
"""


@commands
def time_():
    print(datetime.now().time().strftime('%H:%M:%S'))


@commands
def date_():
    print(datetime.now().date().strftime('%B %d, %Y'))


@commands
def month_():
    calendar.prmonth(*time.localtime()[:2])


@commands
def year_():
    calendar.prcal(time.localtime()[0])


def main(args):
    if len(args) > 1:
        for arg in args[1:]:
            if arg in options.keys():
                options[arg]()  # calling a function stored in the dictionary
                print()
    elif len(args) == 1:
        print(os.path.abspath(__file__).split('/')[-1], list(options.keys()))


if __name__ == '__main__':
    main(sys.argv)
