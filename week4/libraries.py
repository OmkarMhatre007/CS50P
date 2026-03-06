##generate
# import random
# from random import choice

# coin = random.choice(["heads", "tails"])
# print(coin)
# number = random.randint(1, 10)
# print(number) 
# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

##average
# import statistics

# print(statistics.mean([100, 90]))

##name
import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# for arg in sys.argv[1:-1]:
for arg in sys.argv[1:]:
    print("hello, my name is", arg)