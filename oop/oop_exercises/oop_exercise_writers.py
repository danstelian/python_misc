"""
Write two subclasses 'LogWriter' and 'CSVWriter'
that inherit from an abstract base class 'Writer'
"""
from datetime import datetime
import abc
import os


class Writer(metaclass=abc.ABCMeta):

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def openfile(self):
        return open(self.filename, 'a')

    def closefile(self):
        self.f.close()

    def writeline(self, line):
        self.f = self.openfile()
        self.f.write(line + '\n')
        self.closefile()

    @abc.abstractmethod
    def write(self, text):
        return


class LogWriter(Writer):

    def write(self, text):
        self.writeline(f'{self.log()}\t{text}')

    @staticmethod
    def log():
        return datetime.now().strftime('%Y.%m.%d @%H:%M:%S')


class CSVWriter(Writer):

    def __init__(self, filename, delimiter=','):
        super().__init__(filename)
        self.delimiter = delimiter

    def write(self, text):
        self.writeline(self.format(text))

    def format(self, text):
        result = [f'\"{arg}\"' if self.delimiter in arg else arg for arg in text]
        return self.delimiter.join(result)


name = os.path.splitext(os.path.abspath(__file__).split('/')[-1])[0]
logname = name + '_log.txt'
csvname = name + '_file.csv'

alog = LogWriter(logname)

alog.write('This is a line')
alog.write('This is another line')


bcsv = CSVWriter(csvname)

bcsv.write(['a', 'b,2', 'c', 'd'])
bcsv.write(['1', '2', '3', '4'])
