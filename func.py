# Recursion 

# def drive():
#     age= int(input("Enter Your age "))
#     if age>18 and age<100:
#         print("You can drive")
#     else:
#         print("Cannot drive")
#         drive()

# drive()

# import math

# print(math.factorial(5))
# print(math.sqrt(112))
# print(math.pow(1,4))


# keyword

def keyArb(**kwargs):
    print(kwargs)

# keyArb(a=10,b=20)

#lambda ---
#single line functions
# def sums(a,b):
#     return a+b
# def sums(a,b):
#     # return a+b
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"

# fun= lambda a,b: a+b
# print(fun(12,23))
#lambda parameters: statement-1 condition-1 condition-2 statement-2
fun= lambda a:print("Even") if a%2==0 else print("Odd")

print(fun(11))

