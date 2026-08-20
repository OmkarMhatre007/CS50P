import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    check = re.search(r"^(\d{1,2})(\:)?(\d{1,2})? (AM|PM) to (\d{1,2})(\:)?(\d{1,2})? (AM|PM)$", s, re.IGNORECASE)
    if check:
        hours1 = int(check.group(1))
        minutes1 = int(check.group(3) or 0)
        am_pm1 = (check.group(4))
        hours2 = int(check.group(5))
        minutes2 = int(check.group(7) or 0)
        am_pm2 = (check.group(8))
        if hours1 > 12 or hours2 > 12:
            raise ValueError
        else:
            return f"{left(hours1,minutes1,am_pm1)} to {right(hours2,minutes2,am_pm2)}"
    if not check:
        raise ValueError

def left(hours1,minutes1,am_pm1):
    am_pm1 = am_pm1.upper()
    if minutes1 > 59:
        raise ValueError
    elif am_pm1 == "AM":
        if hours1 == 12:
            hours1 = 0
            return f"{hours1:02d}:{minutes1:02d}"
        elif minutes1 == 0:
            return f"{hours1:02d}:{minutes1:02d}"
        else:
            return f"{hours1:02d}:{minutes1:02d}"
    elif am_pm1 == "PM":
        if hours1 == 12:
            hours1 = 12
            return f"{hours1:02d}:{minutes1:02d}"
        if hours1 < 12:
            new1 = hours1 + 12
            if minutes1 == 0:
                return f"{new1}:{minutes1:02d}"
            return f"{new1}:{minutes1:02d}"

def right(hours2,minutes2,am_pm2):
    am_pm2 = am_pm2.upper()
    if minutes2 > 59:
        raise ValueError
    elif am_pm2 == "AM":
        if hours2 == 12:
            hours2 = 0
            return f"{hours2:02d}:{minutes2:02d}"
        elif minutes2 == 0:
            return f"{hours2:02d}:{minutes2:02d}"
        else:
            return f"{hours2:02d}:{minutes2:02d}"
    elif am_pm2 == "PM":
        if hours2 == 12:
            hours2 = 12
            return f"{hours2:02d}:{minutes2:02d}"
        if hours2 < 12:
            new2 = hours2 + 12
            if minutes2 == 0:
                return f"{new2}:{minutes2:02d}"
            return f"{new2}:{minutes2:02d}"

if __name__ == "__main__":
    main()

## Rules
#1.Convert any 12 hr format to 24 hr format
#2.AM and PM should input capital
#3.ValueError if input format is wrong
#4.AM or PM anyone can we 1st in sentence input