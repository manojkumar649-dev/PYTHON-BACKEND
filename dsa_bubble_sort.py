#bubble sort
'''
numbers =[22,10,14,13,6,17]
n=len(numbers)
for i in range(n-1):
  for j in range(n-i-1):
     if numbers[j] > numbers[j+1]:
         numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)

'''

numbers =[25000,18000,23000,13000,27000]
n=len(numbers)
for i in range(n-1):
  for j in range(n-i-1):
     if numbers[j] > numbers[j+1]:
         numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)



     
