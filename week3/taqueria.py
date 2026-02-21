menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    t = 0

    while True:
        try:
            k = input("Item: ").strip().title()
            if k in menu:
                t += menu[k]
                print(f"Total: ${t:.2f}")
        except (EOFError):
            break
main()
