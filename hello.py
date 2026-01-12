##name = input("Enter your name: ")

# Remove whitespace from str and capitalize user input and can put with the 1st line name function
##name = name.strip().title()

#Split user name into first and last name
##first, last = name.split(" ")

##print("Hello " + name + ", welcome to the future")

def hello(to="world"):
    print("hello,", to)


hello()  # prints "hello, world"
name = input("Enter your name: ")
hello(name)

# Rewatch the last 10 mins of cs50P lecture 1 for def function syntax
