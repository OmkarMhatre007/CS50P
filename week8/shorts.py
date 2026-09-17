##Classes
#packages
# class Package:
#     def __init__(self, number, sender, recipient, weight):
#         self.number = number
#         self.sender = sender
#         self.recipient = recipient
#         self.weight = weight

# def main():
#     packages = [
#         Package(number=1, sender="Alice", recipient="Bob", weight=10),
#         Package(number=2, sender="Charlie", recipient="David", weight=5)
#     ]

# main()

##Class Methods and Class Variables
#food
# class Food:
#     base_hearts = 1

#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.hearts = Food.calculate_hearts(ingredients)

#     @classmethod
#     def calculate_hearts(cls, ingredients):
#         hearts = cls.base_hearts
#         for ingredient in ingredients:
#             if "hearty" in ingredient.lower():
#                 hearts += 2
#             else:
#                 hearts += 1
#         return hearts

#     @classmethod
#     def from_nothing(cls, hearts):
#         food = cls(ingredients=[])
#         food.hearts = hearts
#         return food

# def main():
#     mushroom_skewer = Food(ingredients=["mushrooms", "Hearty Mushroom"])
#     print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

#     mushroom_skewer = Food.from_nothing(hearts=2)
#     print(f"This skewer heals {mushroom_skewer.hearts} hearts!")
    
# main()

##Instance Variables
#packages
# class Package:
#     def __init__(self, number, sender, recipient, weight):
#         self.number = number
#         self.sender = sender
#         self.recipient = recipient
#         self.weight = weight

# def main():
#     packages = [
#         Package(number=1, sender="Alice", recipient="Bob", weight=10),
#         Package(number=2, sender="Charlie", recipient="David", weight=5)
#     ]
#     for package in packages:
#         print(f"Package {package.number}: {package.sender} to {package.recipient}, Weight: {package.weight}kg")

# main()

##Instance Methods
#packages
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, Weight: {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Charlie", recipient="David", weight=5)
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")
main()