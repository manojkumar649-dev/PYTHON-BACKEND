'''
package :

*to organize related python modules inside a directory(folder) .
eg :__init__.py,mark.py,student.py
labrary:

*a library contain modules and package eg:pandas,numpy

modules:
  *itertools =module
  
  functools:work with function and resuable function behour and tools

  itertools :work efficiently with iterators and sequences tools for processing value in
  sequence
  itertools:

  number=[10,20,30]
  result =iter
  
from itertools import count
for i in count(2,2):
    print(i)
    if i==24:
        break
condition sat

 
from itertools import cycle
colors=['red','green','blue']
for color in cycle(colors):
    print(color)
    if color =='blue':
        break

from itertools import permutations
leters=['a','b','c','d']
result=permutations(leters,2)
for i in result:
    print(i)

from itertools import combinations
letters=['a','b','c']
result=combinations(letters,2)
for item in result:
    print(item)
  
from itertools import permutations
name=input('enter name')
s=permutations([i for i in name])
print('all possible ways',name,'is:')
c=0
for j in s:
    c+=1
    print(j)
print('total ways',c)
       

from collections import counter

name:input('enter name:')
data = counter(name)
print('char freq dis of',name)
print(str(data))

class solution(object):
    def removeVowels(self,s):
        s=s.replace('a','*')
        s=s.replace('e','*')
        s=s.replace('i','*')
        s=s.replace('o','*')
        s=s.replace('u','*')
        return s
obj = solution()
print(obj.removeVowels(input('enter:')))
'''     
        
