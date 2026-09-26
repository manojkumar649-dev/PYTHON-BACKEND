
'''
even = 0
odd = 0
for i in range(0,10,20):
    if i %2==0:
         even =even+1
        print(i)



for i in range(0,10+1):
    print(i)
  
for i in range(0,11):
    if i %2==0:
        print(i,'even')
    else:
            print(i,'odd')

        
for i in range(0,10):
    if i >4:
        break
    print(i)
        

for i in range(1,21):
    print('0'*i)

for i in range(1,6):
    for j in range(0,i):
        print(i,end='*')
    print()
    
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end='*')
    print()
    
'''

for i in range(0,6):
    for j in range(i,6):
        print(i,end='*')
    print()  
