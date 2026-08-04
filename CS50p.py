# name = input("What's your name? ").strip().title()
# first, second, third = name.split()
# print(f"hello, {first}")
# print(f"hello, {second}")
# print(f"hello, {third}")

# x = float(input("What's x? "))
# y = float(input("What's y? "))
# # print(type(x + y))
# # print(int(input("What's x? ")) + int(input("What's y? ")))
# z = x + y

# print(f"{z:.0f}")
# def hello(name):
#     print(f"hello, {name}")
# x = input("What's your name? ")
# hello(x)

# def main() :
#     name = input("What's your name? ")
#     hello(name)
#     hello()

# def hello(to="world"):
#     print("hello, " ,to)

# main()

# def main():
#     n = int(input("Enter a number: "))
#     print("Square is",square(n))


# def square(x):
#     return x * x

# main()

# a = "pocoself"
# b = a.casefold()
# c = input("Enter: ")
# d = c.casefold().strip()
# if (b == d) :
#     print("yes")
# else:
#     print("No")

# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x > y or x < y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# score = int(input("Score: "))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
# score = int(input("Score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
# x = int(input("What's x? "))
# if x % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")
# def main():
#  x = int(input("What's x? "))
#  if is_even(x):
#     print("Even")
#  else:
#     print("Odd")
# def is_even(n):
#   if n % 2 == 0 :
#     return True
#   else:
#     return False

# main()
# def main():
#  x = int(input("What's x? "))
#  if is_even(x):
#     print("Even")
#  else:
#     print("Odd")
# def is_even(n):
#   return True if n % 2 == 0 else False

# main()
# def main():
#  x = int(input("What's x? "))
#  if is_even(x):
#     print("Even")
#  else:
#     print("Odd")
# def is_even(n):
#   return n % 2 == 0

# main()
# name = input("What's your name? ")
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
# name = input("What's your name? ")
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
# name = input("What's your name? ")
# match name :
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
name = input("What's your name? ")
match name :
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

