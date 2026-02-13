# number 
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x ?"))
            # print(f"x is {x}")
            # break
        except ValueError:
            print("x is not an integer")
            #  or pass 
        else:
            break # or return x
    return x

# print(f"x is {x}")
main()
