import re

def main():
    print(count(input("Text: ")))

def count(s):
    umm = re.findall(r"\bum\b", s, re.IGNORECASE)
    U = 0
    for i in umm:
        if i.lower() == "um":
            U += 1
        else:
            continue
    return U

if __name__ == "__main__":
    main()