"""
Working with abstract base classes (abc)
An abstract class defines an interface that must be implemented by its subclass
(this is absolutely awesome)
"""
import abc


class AbstractEmployee(metaclass=abc.ABCMeta):
    # one way to create an abstract base class is to use a metaclass

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.job = ''

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    # the next three methods will be mandatory (to implement) in the subclass that inherits from AbstractEmployee
    @abc.abstractmethod
    def get_fullname(self):
        return

    @abc.abstractmethod
    def set_job(self, job):
        return

    @abc.abstractmethod
    def get_job(self, job):
        return


class Developer(AbstractEmployee):

    def get_fullname(self):
        return f'{self.first} {self.last}'

    def set_job(self, job):
        self.job = job

    def get_job(self):
        return self.job


# An abstract class is not designed to construct instances
# emp_1 = AbstractEmployee('John', 'Smith', 800)
# TypeError: Can't instantiate abstract class AbstractEmployee with abstract methods get_fullname, get_job, set_job


dev_1 = Developer('John', 'Smith', 800)
dev_1.set_job('Python Developer')
print('{0} is a {1}.'.format(dev_1.get_fullname(), dev_1.get_job()))
