"""class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
class bus(Vehicle):
    pass
school_bus = bus("school Volvo",180,12)
print("vehicle name: ",school_bus.name,"speed: ",school_bus.max_speed,"milage: ",school_bus.milage)"""

class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)
a = Employee("rahul",886012,200000,"Intern")
a.display()