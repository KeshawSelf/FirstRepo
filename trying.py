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

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + input())
# o = response.json()
# print(o)

# def main() :
#     hello("world")
#     goodbye("world")

# def hello(name) :
#     print(f"hello, {name}")

# def goodbye(name) :
#     print(f"goodbye, {name}")

# if __name__ == "__main__" :
#     main()

# import sys
# from say import goodnight

# if len(sys.argv) == 2 :
#     goodnight(sys.argv[1])

# from say import wish
# name = input("Enter your name: ")
# wish(name)

# import emoji
# print(emoji.emojize(":thumbs_up:"))

# import pyfiglet
# import sys

# print(pyfiglet.figlet_format("Baymax", font = "alphabet"))

# from pyfiglet import Figlet
# import pyfiglet
# import random
# figlet = Figlet()
# f = random.choice(figlet.getFonts())
# x = input("Enter: ")
# print(f"{pyfiglet.figlet_format(x, font = f)}")

# import pyfiglet
# from pyfiglet import Figlet
# import random
# import sys

# # figlet = Figlet()

# # if len(sys.argv) == 1 :
# #     x = input("Input: ")
# #     print(f"Output: {pyfiglet.figlet_format(x, font = random.choice(figlet.getFonts()))}")

# # if len(sys.argv) > 1 :
# #     if sys.argv[1] == "-f" or sys.argv[1] == "--font" :
# #         if sys.argv[2] in figlet.getFonts() :
# #             y = input("Input: ")
# #             print(f"{pyfiglet.figlet_format(y, font = sys.argv[2])}")
# #         else :
# #             sys.exit("Invalid usage")

# #     else :
# #         sys.exit("Invalid usage")

# # if len(sys.argv) == 1 :
# #     x = input("Input: ")
# #     Figlet().setFont(font = random.choice(Figlet().getFonts()))
# #     print(f"Output: {Figlet().renderText(x)}")

# # if len(sys.argv) > 1 :
# #     if sys.argv[1] == "-f" or sys.argv[1] == "--font" :
# #         if sys.argv[2] in Figlet().getFonts() :
# #             print(sys.argv[2])
# #             y = input("Input: ")
# #             Figlet().setFont(font = sys.argv[2])
# #             print(f"Output: {Figlet().renderText(y)}")
# #         else :
# #             sys.exit("Invalid usage")

# #     else :
# #         sys.exit("Invalid usage")

# x = input("Enter: ")

# i = 5
# while i > 0 :
#     f = random.choice(Figlet().getFonts())
#     Figlet().setFont(font = "slant")
#     print(f"Output: {Figlet().renderText(x)}")
#     i -= 1
# print(f"{random.choice(Figlet().getFonts())}")

# from pyfiglet import Figlet
# f = Figlet()
# x = "Dummy"
# f.setFont(font = "alphabet")
# print(f.renderText(x))
# f.setFont(font = "rectangles")
# print(f.renderText(x))


