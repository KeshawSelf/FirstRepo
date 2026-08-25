# count = 1

# while count <= 5 :
#     print("hello")
#     count += 1

# i = 1
# while i <= 5 :
#     print("hello", i)
#     i += 1

# i = 1
# while i <= 10 :
#     print(i)
#     i += 1

# print("Loop ended")

# i = 5
# while i >= 1:
#     print("hello", i)
#     i -= 1
# print("Loop Ended")

# a = 1
# while a <=100 :
#     print(a)
#     a += 1

# a = 100
# while a >= 1 :
#     print(a)
#     a -= 1

# a = int(input("Enter a number :"))
# b = 1
# while b <= 10 :
#     c = a*b
#     print(c)
#     b += 1

# i = 1
# n = int(input())
# while i <= 10 :
#     print(i*n)
#     i += 1

# a = 1
# while a <= 10 :
#     print([a*a])
#     a += 1

# heroes = ["ironman", "thor", "superman", "batman", "flash", "wonderwoman"]
# i = 0
# while i < len(heroes) :
#     print(heroes[i]) #traverse
#     i += 1

# t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# print(t)
# n = int(input("Find :"))
# i = 0
# while t[i] != n :
#     i += 1
# print("Found at idx", t.index(n))

# t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# print(t)
# x = int(input("Find :"))
# i = 0
# while i < len(t) :
#     if (t[i] == x):
#         print("Found at idx",i)
#     else :
#         print("Finding...")
#     i += 1

# i = 1
# while i <= 10 :
#     if (i == 7):
#         break #break the cycle
#     print(i)
#     i += 1

# i = 1
# while i <= 10 :
#     if (i == 7) :
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# i = 1
# while i <= 10 :
#     if (i%2 != 0) :
#       i += 1
#       continue
#     print(i)
#     i += 1

# list = ["hi", "i", "am", "best"]
# for el in list :
#     print(el)

# name = "PocoSelf"
# for letter in name :
#     if (letter == "S") :
#         print("S found")
#         break
#     print(letter)

# print("END")

# tup = (1, 2, 3, 4, 5, 6)
# for num in tup :
#     print(num)

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in num :
#     print(el)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# print(tup)
# x = int(input("Find :"))
# b = 0
# for a in tup:
#   if (a == x) :
#    print("found at index",b)
#    break #agr break lgaya to first found pe ruk jayega
#   b += 1

# seq = range(5) #range(start?, stop, step?)
# print(seq[0], seq[1], seq[2], seq[3], seq[4])
# print(seq)

# seq = range(10)
# for i in seq :
#   print(i)

# for i in range(5) : #range(stop)
#     print(i)

# for i in range(2, 10) : #range(start, stop)
#     print(i)

# for i in range(2, 10, 2) : #range(start, stop, step)
#     print(i)

# for i in range(101, 1, -1) :
#     print(i)

# n = int(input("Enter a number :"))
# for i in range(1, 11) :
#  print(n * i)

# for i in range(5) :
#     pass # baad me working code ke liye
# if  i > 2 :
#  pass
    
#  print("some useful work")

# n = int(input("Enter a number :"))
# sum = 0
# for i in range(1, n+1) :
#     sum += i
# print("total sum is :", sum)

# n = int(input("Enter a number :"))
# sum = 0
# i = 1
# while i <= n :
#     sum += i
#     i += 1
# print("total sum is :", sum)

# n = int(input("Enter a number :"))
# pro = 1
# for i in range(1, n+1) :
#     pro *= i
# print("factorial is :", pro)

n = int(input("Enter a number :"))
fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1
print("factorial =", fact)

#Done
