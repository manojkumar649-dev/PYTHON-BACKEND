'''

#MULTITHREADING
#THREAD:A SMALL UNIT OF EXECTIO  INSIDE A PROGRAMM
#MUTITHREADING CONCEPT
#THREAD,THREDING
EG:
   * MEMORY SPACE WILL BR MORE
   * LIGHT WEIGHT
   * 10TYPES OF FLOWER:THREADING
   * IT  ALLOWS MULTIPLE THREAD TO MAKE PROGRESS WITH IN A SINGLE
     PROCESS.
   * INSTEAD OF MAKING EACH TASK WAIT UNNECESSARILY FOR ANOTHER
   * A PROGRAM CA  MAKE MULITE THREAD TO MANGE TASK CONCURRENTLY

import time
def task1():
    print('task1 started')
    time.sleep(3)
    print('task2 completed')
def task2 ():
    print('task2 completed')
    time.sleep(3)
    print('task2 completed')

task1()
task2()
print('all task compledted')

import threading
import time
def task1():
    print('task1 started')
    time.sleep(3)
    print('task2 completed')
def task2 ():
    print('task2 completed')
    time.sleep(3)
    print('task2 completed')

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

t1.join()
t2.join()

import threading
import time
def task1():
    print('find a song')
    time.sleep(3)
    print('downloadfile')
def task2 ():
    print('play a song')
    time.sleep(3)
    print('sent an email')

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

t1.join()
t2.join()
'''
import threading
import time
def task1():
    print('goodmrng')
    time.sleep(5)
    print('good afternoon')
    time.sleep(5)
    print('good evenig')
    time.sleep(5)
    print('ended')

t1=threading.Thread(target=task1)
t1.start()
t1.join()


import threading
import time
def task1(goodmrng,goodafter):
    print('goodmrng')
    time.sleep(5)
    print('good afternoon')
    time.sleep(5)
    print('good evenig')
    time.sleep(5)
    print('ended')

t1=threading.Thread(target=task1)
t1.start()
t1.join()








