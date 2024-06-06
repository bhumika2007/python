            #   ASSIGNMENT
#Question 1:

# WAP Ask user to input a number and then month name corresponding to that number  

month_names = ["January","February","March","April","May","June","July","August",
               "September","October","November","December"] 
 
number = int(input("Enter a number(1-12):"))

if 1<= number <= 12:
   print("The month corresponding to that number is:",
         month_names[number-1])
else:
   print("invalid number.")   

#Question 2:

#WAP Ask user to input 2 number,tell the followings
#1.Both number are equal or not
#2.Which is Bigger in both
#3.Either First NUmber is smaller or equal to Second Number
#4.Print your first name 5 times is first number is greather than second 
#and print your surname 3 times if 1st no is less than second

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

# Both number are equal or not

if num_1 == num_2 :
   print(" Both numbers are equal.")
else :
   print("Both numbers are not equal.") 

#Which is Bigger in both 

if num_1 > num_2 :
   print("First number is Bigger.") 
elif num_2 > num_1:
  print("Second number is Bigger.") 
else :
   print("Both are equal.") 

# Either First Number is smaller or equal to Second Number

if num_1 <= num_2:
   print("First Number is smaller or equal to Second Number")
else:
   print("First Number is greater or equal to Second Number") 

# Print your first name 5 times is first number is greather than second and 
# print your surname 3 times if 1st no is less than second..

if num_1 > num_2:
   print("Your first name " * 5) 
elif num_1 < num_2:
   print("Your surname " * 3) 

#Question 3:

# Using User input ask user to input 2 string and tell followings
#1.using == tell both string equal or not
#2.using is operator tell both equal or not         
    
string1 = input("Enter the first string") 
string2 = input("Enter the second string") 

if string1 == string2:
   print("Using '==' : Both strings are equal") 
else :
   print("Using '==': Both strings are not  equal") 

if string1 is string2:
   print("Using 'is' : Both strings are not equal")  
else:
   print("Using 'is': Both strings are  equal")   

#Question 4:

#Ask user to input 2 string and convert it into numbers and using is op
# tell both are equal or not 

num1 = int(input("Enter first number as a string:"))    
num2 = int(input("Enter second number as a string:"))   
if num1 is num2:
   print("Using 'is' : Both numbers  are equal") 
else:
   print("Using 'is' : Both numbers are not equal")    
            
        
#Question 5:
#Create a menu drive program to peform the calculator as below OP	 
# Welcome to Sada Calculator
# Select your choice

# 1. Addition
# 2. Substration
# 3. Division
# 4. Multiplication
# 5. Power
# 6. Reminder

print("Welcome to Sada Calculator")
print("Select your choice")
print()
print("1. Addition")
print("2. Substration")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Reminder")
choice = int(input(" ---> "))
if choice == 1:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1+num_2
    print("sum is",result)

elif choice == 2:
   num_1 = float(input("Enter first number:"))
   num_2 = float(input("Enter second number:"))
   result = num_1-num_2
   print("difference is",result)

elif choice == 3:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    if num_2 != 0:
     result = num_1 / num_2
     print("division is",result)  
    else :
     print("Cannot divide by zero")
elif choice == 4:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1*num_2
    print("Multiplication  is",result)  
elif choice == 5:
    num_1 = float(input("Enter the base  number:"))
    num_2 = float(input("Enter exponent  number:"))
    result = num_1**num_2
    print("power is",result)
elif choice == 6:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1%num_2
else :
   print("invalid choices..")  

#Question 6:

#Ask User to input a Number and with + or - and perform followings OP

number =int(input("Enter a number ")) 
operations = input("Enter OP from + or -")
if operations == "+":
 result = [i for i in range(0,number)]
elif operations == "-" :
 result = [i for i in range(number,0,-1)]
else :
  result ="invalid number"
print(result) 

#Question 7:

#Ask user to input a number and tell all even number upto that number.

user_num = int(input("Enter a number:"))
for i in range(2,user_num+1):
  if i % 2 == 0:
   print(i)

