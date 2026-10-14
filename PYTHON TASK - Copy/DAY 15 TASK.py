'''

from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def salaryDetails(self):
        pass
class fulltimeEmp(employee):
    def salaryDetails(self):
        salary=30000
        print('fulltime',salary)
class partTime(employee):
    def salaryDetails(self):
        salary =10000
        print('partTime',salary)
obj =fulltimeEmp()
obj1 =partTime()
obj.salaryDetails()
obj1.salaryDetails()
'''
from abc import ABC,abstractmethod

class appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class washingMechine(appliance):
    def turn_on(self):
        washingMechine_on="ON"
        print("washingMechine",washingMechine_on)
class refrigerator(appliance):
    def turn_on(self):
        refrigerator_on="ON"
        print("refrigerator",refrigerator_on)
class AirConditioner(appliance):
    def turn_on(self):
        AirConditioner="ON"
        print("AirConditioner",AirConditioner)
        
obj1=washingMechine()
obj1.turn_on()
obj2=refrigerator()
obj2.turn_on()
obj3=AirConditioner()
obj3.turn_on()




    
        
        
