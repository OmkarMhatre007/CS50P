# Patterns
import re 

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-f0-9]{6}$"
    match = re.search(pattern, code, re.IGNORECASE)
    if match:
        print(f"Valid. Matched: {match.group()}")
    else:
        print("Invalid")

main()