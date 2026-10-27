'''

try:
    value = input("Enter a number: ")
    number = int(value)
    print("Integer value:", number)

except ValueError:
    print("Error: Please enter a valid integer.")


TASK 2

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers")

else:
    print("Result:", result)
    print("Division completed successfully")

finally:
    print("Program execution completed.")


TASK 3
'''
try:
    total_price = float(input("Enter the total price: "))
    quantity = int(input("Enter the quantity: "))

    price_per_item = total_price / quantity

    print("Price per item:", price_per_item)


except ZeroDivisionError:
    print("Error: Quantity cannot be zero.")

except ValueError:
    print("Error: Please enter valid numbers.")






    
