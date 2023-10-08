# Python conditional statement if else elif


# EXERCISE

# Program takes two inputs and checks which of the inputs is greater

# Check Odd or Even numbers

# Grade check results:
# User input score and grade displays in the terminal

# ------------Exercise with the help of chat gpt😘-------------

# Check which input is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print(num1, "is equal to", num2)

# Check odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Grade check
score = int(input("Enter score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)
