# x = float(input("Enter: "))
# print(f"you entered: {x:.1f}")
# a = "hello, there"
# if a.endswith("there"):
#     print("true")
# else:
#     print("false")
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(1,n+1):
        print("#" * i)

main()