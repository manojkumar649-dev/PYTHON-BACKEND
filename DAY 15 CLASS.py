'''DATA APSTACTION :
WE USE APSTARCTMETHOD

from abc import ABC, abstractmethod

class payment (ABC):

     @abstractmethod
     def pay (self):
      pass
class creditcard(payment):

       def pay(self):
           print('payment made using credit card')

class upi(payment):
      #the child provide the actual implementataion.
      #how it is done
      def pay (self ):
         print ('payment')
class cash(payment):

      def pay (self):
         print('pay cash')
         
card= creditcard()
upi=upi()
cash=cash()
card.pay()
upi.pay()
cash.pay()


from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
     print('bark')
class cat(animal):
    def sound(self):
     print('mewo')

     
dog=dog()
cat=cat()
dog.sound()
cat.sound()


        
ERROR AND EXCEPTIONS
ERROR MEANS IS RECOGNIZED AS A MISBEHAVED PART WIYHIN AS SOURCE
CODE.
*ERROR CAN DETECTED AND FOUND BY PARSER (INTERPRETER)
WHEN IT DETECTS THE INCORRECT STATEMENT.
INCORRECT STATEMENT IF THE GIVEN STATEMNT OR CONDITION IS NOT
SUFFICIENT.

ERROR:
    *SYNTAX ERROR-OCCURS WHEN PARSER DETECTS THE ERROR.
    *RUNTIME ERROR-MANY REASONS

EXCEPTION

Exception MEANS AN UNWANTED OR UNEXCEPTED EVENT THAT
DISTRUPTS THE NORMAL FLOW OF PROGRAM EXECTION
EXAMPLE
*USER HAS GIVEN INVALID DATA.
*PIN NO MISTAKE.


will work this exception with the help of exception handlers
'''
try:
    5/0
except:
    print('ZeroDivisionError: division by zero')
finally:
    print('rrrr')

    


      
     
