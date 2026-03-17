import inflect

def main():
    names = [ ]
    while True:    
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    p = inflect.engine()
    print( )
    print(f"Adieu, adieu, to {p.join(names)}")
main()


##Algorithm
# 1. import inflect library
# 2. Create an empty list to store the names.
# 3. Take the inputs names from the user and store them in a list till control d by the user.
# 4. print the names in the required format using inflect library.