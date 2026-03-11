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
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:-1]:
# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)

#say
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     # cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])

#itunes
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?term=" + sys.argv[1] + "&entity=song")
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])

#import own functions
##1.sayings
#def main(): 
#      hello("world")
#      goodbye("world")

# def hello(name):
#     print("hello, " + name)

# def goodbye(name):
#     print("goodbye, " + name)

# if __name__ == "__main__":
# main()

##2.say
# import sys

# from sayings import hello

# if len(sys.argv) == 2:
#     hello(sys.argv[1])
#And run say.py to test it.
