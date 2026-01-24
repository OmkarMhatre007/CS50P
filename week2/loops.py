#while
# i = 3 
# while i != 0:
#     print("meow")
#     i = i - 1
# or  i += 1

#for
# for i in [0, 1, 2]:
#     print("meow")

# for i in range(3):
#     print("meow")
# print("meow\n" * 3, end="")

# while & for
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow") 

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What's n?"))
#         if n > 0:
#             break
#     return n

# def meow(number):
#     for _ in range(number):
#         print("meow")

# main()

#hogwarts
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin" ]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

##dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")


