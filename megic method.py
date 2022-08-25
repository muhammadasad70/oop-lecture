class Employee:
    increment =1.3
    no_of_employee=0

    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary =salary
        self.increment=1.5
        Employee.no_of_employee+=1
    def increase(self):
        self.salary = int(self.salary * Employee.increment)
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
    @staticmethod
    def is_open(day):
        if day=='sunday':
            return 'office is open'
        else:
            return 'office is closed'
    def __add__(self, other):
        return self.salary+other.salary
    def __repr__(self):
        return 'The name of' ' Employee ({}, {},{})'.format(self.fname,self.lname,self.salary)
jacktion=Employee("joan",'alia',99000)
amna=Employee("amna",'ali', 10000)
# print(jacktion.increase())
print(repr(amna))