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
# name = input("What's your name? ")
# match name :
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1
# for i in [0, 1, 2]:
#     print("meow")
# for _ in range(3):
#     print("meow")
# print("meow\n" * 3, end = "")
# print("meow" * 2, sep = "_")
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
    # if n > 0:
    #     break
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")
# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         x = int(input("What's n? "))
#         if x > 0:
#             break
#     return x

# def meow(n):
#     for _ in range(n):
#         print("meow")
    

# main()
# def main():
#     meow(get_number())


# def get_number():
#     while True:
#         x = int(input("What's n? "))
#         if x > 0:
#             return x


# def meow(n):
#     for _ in range(n):
#         print("meow")


# main()
# students = ["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i + 1, students[i])
# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
# for student in students:
#     print(student, students[student], sep=", ")
# print(type(students[student]))

# students = [
#     {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
#     {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
#     {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell terrier"},
#     {"name" : "Draco", "house" : "Slytherin", "patronus" : None},

# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep = ", ")
# x = 50
# print("Amount Due:",x)
# while x > 0:
#   y = int(input("Insert Coin:"))
#   if y == 25 or y == 10 or y == 5:
#     if x-y > 0:
#      print("Amount Due:",x-y)
#      x = x-y
#     elif x-y <= 0:
#         print("Change Owed:",y-x)
#         break
#   else:
#     print("Amount Due:",x)

# x = 50
# while x > 0:
#     print("Amount Due:",x)
#     y = int(input("Insert Coin: "))
#     if y == 25 or y == 10 or y == 5:
#         x = x - y
# if x <= 0:
#     print("Change Owed:",-x)

# x = input("Input: ")
# for y in x:
#     if y=="a" or y=="e" or y=="i" or y=="o" or y=="u" or y=="A" or y=="E" or y=="I" or y=="O" or y=="U":
#         z = x.replace(y,"")
#         x = z

# print(z)
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     s = str(s)
#     for i in range(len(s)):
#        if s[i].isdigit() and s[i+1].isalpha():
#           return False
#        else:
#            return True
      



# main()
# def main():
# s = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
# s = str(s)
    # if 2 <= len(s) <= 6:
    #     if s.isalpha():
    #         return True
    #     elif s.isalnum() and s[0].isalpha() and s[1].isalpha():
# for i in s:
#     if i.isdigit():
#      n = s.index(i)
#      new = s[n:]
#      if new[0] == "0":
#         print("yes")
# main()
try:
    x = int(input("What's x? "))
    
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")