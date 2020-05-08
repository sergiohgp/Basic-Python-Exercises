class Employee:

    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employee += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):

    raise_amount = 1.04

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullName())



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Developer('Test', 'User', 60000, 'java')

mgr_1 = Manager('sue', 'Smith', 90000, [emp_2, emp_1])

print(mgr_1.print_emps())



'''print(help(Developer))
print(emp_1.email)'''

'''emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)'''




