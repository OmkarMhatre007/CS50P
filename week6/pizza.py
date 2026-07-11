import sys
import csv
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith('.csv') == False:
            sys.exit("Not a CSV file")
        else:
            filename = sys.argv[1]
            print(tabulate(get_pizza_menu(filename), headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def get_pizza_menu(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        return list(reader)
main()