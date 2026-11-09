
'''

names= ["arun","priya","rahul","kumar"]
target="rahul"
found=False

for i in names:
    if i==target:
      found=True
      break

if found:
    print("YES FOUND RAHUL")
else:
    print("NO NOT FOUND")        



list=[10, 20, 10, 30, 10, 40]
target=10
count= 0

for i in list:
    if i == target:
        count = count+1

print(count)  

'''
numbers= [5, 10, 15, 20, 25]
target=50
found=False

for i in numbers:
    if i==target:
      found=True
      break

if found:
    print("YES FOUND ")
else:
    print("NO NOT FOUND")  