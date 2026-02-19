def main():
    percentage = get_value()
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_value():
    while True:
        try:
            fraction = input("Fraction:")
            num, den = fraction.split("/")
            num = int(num)
            den = int(den)

            if den == 0:
                continue
            if num < 0 or den < 0:
                continue
            if num > den:
                continue
            percentage = round((num/den) * 100)
            break
        except (ValueError, ZeroDivisionError):
            pass
    return percentage

main()
