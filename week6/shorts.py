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
# import csv
# import numpy as np
# from PIL import Image

# def main():
#     with open("views.csv", "r") as file, open("analysis.csv", "w", newline="") as analysis:
#         reader =csv.DictReader(file)
#         writer = csv.DictWriter(analysis, fieldnames=["Id", "Title", "Brightness"])
#         writer.writeheader()
    
#         for row in reader:
#             row["Brightness"] = round(calculate_brightness(f"{row['Id']}.jpeg"), 2)
#             writer.writerow(row)
#             # brightness = calculate_brightness(f"{row['Id']}.jpeg")
#             # writer.writerow(
#             #     {
#             #         "Id": row["Id"],
#             #         "Title": row["Title"],
#             #         "Brightness": round(brightness, 2)
#             #     })

#             # print(row)

# def calculate_brightness(filename):
#     with Image.open(filename) as image:
#         brightness = np.mean(np.array(image.convert("L"))) / 255
#     return brightness

# main()


##Reading and Writing Files
def main():
    with open("HP.txt", "r") as f:
        # contents = f.read()
        contents = f.readlines()

    chapter1 = contents[3:119]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
    # print(chapter1[0])
    # print(contents[0])

main()