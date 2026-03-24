import random
def main():
    level = get_level()
    number = random.randint(1, level)
    guess_number(number)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def guess_number(number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            else:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    
                    break
        except ValueError:
            pass

main()

##Algorithm 
#1. get the level input from the user 
#2. check the input is valid (is it a number? is it within the range?)
#3. generate a random number 
#4. compare the input with the random number 
#5. provide feedback to the user 
#6. repeat until the user guesses correctly 