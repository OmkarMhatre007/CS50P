#calculator
# def main():
#     x = (input("What's x? "))
#     print("x squared is", square(x))

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     main()

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()