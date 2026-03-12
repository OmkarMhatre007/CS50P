from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:
    fonts = Figlet().getFonts()
    font = random.choice(fonts)
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in Figlet().getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(Figlet(font=font).renderText(text))
    
