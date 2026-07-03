def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    min_len = 2
    max_len = 6

    if not plate.isalnum():
        return False
    elif not min_len <= len(plate) <= max_len:
        return False
    elif not plate[:2].isalpha():
        return False
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == "0":
                return False
            return plate[i:].isdigit()
    return True
    
if __name__ == "__main__":
    main()
