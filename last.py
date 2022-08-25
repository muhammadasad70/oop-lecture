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
    @property
    def email(self):
        return self.fname+self.lname+'@gmail.com'
    @staticmethod
    def is_open(day):
        if day=='sunday':
            return 'office is open'
        else:
            return 'office is closed'
if __name__ == '__main__':
    jacktion = Employee("joan", 'alia', 99000)
    amna = Employee("amna", 'ali', 10000)
    print(amna.email,':', jacktion.email)
    amna.lname= 'ijaz'
    print(amna.email,':', jacktion.email)