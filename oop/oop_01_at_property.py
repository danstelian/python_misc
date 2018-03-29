"""
Implement a class named Employee
Use decorators to enforce the rules:
1. 'salary must be integer'
2. 'salary must not be 0'
"""
class Employee:

    num_of_emp = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.num_of_emp += 1

    @property  # 1
    def salary(self):
        return self.__salary

    @salary.setter  # 2
    def salary(self, value):
        assert isinstance(value, int), 'salary must be integer'
        assert value != 0, 'salary must not be 0'

        self.__salary = value
    # chance 1 & 2 with some kind of descriptor (learn descriptors)

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()


emp_1 = Employee('John', 'Smith', 1000)

print(emp_1.fullname)
emp_1.fullname = 'Tom Green'
print(emp_1.email)
