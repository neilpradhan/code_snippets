
class Employee:
    raise_amt = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
#         class variables can only be applied throgh instance of the object or class itself
        self.pay = self.pay * self.raise_amt

        
print("number_of_employees_before",Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print("number_of_employees_after",Employee.num_of_emps)
emp_1.raise_amt = 5
print(emp_1.raise_amt)
print(Employee.raise_amt)


print(emp_1.__dict__)
print(Employee.__dict__)

