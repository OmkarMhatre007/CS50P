### name
name = []
# name = input("Enter your name: ")

# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("name.txt", "r") as file:
#      lines = file.readlines()

#  for line in lines:
#      print("hello,", line.strip())

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
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# Stop's at 39 mins in lecture.