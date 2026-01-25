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
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to Spelling Bee!")
    print("Yours letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper()

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")

main()
