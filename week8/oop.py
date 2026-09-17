##student 
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student 

# if __name__ == "__main__":
#     main()

##Classes
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         elif not house:
#             raise ValueError("Missing house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self._name = name

# ## Getter
#     @property
#     def house(self):
#         return self._house
    
# ## Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)
        
# def main():
#     student = Student.get()
#     print(student)

# if __name__ == "__main__":
#     main()

##type
# print(type(50))

##class methods
# import random
# class Hat:
#     house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     @classmethod        
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.house))

# Hat.sort("Harry")

##Inheritance
##wizard

# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name

#     ...

# class Student(Wizard):
#     def __init__(self, name, house):
#         super().__init__(name)
#         self.house = house

#     ...

# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     ...

# wizard = Wizard("Albus Dumbledore")
# student = Student("Harry Potter", "Gryffindor")
# professor = Professor("Minerva McGonagall", "Transfiguration")

##vault
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(1000, 50, 25)
print(potter)

weasley = Vault(200, 25, 10)
print(weasley)

total = potter + weasley
print(total)
