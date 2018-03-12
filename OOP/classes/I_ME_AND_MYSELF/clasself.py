class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
emp_1 = Employee('Masinde', 'Masinde', 4000)
emp_2 = Employee('Masinde', 'Mtesigwa', 14000)

emp_1.fullname()
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
print(emp_1.email)
print(emp_2.email)
