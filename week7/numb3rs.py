import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    numbers = ip.split(".")
    num1 = r"^\d+\.\d+\.\d+\.\d+$"
    if re.search(num1, ip):
        for number in numbers:
            if not 0 <= int(number) <= 255 or (len(number) > 1 and number.startswith("0")):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
