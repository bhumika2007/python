# write a function that checks whether a passed string is palidrome or not.

def is_palidrome(s):
    return s ==s[::-1]
name = "radar"
if is_palidrome(name):
    print("Your String is palidrome")
else:
    print("Your String is not palidrome")

# write a python program to sort a list of tuples using lambda.

l1 = [("english",88),("social science",82),("science",90),("math",97)]
c =sorted(l1,key = lambda a :a[0]) #sorted the first element of the tuple list
d =sorted(l1,key = lambda a :a[1]) #sorted the second element of the tuple list
print(c)
print(d)

# write a python program to square the elements of  list using the map() function.

def square(a):
    return a**2
a =map(square,[2,5,7,9])
print (list(a))

#given a list of strings write a python program to capitalize the first letter 
# of each string using the map() function

bb= ["hello","welcome","in","python","language"]
def capitalize(bb):
    return bb.capitalize()
new = list(map(capitalize,bb))
print(new)

# write a python function that takes a list of numbers and return a new list 
# containing the square root of those numbers using the map() function.

import math
cc = [1,4,9,16,25]
def square_roots(cc):
    return math.sqrt(cc)
new= list(map(square_roots,cc))
print(new)
  
# Write a Program to check if a number is prime or not

num = int(input("Enter the number :"))
count = 0
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
            
            count += 1
            break
    if count:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

# wap to print fibonacci series up to n terms using lambda function.
fibo=lambda n,a =0,b=1:[] if n==0 else[a]+fibo(n-1,b,a+b)
n = int(input("Enter any value for n: ",))
print("fibonacci series up to",n,":")
print(fibo(n))
