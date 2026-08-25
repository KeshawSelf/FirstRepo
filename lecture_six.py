# def sum(a, b):
#      s = a + b
#      print(s)
#      return s
     
     

# # a = int(input("1st number : "))
# # b = int(input("2nd number : "))
# # sum(a, b)
# sum(2, 3)
# sum(4, 7)
# sum(9, 11)


# a = int(input("1st number : "))
# b = int(input("2nd number : "))
# def calc_sum(a, b) :
#     return a + b
# sum = calc_sum(a, b)
# print("Sum is :",sum)

# def print_hello() :
#     print("Hello")

# output = print_hello()
# print(output)


# a = 2
# b = 5
# c = 8
# def avg(a, b, c) :
#     return (a + b + c)/3 

# avg = avg(a, b, c)
# print(avg)
# print(type(avg))

# def calc_avg(a, b, c) :
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# a = int(input("1st number : "))
# b = int(input("2nd number : "))
# c = int(input("3rd number : "))
# calc_avg(a, b, c)

# print("apnacollege","shradhakhapra")
# print("apnacollege")
# print("shradhakhapra")
# print("apnacollege", end = "$")
# print("shradhakhapra")

# def multi(a, b = 2) :
#     print(a * b)
#     return a * b

# multi(4)

# def multi(a = 3, b) :
#     print(a * b)
#     return a * b

# multi(4)

# marks = [20, 25, 20, 35, 46, 58, 24]
# cities = ["delhi", "pune", "indore", "banglore"]

# def some_len(something) :
#     print(len(something))

# some_len(marks)
# some_len(cities)

# marks = [20, 25, 20, 35, 46, 58, 24]
# cities = ["delhi", "pune", "indore", "banglore"]

# def some_list(something) :
#     for item in something :
#      print(item, end=" ")

# some_list(cities)
# print()
# some_list(marks)

# def cal_fact(n) :
#     fact = 1
#     for i in range (1, n+1) :
#         fact *= i
#     print(fact)
# cal_fact(int(input("Enter a number : ")))

# def converter(usd_val) :
#     inr_val = usd_val * 94
#     print(usd_val,"USD =",inr_val,"INR")
# converter(2)

# n = int(input("Enter a number : "))
# def odd_even(n) :
#     if (n%2 == 0):
#         print("EVEN")
#     if (n%2 != 0) :
#         print("ODD")

# odd_even(n)

#Recursive Function
# def show(n) :
#     if (n == 0) :
#         return
#     print(n)
#     show(n-1)
#     print("END")
# n = int(input("Enter a number : "))
# show(n)

# def fact(n) :
#    if (n == 0 or n == 1) :
#       return 1
#    return fact(n-1) * n
# print(fact(6))


# def sum(n) :
#     k = 0
#     for i in range (1, n+1) :
#        k += i
#     print(k)

# sum(3)

# def calc_sum(n) :
#     if (n == 0) :
#         return 0
#     return calc_sum(n-1)+n

# sum = calc_sum(10)
# print(sum)

# marks = ["math", "phy", "chem", "bio"]
# def marks_list(n) :
#     for n in range(0, len(marks)) :
#      print(marks[n])
#     n += 1

# marks_list(1)

# def print_list(list, idx=0) :
#     if (idx == len(list)) :
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["mango", "litchi", "apple", "banana", "kiwi"]
# print_list(fruits)

#Done
