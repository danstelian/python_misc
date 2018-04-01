"""
Write a class named Employee
Use NonType descriptor class to enforce the rules:
1. 'first_name and last_name must be of type string'
2. 'first_name and last_name must not be empty'
"""


class NonType:

    def __init__(self, field_name):
        self.field_name = field_name

    def __set__(self, instance, value):
        assert isinstance(value, str), f'{self.field_name} must be a string'
        assert len(value) != 0, f'{self.field_name} must not be empty'
        instance.__dict__[self.field_name] = value


class Employee:

    first_name = NonType('first_name')
    last_name = NonType('last_name')

    # in the next part use the syntax:
    # first_name = NonType()
    # last_name = NonType()

    num_of_emp = 0

    def __init__(self, first, last, salary=0):
        self.first_name = first
        self.last_name = last
        self._salary = salary

        Employee.num_of_emp += 1

    @property
    def salary(self):
        return self._salary

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@company.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split()

    def __str__(self):
        return f'{self.first_name} {self.last_name} [{self.email}]'


emp_1 = Employee('John', 'Smith', 1000)

print(emp_1)
