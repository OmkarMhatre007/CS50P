import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    check = re.search(r"^(\d{1,2})(\:)?(\d{1,2})? (AM|PM) to (\d{1,2})(\:)?(\d{1,2})? (AM|PM)$", s, re.IGNORECASE)
    hours1 = int(check.group(1)) 
    minutes1 = int(check.group(3) or 0) 
    am_pm1 = (check.group(4))
    hours2 = int(check.group(5)) 
    minutes2 = int(check.group(7) or 0) 
    am_pm2 = (check.group(8))
    if check:
        if hours1 == None or hours2 == None:
            raise ValueError
        if hours1 > 12 or hours2 > 12:
            raise ValueError
        else:
            return f"{left(hours1,minutes1,am_pm1)} to {right(hours2,minutes2,am_pm2)}"

def left(hours1,minutes1,am_pm1):
    if minutes1 > 59:
        raise ValueError
    elif am_pm1 == "AM":
        if hours1 == 12:
            new1 = hours1.replace(12, 00)
            return f"{new1}:{minutes1}"
        elif minutes1 == " ":
            return f"{hours1}:00"
        else:
            return f"{hours1}:{minutes1}"
    elif am_pm1 == "PM":
        if hours1 < 12:
            new2 = hours1 + 12
            if minutes1 == " ":
                return f"{new2}:00"
            return f"{new2}:{minutes1}"
        if 12 < hours1 < 24:
            return f"{hours1}:{minutes1}"
    
def right(hours2,minutes2,am_pm2):
    if minutes2 > 59:
            raise ValueError
    elif am_pm2 == "AM":
        if hours2 == 12:
            new3 = hours2.replace(12, 00)
            return f"{new3}:{minutes2}"
        elif minutes2 == " ":
            return f"{hours2}:00"
        else:
            return f"{hours2}:{minutes2}"
    elif am_pm2 == "PM":
        if hours2 < 12:
            new4 = hours2 + 12
            if minutes2 == " ":
                return f"{new4}:00"
            return f"{new4}:{minutes2}"
        if 12 < hours2 < 24:
            return f"{hours2}:{minutes2}"
                
if __name__ == "__main__":
    main()

## Rules
#1.Convert any 12 hr format to 24 hr format
#2.AM and PM should input capital
#3.ValueError if input format is wrong
#4.AM or PM anyone can we 1st in sentence input
#5.