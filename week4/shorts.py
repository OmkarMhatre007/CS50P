##API Calls
# import requests

# def main():
#     print("Search the Art Institute of Chicago!")
#     artist = input("Artist: ")  

#     try:
#         response = requests.get(
#             "https://api.artic.edu/api/v1/artworks/search",
#             {"q": artist}
#         )
#         response.raise_for_status()
#     except requests.HTTPError:
#         print("Couldn't complete requests!")
#         return
        
#     content = response.json()
#     for artwork in content["data"]:
#         print(f"* {artwork['title']}")

# main()

##Creating Modules and Packages

##Random Module
# import random

# cards = ["jack", "queen", "king"]

# def main():
#      random.seed(0)
#      print(random.choices(cards, k=2))
#     # print(random.choices(cards, weights=[75, 20, 5], k=2))


# main()

##Style
students = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin",
    "Luna": "Ravenclaw",
    "Cedric": "Hufflepuff"
}
for student in students:
    print(student)