"""
Inspired by Luciano Ramalho (Decoretors and Descriptors Decoded)
and David Beazley (The Fun of Reinvention)
"""


class Contract:

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    def __set_name__(self, cls, name):
        self.name = name

    def check(self, value):
        pass


class PositiveInteger(Contract):

    def check(self, value):
        assert isinstance(value, int), f'{self.field_name} must be an integer'
        assert value > 0, f'{self.field_name} must be positive'
        self.field_name = value


class NonemptyString(Contract):

    def check(self, value):
        assert isinstance(value, str), f'{self.field_name} must be a string'
        assert len(value) > 0, f'{self.field_name} must not be empty'
        self.field_name = value


def set_attr(cls):
    for name, attr in cls.__dict__.items():
        if issubclass(attr.__class__, Contract):
            attr.field_name = name
    return cls


@set_attr
class Employee(Contract):

    name = NonemptyString()
    email = NonemptyString()

    salary = PositiveInteger()

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    @property
    def full_email(self):
        return f'{self.name} <{self.email}>'


c = Employee('Dan', 'dan@company.com', 1000)
print(c.full_email)
