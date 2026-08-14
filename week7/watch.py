import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r"(^<iframe .+)http(s)?://(www\.)?youtube\.com/embed/([a-z0-9A-Z?=_]+)", s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(4)}"


if __name__ == "__main__":
    main()
