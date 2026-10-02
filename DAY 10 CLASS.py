'''
#CONSTRUCTOR
#TYPES


#with perameter:

class Employee:
    course='python'#class veriable
    def __init__(s,name,age):#INSTANCE VARIABLE
        s.name=name
        s.age=age
    def display(s):#instance method
        print(s.name)
        print(s.age)
obj1=Employee('mano',24)
obj1.display()
print(obj1.course)
obj2=Employee('madhan',49)
obj2.display()
print(obj2.'java')


#NON PERAMETERISE:


class car:
    def __init__(self):
        self.carname='bmw'
        self.carprice=2000000
    def display(self):
        print(self.carname)
        print(self.carprice)
car1=car()
car1.display()

class school:
    schoolname='sla'
    def __init__(self,sname,city='chennai'):
        self.sname=sname
        self.section='b'
    def display(self):
        print(self.sname)
        print(self.section)
obj1=school('mano')
obj1.display()

 #inheritance:
    the child class can able to access properties and behaviours
    behaviours of pranter class
    parent class /base class
    childclass derived class

single inheritance
multiple inheritance
multilevel inheritance
hierarical inheritance
hybrid

class emplyee:
     def show_employee_

