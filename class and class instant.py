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
print(Employee.no_of_employee)
asad=Employee("Muhammad","Asad",44000)
print(Employee.no_of_employee)
ali=Employee("Muhammad","Ali",44000)
print(Employee.no_of_employee)
# print(ali.salary)
# asad.increase()
# ali.increase()
# print(ali.salary)



