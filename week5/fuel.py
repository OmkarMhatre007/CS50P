def main():
    while True:
        fraction = input("Fraction:")
        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
        try:
            num, den = fraction.split("/")
            num = int(num)
            den = int(den)
        except (ValueError, ZeroDivisionError):
            raise ValueError
        if den == 0:
            raise ZeroDivisionError
        if num < 0 or den < 0:
            raise ValueError
        if num > den:
            raise ValueError
        percentage = round((num/den) * 100)
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
