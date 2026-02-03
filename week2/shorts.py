##Dictionaries
# report
# def main():
#     #spacecraft = {"name": "Chandrayaan 3", "distance": 0.00257}
#     spacecraft = {"name": "Mangalyaan"}
#     # spacecraft["distance"] = 1.53
#     spacecraft.update({"distance": 1.53, "orbit": "Mars"})

#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ========== REPORT ==========

#     Name: {spacecraft.get("name", "Unknown")}
#     Distance: {spacecraft.get("distance", "Unknown")} AU
#     Orbit: {spacecraft.get("orbit", "Unknown")}

#     ============================
#     """

# main()

#distances
# distances = {
#     "Chandrayaan 3": 0.00257,
#     "Mangalyaan": 1.53,
#     "Voyager 1": 163,
#     "New Horizons": 58,
#     "Pioneer 11": 44,
# }

# def main():
#     for distance in distances.values():
#         print(f"{distance} AU is {convert(distance)} meter")

# def convert(au):
#     return au * 149597870700

# main()

##Dictionary Methods
#WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# def main():
#     print("Welcome to Spelling Bee!")
    # print("Yours letters are: A I P C R H G")

    # while len(WORDS) > 0:
    #     print(f"{len(WORDS)} words left!")
    #     guess = input("Guess a word: ").upper()

    #     if guess == "GRAPHIC":
    #         WORDS.clear()
    #         print("You've won!")
    #     if guess in WORDS.keys():
    #         points = WORDS.pop(guess)
    #         print(f"Good job! You scored {points} points.")

    # print("That's the game!")

# def main():
#     print("Welcome to Spelling Bee!")
#     for word, point in WORDS.items():
#         print(f"{word} was worth {point} points.")

# main()

##For Loops
# def main():
#     names = ["Mario", "Luigi", "Daisy", "Yoshi"]
#     for name in names:
#         print(write_letter(name, "Princess Peach"))

# def write_letter(reciver, sender):
#     return f""" 
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         Dear {reciver},
        
#         You are cordially invited to a ball at
#         Peach's Castle this evening, 7:00 PM
        
#         Sincerely,
#         {sender}
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     """
# main()

##Lists
# results = ["Ferrari", "Red Bull Racing"]

# results.append("Mclaren")
# results.append("Mercedes")
# results.append("Aston Martin")

# results.append(["Racing Bulls", "Alpine"])
# results.remove(["Racing Bulls", "Alpine"])
# results.extend(["Racing Bulls", "Alpine"])

# results = ["Ferrari", "Red Bull Racing", "Mclaren", "Mercedes", "Aston Martin", "Racing Bulls", "Alpine"]

# results.remove("Alpine")
# results.insert(0, "Alpine")
# results.reverse()

# print(results)

##List and Dictionary Comprehensions
# def main():
#     counts = {}
#     words = get_words("address.txt")
#     lowercase_words = [word.lower() for word in words if len(word) > 4]

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
    
#     save_counts(counts)

# main()

##List Methods
# def main():
#     history = []

#     while True:
#         action = input("Action: ").lower()

#         if action == "undo":
#             undone = history.pop()
#             print(f"Undone: {undone}")
#         elif action == "restart":
#             history.clear()
#         else: 
#             history.append(action)
#             print(history)

# main()

##String Slicing
# def main():
#     phone = "617-495-1000"
#     print(phone[-8:])

# main()

