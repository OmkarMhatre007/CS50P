name = input("Enter your name:")

with open("name1.txt", "w", newline="") as file:
    file.write(f"{name}")

with open("name1.txt", "r", newline="") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.strip())


#Algorithm

#1. import sys
#2. check command line arguments
#3. get file name from argument and put in open file to read that file.
#4. read that lines, and ignore the whitespaces and comments and count the code lines
#5. give the output no. of lines 