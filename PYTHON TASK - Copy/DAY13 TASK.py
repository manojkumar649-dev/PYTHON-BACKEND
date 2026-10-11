#TASK 1
'''
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def display_electronic(self):
        self.display_product()
        print('Warranty', self.warranty, 'years')

class ClothingProduct(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def display_clothing(self):
        self.display_product()
        print("Size:", self.size)
laptop = ElectronicProduct('Laptop', 500233, 2, 2)
laptop.display_electronic()
print()
shirt = ClothingProduct('Shirt', 600, 5, 'XL')
shirt.display_clothing()

'''
TASK 2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)
        print("Course:", self.course)

class CollegeStudent(Student):
    def __init__(self, name, age, student_id, course, college_name, academic_year):
        super().__init__(name, age, student_id, course)
        self.college_name = college_name
        self.academic_year = academic_year

    def display_college_student(self):
        self.display_student()
        print("College:", self.college_name)
        print("Academic Year:", self.academic_year)

student = CollegeStudent("Manoj", 21,"ST101","B.Sc Computer Science","ABC College",3)
student.display_college_student()
'''
