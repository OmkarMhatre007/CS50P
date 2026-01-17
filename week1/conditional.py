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
# name = input("Enter your name: ")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Griffindor")
#     case "Draco" | "Crabbe" | "Goyle":
#         print("Slytherin")
#     case _:
#         print("Muggle")

#recommendations
# def main():
#     difficulty = input("Enter Difficulty of Game (Easy/Medium/Hard): ")
#     players = input("Single Player or MultiPlayers: ")

#     if difficulty == "Easy" and players == "Single Player":
#         recommend("Subway Surfers")
#     elif difficulty == "Medium" and players == "Single Player":
#         recommend("Shadow Fight 2")
#     elif difficulty == "Hard" and players == "Single Player":
#         recommend("Black Myth Wukong")
#     elif difficulty == "Easy" and players == "MultiPlayers":
#         recommend("Among Us")
#     elif difficulty == "Medium" and players == "MultiPlayers":
#         recommend("Fortnite")
#     elif difficulty == "Hard" and players == "MultiPlayers":
#         recommend("Call of Duty: Black Ops & Valorant")
#     else:
#         print("No recommendations available")
    
# def recommend(game):
#     print("You might enjoy playing this game: " + game)
    
# main()

#password
password = input("Enter password: ")
special_symbols = '@#$%^&'

symbols = any(char in special_symbols for char in password)

if password == "admin@123":
    print("Try strong password")
elif len(password) >= 8 and symbols == True:
    print("Password is saved successfully")
else:
    print("Invalid Password")
