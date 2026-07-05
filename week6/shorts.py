##Pillow: Pillow is a Python Imaging Library that adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities.
# from PIL import Image
# from PIL import ImageFilter

# def main():
#     with Image.open("1.jpeg") as img:
#         img = img.rotate(180)
#         img = img.filter(ImageFilter.FIND_EDGES)
#         img.save("2.jpeg")

# main()


##Reading and Writing CSVs
import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as file:
        reader =csv.DictReader(file)
        for row in reader:
            print(row)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main()

# Lecture watched till def main() completion and run 7-8 mins only out of 20 mins.