'''

class bankaccount :
    def details(self,accno,balance):
        self.accno=accno
        self.balance=balance
class savingAccount(bankaccount):
    def details(self):
         interst=self.balance*5/100
         self.balance=self.balance+interst
         print(self.accno)
         print(self.balance)
         print(interst)
class currentaccount(details)
     def deatails (self)
     self.self.balance-500
     print(self.balance)
     print(self.account)
     
b=savingaccount(1,50000)
b.details()

(c= currentaccount(2,80000)
C.details()

class emplyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class developer(emplyee):
    def developer_details(self,lang):
        print(language)
class manager(developer):
    def manage_details(self,team_size):
        self.teamsize=teamsize
class teamlead(developer,manager):
    def teamlead(self):
        if self.salary>70000:
            bounce=self.salary*10/100
        else:
            finalsalary=self.salary 

        
        print(self.name)
        print(self.salary)
        print(self.language)
        print(teamsize)

b=teamlead('manoj',70000)       


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Developer(Employee):
    def developer_details(self, language):
        self.language = language
        
class Manager(Developer):
    def manage_details(self, team_size):
        self.team_size = team_size
        
class TeamLead(Manager):
    def teamlead_details(self):
        if self.salary > 70000:
            bonus = self.salary * 10 / 100
            final_salary = self.salary + bonus
        else:
            final_salary = self.salary

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Team Size:", self.team_size)
        print("Final Salary:", final_salary)


b = TeamLead("Manoj", 70000)

b.developer_details("Python")
b.manage_details(10)
b.teamlead_details()
'''

#polymorphism :ONE ROLE MUTIPLE FUNCTION BEHAVIOURS

'''
* DUCK TYPING
* METHON OVERRIDE
* OPERATOR OVERLOADING
* METHOD OVERLOADING

DUCK TYPING = SAME METHOD DIFFERNT BEHAVIOURS

class dog:
    def sound(self):
        print('bark')
class cat:
    def sound(self):
        print('mewo')
class lion:        
     def sound(self):
        print('roar')   

d=dog()
d.sound()
c=cat()
c.sound()
l=lion()
l.sound()

OPERATOR OVERLOAD:


'''
class A:
    n=10
    def total_count(self,n):
        print(int(self.n)+int(n))


class B:
    def total_count(self,s):
        print(len(str(s)))
    
a=A()
b=B()

a.total_count(50)
print('\n')
b.total_count(50)

data encaput

data encap data hiding and dynomic binding it take the nessry action
data encaputaion process of ceating object for 


* public access sepcifiers
* private access sepcifiers
*









