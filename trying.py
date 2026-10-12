# x = float(input("Enter: "))
# print(f"you entered: {x:.1f}")
# a = "hello, there"
# if a.endswith("there"):
#     print("true")
# else:
#     print("false")
# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(1,n+1):
#         print("#" * i)

# main()

# import random

# coin = random.choice(["head","tail"])
# print(coin)

# from random import choice

# coin = choice(["head","tail"])
# print(coin)

# import random

# number = random.randint(1,10)
# print(number)

# import random

# cards = ["jack","queen","king"]
# random.shuffle(cards)
# print(cards)
# for card in cards:
#     print(card)

# import statistics

# print(statistics.mean([100, 90]))

# import sys
# try :
#     print("hello, i am ", sys.argv[1])
# except IndexError :
#     print("too few arguments")

# import random

# dice = [1, 2, 3, 4, 5, 6]
# random.shuffle(dice)
# for dice in dice :
#     print(dice)

# import sys

# if len(sys.argv) < 2 :
#     sys.exit("Too few words!")
# elif len(sys.argv) > 2 :
#     sys.exit("Too many words!")
# else :
#     print("Hey,", sys.argv[1])

# import sys

# if len(sys.argv) < 2 :
#     print("Too few words !")

# for word in sys.argv[1:] :
#     print("My name is", word)

# import cowsay
# import sys

# if len(sys.argv) == 2 :
#     cowsay.cow("Hello, " + sys.argv[1])

# import cowsay
# import sys

# if len(sys.argv) == 2 :
#     cowsay.trex("Hello, " + sys.argv[1])

# import json
# import requests
# import sys

# if len(sys.argv) != 2 :
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
# o = response.json()
# for result in o["results"] :
#     print(result["trackName"])

# def main() :
#     hello("world")
#     goodbye("world")

# def hello(name) :
#     print(f"hello, {name}")

# def goodbye(name) :
#     print(f"goodbye, {name}")

# if __name__ == "__main__" :
#     main()

import sys
from say import goodnight

if len(sys.argv) == 2 :
    goodnight(sys.argv[1])