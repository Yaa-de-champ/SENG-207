# Python tuple is a collection which is ordered.
# A tuple is not mutable
# It allows duplicate members



"""
market_list = ("pepper", "Onion", "Mango", "Cabbage", "Onion")
print(market_list)
print(type(market_list))

print(market_list[2])
print(market_list[2][1])
"""

# checking mutability of tuples
"""
market_list = ("pepper", "Onion", "Mango", "Cabbage", "Onion")
# market_list[0] = "Carrot"
# print(market_list.append("Carrot"))
"""

# there is an error because it cannot be changed
# can support benefits like passwords

# Unpack Tuple
a, b = (2, 3)
print(a)
print(b)

"""
# x, y = (2, 4, 5)
# print(x)
# there is an error: to many errors to unpack
"""
e, f, *g = (1, 3, 4, 5, 5)
print(e)
print(f)
print(g)

# exploring the use of count function
market_list = ("pepper", "Onion", "Mango", "Cabbage", "Onion")
print(market_list.count("Cabbage"))
print(market_list.count("Onion"))

print(market_list.index("Mango"))