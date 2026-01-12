#x = input("Enter a number x: ")
#y = input("Enter a number y: ")
#z = int(x) + int(y)
#print (z)

#x = int(input("Enter a number x: "))
#y = int(input("Enter a number y: "))
#print (x + y)

#x = float(input("Enter a number x: "))
#y = float(input("Enter a number y: "))
#print (x + y)
#z = round(x + y)
#print (z) 
#print (f"{z:,}")
#print (f"{z:.2f}") #used for rounding to 2 decimal places

def main():
    x = int(input("Enter a number x:"))
    print("x squared is", square(x))


def square(n):
    return n * n

main()
