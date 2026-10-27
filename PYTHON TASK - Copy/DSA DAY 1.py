'''
DSA

AN ARRAY IS A DATA STUCTURE USED TO STORE MULTIPLE ELEMENTS IN AN
ORGANIZED WAY

EACH ELEMENTS HAS AN INDEX THAT IDENTIFIES ITS POSITION

*ARRAY OPERATION ARE:

NUM =[10,20,30,40]
PRINT(NUMBERS[0])=ACCESSING VALUE
NUM[0]= 100 =UPDATE THE VALUE

NUM.APPEND(600)=ADD VALUE AT THE END

NUM.INSERT(1,15)=INSERT THE VALUE IN FIRST INDEX

NUM.REMOVE(30)=REMOVE THE VALUE

PRINT(LEN(NUMBERS))=LEN OF NOS

TRAVERSING THE LOOP ENTER ALL THE CURRENT ELEMENTS AND MOVES


number=[25,30,60,40,35]
largest =number[0]
for i in number:
    if i>largest:
        largest=i
print(largest)



def liner_search(number,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i,numbers[i]
        return -1
numbers =[10,20,30,40]
target = 45
index,value =linear_search(numbers,target)
def linear_search(numbers, target):
    indexes =[]

    for i in range(len(numbers)):
        if numbers[i] == target:
            indexes.append(i)

    return indexes

print(linear_search([10,20,30,30,20,40],30))
'''

def linear_search(numbers):
    for num in numbers:
        if num > 50:
            return num
        
    return None
        
print(linear_search([10,20,30,40,60]))



def linear_search(array_list):
       largest=array_list[0]
       for num in array_list:
            if num < largest:
               largest=num
       return num    
print(linear_search([10,20,60,30,40,70]))        
'''        
binary search
means it should have sorted array.
finds an elements by repeately divive a sorted list into
two half

l=0
m=24
h=62

why we do use binary search
time consumption
o(logn)
sorting
binary search
works : divides the array into two halves
number =[10,20,30,40,50,60,70]
target =60
low = 0

high len(numbers)

while low <= high:
    mid = (low + high)//2
    if numbers[mid] == target:
        print("Element found at index:",mid)
        break

    elfi target > numbers[mid]:
        low = mid+

























        
    
