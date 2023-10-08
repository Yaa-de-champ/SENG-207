# A function is a block of reusable code 
# Place a parenthesis() in front of the function name to call / invoke it

# Parameters vs Argument
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Functions with Parameters and Argument


# Important to be mindful of indentation


# *args and **kwargs

def addition(*x):
    print(x)
    print(type(x))
addition(1, 2, 3, 4, 5, 6)

# x,*y = 1, 2, 3, 6, 8
# print(y)
# print(type(y))


# def addition(*args):
#     total = 0
#     for numbers in args:
#         total += numbers
        
#     print(f'Sum = {total}')
# addition(1, 4, 5, 6, 6)

# def myFunction(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# myFunction(name ='Doku', age = 20)

# def myFunction(**kwargs):
#     print(kwargs.get('name'))
#     for keys, values in kwargs.items():
#         print(f'{keys} = {values}')

# myFunction(name ='Doku', age = 20)

def myFunction(*args, **kwargs):
    print(args)
    print(type(args))
    for keys, values in kwargs.items():
        print(f'{keys} = {values}')

myFunction('University of Ghana', name = 'Doku', age = 20)

