"""
Add a @classmethod to the curent Employee class (line 48)
and a @staticmethod to the Manager subclass (line 77)
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

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        assert isinstance(value, int), 'salary must be integer'
        assert value != 0, 'salary must not be 0'

        self.__salary = value

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    # new
    @classmethod
    def get_emp_count(cls):
        return cls.num_of_emp


class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        # new
        self.employees = self.filter_emp_list(employees)

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

    # new
    @staticmethod
    def filter_emp_list(employees):
        if employees is None:
            return []
        else:
            assert isinstance(employees, list), 'employees must be a list'
            return employees[:]


emp_1 = Employee('John', 'Smith', 1000)

# not working
# mng_1 = Manager('Jim', 'Thomas', 1600, '')
# mng_1 = Manager('Jim', 'Thomas', 1600, 2)

# working
# mng_1 = Manager('Jim', 'Thomas', 1600,)
# mng_1 = Manager('Jim', 'Thomas', 1600, [])
mng_1 = Manager('Jim', 'Thomas', 1600, [emp_1])


print(Employee.get_emp_count())
