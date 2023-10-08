# Python string and methods

# When to use single or double quotation marks

"""
print("Ghana's premier university")
print('Ghana "premier" university')

"""
"""
country = "Ghana"
status = '"premier"'
statement = f"{country}'s {status} university"

print(statement)

"""

# Indexing: Python indexing starts from 0

"""
dream_school = "University of Bath"
#               0123456789.......17
print(dream_school[0])
print(dream_school[1])
print(dream_school[:10])
print(dream_school[14:])
print(dream_school[-1])
print(dream_school[14:-1])


"""
# len function
"""
print(len(dream_school))

"""

# STRING METHODS

# Capitalize -- Converts the first character to uppercase
"""
favourite = "mango"

print(favourite.capitalize())
print(favourite.upper())

"""

# Count -- Returns the number of times a specified character occurs in a string
pet = "My pet's name is shabby"
print(pet.count('e'))


# Find -- Searches the string for a specified value and returns the position (index) of where it was found
"""
surname = "Doku-Amponsah"
print(surname.find('h'))

"""
# Replace -- Replaces a specified value with another
snacks = "I love pizza"
print(snacks.replace('pizza', 'cake'))

hobby = 'I love reading '
print(hobby.replace('reading', 'painting'))


# Index -- Searches the string for a specified value and returns the position of where it was found
school = "Elican"
print(school.index('i'))

# Lower -- Co nverts a string into lower case
fav_fruit = "APPLE"
print(fav_fruit.lower())

# Upper -- Converts a string into upper case
name = "Doku-Amponsah"
print(name.upper())

# Isalnum -- Returns True if all characters in the string are alphanumeric
statement = "Nana2004"
print(statement.isalnum())

# Isdigit -- Returns True if all characters in the string are digits

password = '10947512'
print(password.isdigit())

# Isspace -- Returns True if all characters in the string are whitespaces

space = " "
print(space.isspace())

# Slipt -- Splits the string at the specified separator, and returns a list

shop_list = "Biscuits Kalypo Sardine Drinks"
print(shop_list.split())

# Startwith -- Returns true if the string starts with the specified value
sentence = "She is a best friend "
print(sentence.startswith('She'))
print(sentence.startswith('friend'))

# # Endwith -- Returns true if the string ends with the specified value

quote = "determination is always the key to success"
print(quote.endswith('success'))
print(quote.endswith('is'))