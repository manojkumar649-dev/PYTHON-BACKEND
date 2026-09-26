
'''
price_amount=int(input('enter price'))

if price_amount>=99:
    print(price_amount,'free delivery')
else :
    print('price',price_amount ,'shiping charge 40', 'total',price_amount+40)


'''

balance =1000

print(1,'withdraw')
print(2,'deposite')
print(3,'cheak balance')
option = int (input('enter your option'))
if option ==1:
    withdraw=int(input('enter withdraw amount'))
    print(withdraw-balance,'balance')
elif option ==2:
    deposite=int (input('enter deposite amount'))
    print(balance+deposite,'current balance')
elif option ==3:
    print(balance,'current balance')
else:
    print('no option here')
    
    
    
