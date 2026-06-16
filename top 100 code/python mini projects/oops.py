'''
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod        # class method not instance method like others
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('mohana', 'sruthy', 50000)
emp_2 = Employee('test','user',60000)
'''



'''
import datetime
import time

my_date = datetime.date(2016, 7, 11)
print(Employee.is_work_day(my_date))
'''
'''
# emp_1.set_raise_amount(1.05) # used class method from instance
Employee.set_raise_amount(1.05) # used class method from instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


emp_str_1 = "mohana-sruthy-50000"
emp_str_2 = "steve-smith-70000"
emp_str_3 = "jane-doe-90000"

new_emp_1 = Employee.from_string(emp_str_3)
print(new_emp_1.email)
'''



'''
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):

    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first,last,pay)
        self.prog_lan = prog_lan

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
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
            print('-->', emp.fullname())


dev_1 = Developer('mohana', 'sruthy', 50000, 'Python')
dev_2 = Developer('test','user',60000, 'Java')

mgr_1 = Manager('Sue','smith',90000,[dev_1])

print(f"is instance : {isinstance(mgr_1, Manager)}")
print(f"is subclass : {issubclass(Manager, Developer)}")



print(dev_1.email)
print(dev_1.prog_lan)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
'''


'''
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('mohana', 'sruthy', 50000)
emp_2 = Employee('test','user',60000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

print(emp_1 + emp_2)

print(len(emp_2))
'''








class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@gamil.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee('Jhon', 'Smith')

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname

print(emp_1.fullname)