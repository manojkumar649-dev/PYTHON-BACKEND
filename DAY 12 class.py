'''

class Transport:
    landtrans='bus'
    def __init__(s,person,price):
        s.person=person
        s.price=price
    def display(s):
        print('person type',s.person)
        print('price',s.price)
obj1=Transport('kids',1000)
obj1.display()
obj2=Transport('adult',2000)
obj2.display()
print(obj2.landtrans)
'''

class student:
    def __init__(s,name,course):
        s.name=name
        s.course= course
    def show(s):
        print('name',s.name)
        print('price',s.course)
class placement(student):
    def __init__(s,name,course,company):
        super().__init__(s.name,course)
        s.company=company
    def show_place(s):
        print(s.company)
class placement_age(placement):
    def __init__(s,name,course,company):
        super().__init__(s,name,course,company,age)
        s.age=age
    def show_place(s):
        print(s.company)        

        
        
obj1=placement('manoj','python','zoho')
obj1.show_place()


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def show(self):
        print("Name:", self.name)
        print("Course:", self.course)
class Placement(Student):
    def __init__(self, name, course, company):
        super().__init__(name, course)
        self.company = company
    def show_place(self):
        print("Company:", self.company)

class Placement_Age(Placement):
    def __init__(self, name, course, company, age):
        super().__init__(name, course, company)
        self.age = age

    def show_age(self):
        print("Age:", self.age)

obj1 = Placement_Age(" Manoj ", "Python", "Zoho", 22)
obj1.show()
obj1.show_place()
obj1.show_age()

'''
class student :
    def __inti__(self,name,course):
        self.name= name
        self.course=course
    def show(self):
        print('name',self.name)
        print('course',self.course)
        

        






        

        











