def main():
    try:
        fraction = input("Fraction:")
        print(gauge(convert(fraction)))
        
    except (ValueError, ZeroDivisionError):
        pass

def convert(fraction):
        num, den = fraction.split("/")
        num = int(num)
        den = int(den)

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

# algorithm
