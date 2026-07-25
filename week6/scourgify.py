import sys
import csv

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
            filename = sys.argv[1]
            new_csv(filename)
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")

def new_csv(filename):
    with open(filename) as input_file:
        reader = csv.DictReader(input_file)
        with open(sys.argv[2],"w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames= ["first","last","house"])
            writer.writeheader()
            for row in reader:
                l_name, f_name = row["name"].split(",")
                writer.writerow({"first":f_name.lstrip(),"last":l_name,"house":row["house"]})

main()
