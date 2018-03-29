"""
Add two special methods to the Employee class
__str__ and __repr__
"""
class Employee:

    num_of_emp = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.num_of_emp += 1

    def __str__(self):
        return f'{self.first} {self.last} [{self.email}]'

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}('{self.first}', '{self.last}', {self.salary})"

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
print(emp_1)

emp_2 = eval(repr(emp_1))
emp_2.fullname = 'Tom Green'
print(emp_2)
print(Employee.num_of_emp)
