## debugging
# def main():
#     height = int(input("Height:"))

#     for h in range(height + 1):
#         spaces = " " * (height - h)
#         hash = "#" * (h)
#         print(spaces + hash)
# main()

## Handling Exceptions

# distances
# distances = {
#     "Ferrari": "5",
#     "Mclaren": "4",
#     "Red Bull Racing": "3 KM",
#     "Mercedes": "2",
#     "Aston Martin": "1"
# }

# def main():
#     F1car = input("Enter the F1 car: ")

#     try:
#         km = float(distances[F1car])
#     except ValueError:
#         print(f"Can't convert {distances[F1car]} to float")
#         return
#     except KeyError:
#         print(f"{F1car} is not in list")
#         return
    
#     c = convert(km)
#     print(f"{c} is m away")

# def convert(km):
#     return km * 1000

# main()

## Raising Exceptions

def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid min")
    
    return minutes/miles

main()
