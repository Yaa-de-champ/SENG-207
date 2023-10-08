# Loop
# For loop
'''
name = "Nana Yaa"
for char in name:
    print(char)
'''

countries = ["France", "Ghana", "Germany", "England", "Ghana"]
for country in countries:
    print(country)
    if country == "Germany":
        break

#the variable country is a new variable while countries is the variable of the list.

'''
for country in enumerate(countries):
    print(country) #returns a tuple containing the index and element of the list. eg.(0, 'France')
    print(country[0])
'''
countries = ["France", "Ghana", "Germany", "England", "Ghana"]
for country in enumerate(countries):
    if country[1] == "Ghana":
        print(country)
# ---------------------------------------------------

names = ["Nana", "Ama", "Kwame"]
scores = [95,  75, 50]
grades = ["A", "B+", "D"]

for name, score, grade in zip(names, scores, grades):
    print(f'{name} had {score} percent in the Thermodynamics Exams. She will see grade {grade} in her records.\n')

# ----------------------loops on a dictionary-----------------

classlist = {'Safui' : 'Course Rep', 'Nana Yaa' : 'Assitant Course Rep', ' Issabella':' Secretary'}
for key, value in classlist.items():
    print(f"{key} is the {value} of the Bmen Level 200 Class.\n")
    print(key, value) #why is it printing the key and value of Isabella and Secretary.
for value in classlist.values():
    print(value)
for key in classlist.keys():
    print(key)
# # --------------------------------------------------------------------------

# print("[",end='')
# for x in range(1, 20, 2):
#     print(x, end =",")
# print("]")


# While 



# Loop through List

# Loop through multiple Lists simultaneously using zip nethod


# range method and loops


# Loop through Dictionary

# Exercise
# 1. Find all the even numbers in a range
# 2. Find the sum of all elements in a list
