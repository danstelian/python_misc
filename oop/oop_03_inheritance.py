"""
Add two subclasses to the curent Employee class
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


class Developer(Employee):

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}('{self.first}', '{self.last}', {self.salary}, '{self.prog_lang}')"


class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)

        if employees is None:
            self.employees = []
        else:
            # should assert if every employee in the list is instance of class Employee...
            assert isinstance(employees, list), 'employees must be a list'
            self.employees = employees[:]

    def add_emp(self, new_emp):
        if new_emp not in self.employees:
            self.employees.append(new_emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        if not self.employees:
            print('empty list')
        else:
            print('-->', end='')
            for emp in self.employees:
                print(f'\t{emp.fullname}')


emp_1 = Employee('John', 'Smith', 1000)
print(emp_1)

# dev_1 = Developer('Tom', 'Green', 0, 'Python')  # still getting error messages
dev_1 = Developer('Tom', 'Green', 1200, 'Python')
print(repr(dev_1))  # rewrote the __repr__ sepecial method to accommodate the 'prog_lang' attribute

mng_1 = Manager('Jim', 'Thomas', 1600, [emp_1])
# mng_1 = Manager('Jim', 'Thomas', 1600, [])
# mng_1 = Manager('Jim', 'Thomas', 1600)
print(mng_1)
# mng_1.add_emp(emp_1)
mng_1.add_emp(dev_1)
mng_1.print_emp()
