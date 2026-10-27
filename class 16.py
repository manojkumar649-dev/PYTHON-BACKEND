'''

file handiling

open()method
close()method
accessing nodes for creating the file ,modifying and deleting

x
w
r

fp=open('dummy.txt','x')
fp.close()

fp=open('dummy.txt','w')
fp.write('first code')
fp.close()

fp=open('newfile.txt',r)
print('filename',fp.name)
print('filemode',fp.mode)
print('closefile',fp.closed)
fp.close()
print('is closed',fp.closed)


file=open('newfile.txt','x')
file.close()
fp=open('newfile.txt','w')
fp.write('addgftyryutygj')
fp.close()

fp=open('newfile.txt','r')
print('filename',fp.name)
print('filemode',fp.mode)
print('closefile',fp.closed)
fp.close()
print('is closed',fp.closed)
file=open('newfile.txt','x')
file.close()

import os
print(os.path.isfile('newfile.txt'))

with open(r'D:/BACKENT PYTHON/class16.py) 


try:
    fp=open("newfile.txt","r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
        print("please cheak")

fp=open("newfile.txt","a")
fp.write("\n new line the content")
fp.close()

fp=open("newfile.txt","r")
print(fp.read())
fp.close()

import os
cwd=os.getcwd()
print(f"Directory Content:{cwd}")

files =os.listdir(".")
print(f"Directory Content :{files}")

import os
os.makedirs('D:/BACKEND PYTHON)
'''

import random
num2 =random.randrange(100,500)
print(num2)

import random

for i in range(5):
    print(random.randint(10,30),end="-")
    
import random
print(random.sample([10,20,30,40],2))
          


















