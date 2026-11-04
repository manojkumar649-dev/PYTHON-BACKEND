'''

a= ['t','u','t','o','r','i','a','l']

target= 'a'

for i in range(len(a)):
    if a[i] == target:
        print('index and value found',i)
    else:
        print('not found')
        


        
no = [2, 4, 6, 8, 10, 12, 14, 16]

def binary_no(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

result = binary_no(no, 10)

if result != -1:
    print('number found', result)
else:
    print('number not found')



arrname = 'python_python'

for i in arrname:
    print(i, arrname.count(i))


reverse ='manoj'

reverse_name=reverse[::-1]
print(reverse_name)


a= 10
b=20

a,b=b,a
print(a,b)

'''

name = 'madam'
reverse = name[::-1]
if name == reverse:
    print('Yes')
else:
    print('No')


text = 'python'
reversed_text = ''

for char in text:
    reversed_text = char + reversed_text  # Adds each new character to the front

print(reversed_text)


    
    
















    
    
        
    





