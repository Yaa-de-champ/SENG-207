# Exception Handling
age = 8
try:
    print(age)
except:
    print('Error: Variable not defined')


import sys
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
try:
    result = number1/number2 #not a global variable 
except ZeroDivisionError:
    print('Error: Cannot divide by zero')
    sys.exit(1)
finally: #executes whether there was an error or not 
    print('Code executed successfully')
print(f'Division: {result}')


# Environment Variables


# Virtual Environment in Python
