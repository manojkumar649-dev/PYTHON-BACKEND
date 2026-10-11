'''

self :self keyword to access or modify the the instance variable .
class student :

class variable :is a variable that is declared inside of a class
but outside of any instance method or __inti__()method .

class sla :
    class variable = 'inst'
    def show (self .name.city)

    
#modify the class variable .
class student :
class _var='abc'
def __inti__(self,name,city )
self.name=name
self .city=city
def show (self.name)
print(self .name)
print (self.city)

s=student('jaya','blr')
s.show()
print('before',student.class_var)#
#classname.variable =value
student.class_var='xzy'

#class method used to access or modify the class state
@classmethod decorator
classmethod ()function

cls is recemmond
class Student:
    schoolname = 'anna adarsh'

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @classmethod
    def change_method(cls, schoolname):
        cls.schoolname = schoolname

    def show(self):
        print(self.name, self.city, Student.schoolname)

s = Student('jayasree', 'ihr')
s.show()
Student.change_method('jbas')
s.show()
s1 = Student('jaya', 'cig')

#data encapsulation:
    public ,private and protected access specifiers:
        bank account -class
        public accesss specifiers
        
        
  

class bankaccount :
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accon
        self.balance=balance
    def show_details(self):
        #member function
        print('name',self.accno)
        print('accno',self.accno)
        print('balance',self,balance)

account =bankaccount ('thiru',456789,577777)
print(account.name)#accessing variable outside of class

private assces secifiers:
    we connot accces private member outside of a class
    if we want to access it we required a permission(name mangling)

    __ duble underscore

    e.show ()#inside the class im accessing private access specifier
    print(e.Emplyee__salary )# name mangling

    
protected access specifiers:

we cant access it form inside of the class
and from outside of the class .
    
    class bank_account:
        self.name=name #public
        self._
    

class BankAccount:
    def __init__(self, name, password, balance):
        self.name = name
        self._password = password
        self.__balance = balance

    def login(self, password):
        if password == self._password:
            print("Login successful")
            return True
        else:
            print("Login unsuccessful")
            return False
        
    def show_balance(self, password):
        if password == self._password:
            print("Current balance:", self.__balance)
        else:
            print("Wrong password")
account = BankAccount("Manoj", "1234", 50000000)

print(account.name)
account.login("1234")
account.show_balance("1234")


#protected is single_underscore - ' _  '
#privete is duble underscore -  ' __  '


its an online shoping system name can be public and password prive 

'''

class customer:
    def __init__(self,name,password,loginstatus):
        self.name=name
        self._password =password
        self.__loginstatus=loginstatus
    def login(self,password):
        if password == self._password:
            print ('login successful')
            return True
        else:
            print('login unsuccessful')
            return False
    def show_loginstatus(self,password):
        if password == self._password:
            print('loginstatus ',self.__loginstatus)
        else:
            print('wrongpassword')
login1= customer('manoj','0000',5000000)
print(login1.name)
login1.login('0000')
login1.show_loginstatus('0000')
            
                




        
        











