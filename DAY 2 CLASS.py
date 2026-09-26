'''
age = int(input('enter your age'))
if age>=18:
     print('ok')
     
actual_price=int(input('enter your amount'))
if actual_price>10000:
    if actual_price >=10000:
    discount=actual_price*20/100
    amount=actual_price
    print('the discout value',discount)
    print('the amount is ',amount)
    else:
        discount=actual_price*10/100
        amount=actual_price-discount
        print('the discount value is',discount)
        print('the amount is',amount)
 else:
     print('plz pay the actual_amount') 
    
          '''
number_of_unit=int(input('number of unit'))
if number_of_unit >=9000:
     price=125*number_of_unit
     print('totalp price',price)
     
