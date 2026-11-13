name='abc_abc_bac'
count={}
for i in name:
    if i in count:
        count[i] +=1
    else:
        count[i] =1
print(count)        

list =[4,21,84,12,6,24]
largest_no =list[0]

for i in list:
    if i >largest_no:
        largest_no =i

print(largest_no)


global_var = "python"

print("first", global_var)

def ft():
    global global_var
    global_var = "python django"

ft()

print("updated", global_var)
        
    
