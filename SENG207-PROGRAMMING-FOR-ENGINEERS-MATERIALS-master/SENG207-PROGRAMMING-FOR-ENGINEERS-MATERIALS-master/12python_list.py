# Python list is a collection which is ordered and mutable.
# It allows duplicate members
fruits = ["mango","Orange", "Pawpaw", "mango"]
print(fruits)

# --------------------------------------------

stationeries = ["Pencil", "Diary", "Ruler"]
print(stationeries)
print(type(stationeries))

# list accepts different data types
information =[1, True, "Nana Yaa", 34.56]
print(information)

countries = ["Ghana", "Nigeria", "United Kingdom", "Germany", "Algeria"]
print(countries[2])
print(countries[-1])
print(countries[:3])



# len fucntion
countries = ["Ghana", "Nigeria", "United Kingdom", "Germany", "Algeria"]
print(len(countries))

# LIST METHODS

# Append -- Adds an element at the end of the list
countries = ["Ghana", "Nigeria", "United Kingdom", "Germany", "Algeria"]
countries.append("Togo")
print(countries)

# Clear -- Removes all the elements from the list
countries = ["Ghana", "Nigeria", "United Kingdom", "Germany", "Algeria"]
countries.clear()
print(countries)

# Copy -- Returns a copy of the list
stationeries = ["Pencil", "Diary", "Ruler"]
new = stationeries.copy()
print(new)

# Count -- Returns the number of elements with the specified value
stationeries = ["Pencil", "Diary", "Ruler"]
print(stationeries.count("Pencil"))
print(fruits.count("mango"))

# Index -- Returns the index of the first element with the specified value
countries = ["Ghana", "Nigeria", "United Kingdom", "Germany", "Algeria"]
countries.sort()
print(countries)
print(countries.index("Nigeria"))

# Sort -- Sorts the list
marks = [90, 99, 45, 67, 90, 56, 34, 89]
marks.sort() #sorts in asceding order
marks.sort(reverse=True) #sorts in descending order
print(marks)

# Reverse -- Reverses the order of the list
fruits = ["mango","Orange", "Pawpaw", "mango"]
marks = [90, 99, 45, 67, 90, 56, 34, 89]
marks.reverse() #reverses the order and not necessarily sort it out
print(marks)

# Remove -- Removes the first item with the specified value
marks = [90, 99, 45, 67, 90, 56, 34, 89]
marks.remove(90)
print(marks)

fruits = ["mango","Orange", "Pawpaw"]
fruits.remove("mango")
print(fruits)

# Pop -- Removes the element at the specified position
marks = [90, 99, 45, 67, 90, 56, 34, 89]
marks.pop()
marks.pop(3)
print(marks)

fruits = ["mango","Orange", "Pawpaw", "mango"]
fruits.pop()
print(fruits) #why didn't it remove all mangoes?