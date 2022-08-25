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
class Programmer(Employee):
    def __init__(self,fname,lname,salary,language,experience):
        super().__init__(fname,lname,salary)
        self.language = language
        self.experience = experience
    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2))
        return self.salary

jacktion=Programmer("joan",'alia',99000 ,'python','4 years')
amna=Programmer("amna",'ali', 100000 ,'java','3 years')
print(jacktion.increase())
# print(amna.fname,amna.lname,amna.salary,amna.language,amna.experience)




# print(Employee.no_of_employee)
# asad=Employee("Muhammad","Asad",44000)
# # print(Employee.no_of_employee)
# ali=Employee("Muhammad","Ali",44000)
# # print(Employee.no_of_employee)
# Employee.change_increment(5 )
# asad.increase()
# # print(asad.salary)
# print(Employee.is_open('sunday'))
jacktion=Employee("joan",'alia','99000')
amna=Employee("amna",'ali','10000')
print()