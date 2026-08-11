## Patterns
# import re 

# def main():
#     code = input("Hexadecimal color code: ")

#     pattern = r"^#[a-f0-9]{6}$"
#     match = re.search(pattern, code, re.IGNORECASE)
#     if match:
#         print(f"Valid. Matched: {match.group()}")
#     else:
#         print("Invalid")

# main()

## Capture Groups
import re

locations = {"+1": "United States and Canada", "+44": "United Kingdom", "+91": "India"}

def main():
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Phone Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group(1)
        print(locations[country_code])
        # print("Valid")
    else:
        print("Invalid")

main()