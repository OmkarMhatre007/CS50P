import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y 

        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")  

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 4 > level > 0:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError
    
if __name__ == "__main__":
    main()

##Algorithm
# . Ask user for the level between 1-3 if not then repromt.
# . Check the level and decide the range of random number generation
# . generate the random numbers in Addition equation x + y for 10 problems(10 times)
# . check the user answer if correct next problem but if wrong display EEE and ask same problem again
# . ask the wrong answer problem again for 3 times, if still wrong display the correct answer of problem and ask next problem
# . after 10 problems display score of 10 problems 