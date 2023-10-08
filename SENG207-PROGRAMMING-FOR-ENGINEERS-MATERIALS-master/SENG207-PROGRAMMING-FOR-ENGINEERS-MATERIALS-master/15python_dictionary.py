# Python dictionary is a collection of key value pair of data.
# It is ordered and mutable.
# It does not support duplicate members

personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}

print(personal_info)
print(personal_info['name'])
print(personal_info['ID'])

# Dictionary Methods

# Copy -- Returns a copy of the dictionary
new_info = personal_info.copy()
new_info['name'] = 'Doku-Amponsah'
print(new_info)
# Clear -- Removes all the elements from the dictionary
'''
personal_info.clear()
print(personal_info)
'''

# Pop -- Removes the element with the specified key
personal_info.pop('age')
print(personal_info)

# Keys -- Returns a list containing the dictionary's keys
print(personal_info.keys())
# Values -- Returns a list containing the dictionary's values
print(personal_info.values())


# ------------------------------------------------------
personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
personal_info['height'] = 67.45 #to add a new key with a value
print(personal_info)

personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
del personal_info['age'] #to remove a key valued pair
print(personal_info)

print(len(personal_info))
# -------------------------------------------------------

if 'name' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'nage' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'email' not in personal_info:
    print('the key "email" is not in the dictionary')

new_string = str(personal_info)
print(new_string)

print(type(personal_info))

sorted_keys = sorted(personal_info)
print(sorted_keys) #sort the keys in the dictionary