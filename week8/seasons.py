import sys
import re
from datetime import date
import inflect

p = inflect.engine()
def main():
    birth_date = input("Date of Birth: ")
    try:
        y, m, d = check_birthday_date(birth_date)
    except ValueError:
        sys.exit("Invalid Date")
    in_words = calculate_result(y, m, d)
    print(in_words)
    
def check_birthday_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        y, m, d = birth_date.split("-")
        return  y, m, d
    else:
        raise ValueError
            
def calculate_result(y, m, d):
    try:
        dob = date(int(y), int(m), int(d)) 
        dot = date.today()
        difference = dot - dob
        total_min = difference.days * 24 * 60
        result = p.number_to_words(total_min, andword="")
        return f"{result.capitalize()} minutes"
    except ValueError:
        return sys.exit("Invalid Date")

if __name__ == "__main__":
    main()
    