### name
# name = []
# name = input("Enter your name: ")

# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("name.txt", "r") as file:
#      lines = file.readlines()

# for line in lines:
#     print("hello,", line.strip())

## with open("name.txt", "r") as file:
#       for line in file:
            # print("hello,", line.strip())

## with open("name.txt", "r") as file:
#        for line in file:            
#             name.append(line.strip())

# for name in sorted(name):  #we can reverse the order by adding reverse=True
#     print(f"hello, {name}")

## with open("name.txt") as file:
#        for line in sorted(file):
#            print(f"hello,", line.strip())

### Students
## with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# import csv

# students = []

# with open("students.csv") as file:
#     # reader = csv.reader(file)
#     # for name, home in reader:
#     #     students.append({"name": name, "home": home})
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#      print(f"{student['name']} is from {student['home']}") 

# import csv

# name = input("Enter your name: ")
# home = input("Where are you from? ")

# with open("students.csv", "a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})

##Costume
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif", save_all=True, append_images=images[1:], duration=200, loop=0
    )
# Take two gif images and combine them into one gif image. The first image is the base image, and the second image is the overlay image. The overlay image is placed on top of the base image, and the result is saved as a new gif image.And that image is saved as costume.gif. The duration of each frame is set to 200 milliseconds, and the loop is set to 0, which means the gif will loop indefinitely.
