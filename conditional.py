# Compare 
# x = int(input("Enter a x number: "))
# y = int(input("Enter a y number: "))

# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# def sub(name):
#     print(f"Your subject is selected.")

# subject = input("Enter your subject: ")

# if subject == "AI & DS":
#    sub(subject)
# else:
#     print("Subject is not available for you.")

#grade
# def grade():
#     if score >=90 and score <=100:
#         print("Your grade is A")
#     elif score >=80 and score <=90:
#         print("Your grade is B")
#     elif score >=70 and score <=60:
#         print("Your grade is C")
#     elif score >=60 and score <=35:
#         print("Your grade is D")
#     else:
#         print("You are fail")

# score = int(input("Enter your score: "))
# grade()

#parity
# input = int(input("Enter a number: "))

# if input % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# match
name = input("Enter your name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco" | "Crabbe" | "Goyle":
        print("Slytherin")
    case _:
        print("Muggle")

