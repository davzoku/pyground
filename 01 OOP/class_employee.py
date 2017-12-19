# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# lesson 1 : Class and Instance
## lesson 2: Class Variables
### lesson 3: classmethods, staticmethods
#### lesson 4: Inheritance & subclasses
#####
###### lesson 6
import datetime

class Employee:
    ## create class variables
    raise_percent = 1.1
    # create constructor
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    #create method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raisepay(self):
        self.pay = self.pay * self.raise_percent
        return self.pay
    ###create classmethod that calls on a class
    @classmethod
    def set_raise_percent(cls, amount):
        cls.raise_percent = amount
    ###classmethod as alternative constructors to do repeative parse
    @classmethod
    def from_string(cls, e_str):
        first, last, pay = e_str.split('-')
        # split string separated by -
        return cls(first,last,pay)
    ####staticmethod dont operate on class or instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
        # mon = 0 ... sun = 6
            return False
            #caps False

#### create 2 subclasses

class Manager(Employee):
    def __init__(self,first,last,pay,employees= None):
        super().__init__(first, last,pay)
        #none to avoid mutable data types
        self.employees = employees
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('>>', emp.fullname())

class Developer(Employee):
    def __init__(self,first,last,pay,proglang):
        super().__init(first, last,pay)
        #let Employee class handle the attributes
        self.proglang = proglang

#print (help(Developer))


#Create 2 instances with 3 attributes
e1 = Employee('Tom1', 'Harry', 5)
e2 = Employee('Jon2', 'Wick', 55)

#print(e1.fullname())
print('Employee 1:')
print(Employee.fullname(e1))
print('Pay before raise:', e1.pay)
e1.raisepay()
print('Raise %:', e1.raise_percent)
print('Pay after raise:', e1.pay)
print(e1.email+ '\n')


print('Employee 2:')
print(Employee.fullname(e2))
print('Pay before raise:', e2.pay)
e2.raise_percent= 2
e2.raisepay()
print('Raise %:', e2.raise_percent)
print('Pay after raise:', e2.pay)
print(e2.email+ '\n')

Employee.set_raise_percent(10)

print(Employee.raise_percent)
e1.raisepay()
print('Tom1\'s new pay:', e1.pay)

### suppose employee list is this

e_str_1 = 'Harry3-Osborn-100'
e3 = Employee.from_string(e_str_1)

print('Employee 3:')
print (Employee.fullname(e3))


testdate =datetime.date(2017,12,16)

print(Employee.is_workday(testdate))


mgr1 = Manager('Frank', 'Castle', 1000, [e1, e2])

print('Manager 1:', Manager.fullname(mgr1))
mgr1.print_emps()

#mgr1.add_emp(e3)
#mgr1.remove_emp(e1)

print('Manager 1:', Manager.fullname(mgr1))
mgr1.print_emps()