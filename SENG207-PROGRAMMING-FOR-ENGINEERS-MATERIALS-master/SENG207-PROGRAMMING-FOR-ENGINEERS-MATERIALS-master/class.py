school = "University of Ghana" #this becomes a global variable because it can be accessed anywhere in the code.


    # def myFunction():
    #     print("This is my baking pan function")
    # department = 'Biomedical Engineeing' #this becomes a class variable

class BakingPan:
    unit_price = 5
    def __init__(self, flour, sugar, special_ingredient):
        self.flour = flour
        self.sugar = sugar
        self.special_ingredient = special_ingredient

    def bread_name(self):
        return f'{self.special_ingredient} bread'
    
    def total_price(self, quantity):
        # total = quantity * self.unit_price
        total = quantity * BakingPan.unit_price
        return f'Total Price of {quantity} {self.bread_name()}= Ghc{total}'


bread1 = BakingPan("Hard", "20 grams", "Coconut")
bread2 = BakingPan("Soft", "40 grams", "Banana")
bread3 = BakingPan('Hybrid', 'cube sugar', 'mixed fruits')

# print(bread1.bread_name())
# print(bread2.bread_name())
print(bread3.bread_name())
print(bread3.total_price(7))

# print(bread1.total_price(10))
# print(bread2.total_price(5))





# print(bread1.flour)
# print(bread1.sugar)
# print(bread1.special_ingredient)


# print(bread2.flour)
# print(bread2.special_ingredient)


# print(school)
# print(BakingPan.department)
# print(bread1.department)




# print(BakingPan.myFunction())

# characteristics of a function and a method.

# the object becomes the instance of the class

