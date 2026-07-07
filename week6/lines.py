import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith('.py') == False:
            sys.exit("Not a Python file")
        else:
            filename = sys.argv[1]
            print(calculate_lines_of_code(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")
        
def calculate_lines_of_code(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        count = 0
                
    for line in lines:
        if line.strip() == "" or line.lstrip().startswith("#"):  
            continue
        count += 1
    return count               
       
main()
