import sys, os
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) == 3:
            imagename = sys.argv[1]
            shirt(imagename)
        else:
            sys.exit("Invalid Input")
    except FileNotFoundError:
        sys.exit("Input does not exists")

def shirt(imagename):
    end = [".jpg",".png",".jpeg"]
    end_one = os.path.splitext(imagename)
    end_two = os.path.splitext(sys.argv[2])

    if end_two[1] not in end:
        sys.exit("Invalid output")
    elif end_one[1].lower() == end_two[1].lower() and end_one[1] in end:
        input_image = Image.open(imagename)
        shirt = Image.open("shirt.png")
        size = shirt.size
        input_image = ImageOps.fit(input_image, size)
        input_image.paste(shirt, shirt)
        input_image.save(sys.argv[2])
    elif end_two[1].lower() != end_one[1].lower() and end_one[1] in end:
        sys.exit("Input and output have different extensioins")
main()

