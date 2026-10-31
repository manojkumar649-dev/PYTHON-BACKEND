
'''
num=7

if num%2 == 0:
    print("it even")
else:
    print("its odd")   


list=[-1,3,-2,5]
pos = 0
neg = 0
for i in list:
    if i > 0:
        pos=i
        print("positive number" ,pos)
    elif i < 0:
        neg = i
        print("negative number",neg)    


list = [10,30,20,40,21]
largest=list[0]
for i in list:
    if i > largest:
        largest = i
        
print(largest)

a=10
b=20
a,b=b,a
print(a,b)

year = 2024
if (year % 4 == 0 and year % 100 != 0):
    print("leapyear")
else:
    print("no leapyear")    
'''

num=10
count= 0
for i in range(1,num+1):
    count=count+i
    print(count)




