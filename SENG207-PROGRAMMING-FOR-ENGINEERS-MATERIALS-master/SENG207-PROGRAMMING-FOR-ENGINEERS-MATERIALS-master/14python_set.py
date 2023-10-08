# Python set is a collection which is unordered and not mutable.
# It does not allow duplicate members


# Union and Intersection


# Difference


friends = {'Issabella', 'Lois', 'Sefakor', 'Gafuru'}
bmenmates = {'Issabella', 'Sefakor'}
# common_names = bmenmates.intersection(friends)
# cn = friends.intersection(bmenmates)

# print(common_names)
# print(cn)

# all elements in friends but not in  bmenmates
friends_not_classmates = friends.difference(bmenmates)
print(friends_not_classmates)

fav_course = {'ThermoD', 'Programming'}
course = {'french', 'mathematics', 'ThermoD'}

print(fav_course.difference(course))
print(course.difference(fav_course))