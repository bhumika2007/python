# Write a python program that handle a ZeroDivisionError exception 
# when dividing a number by zero .
try:
 num1 = int(input("Enter the first number:"))
 num2= int(input("Enter the second number:"))
 result = num1/num2
 print(result)
except ZeroDivisionError as e:
    print (e)
# Write a python program that prompts the user to input an integer and
# raises a ValueError exception if the input is not a valid integer.

try:
 num1 = int(input("Enter the first number:"))
 num2= int(input("Enter the second number:"))
 result = num1/num2
 print(result)
except ZeroDivisionError as e:
    print (e)
except ValueError:
    print("Error:please enter valid interger values.")
finally:
    print("I'm always executed")

#Write a python program that opens a file and handles a FileNotFoundError
#exception if the file does not exist.
try:
  f =open("example.txt",'r')
  text = f.read()
  print(text)
  f.close()
except FileNotFoundError :
  print("error:file not found..")

#Write a Python program that prompts the user to input two numbers and 
#raises a TypeError exception if the inputs are not numerical.
try:
 num1 =float(input("Enter the first number:"))
 num2 =input("Enter the second number:")
 result = num1 + num2
 print(result)
except ValueError as e:
  print("value error.")
except TypeError :
   print("Error:Please enter valid numbers.") 

# Write a Python program that creates a directory named "MyFiles";
# if doesn't already exist.Within "MyFiles",create three files:"file1.txt",
# "file2.txt",and file3.txt.Write Hello World! into each file.

import os
directory ="MyFiles"
files = ["file1.txt","file2.txt","file3.txt"]
content = "Hello,World!"
if not os.path.exists(directory):
    os.makedirs(directory)
for file_name in files:
    file_path = os.path.join(directory ,file_name)
    with open (file_path,'w') as file:
        file.write(content)
print("files created and content written successfully.")
#Write a Python program that deletes all files 
#in a specified directory with a given file extension.
import os 
directory = "MyFiles"
extension = ".txt"
if not os.path.exists(directory):
    print(f"the directory{directory} does not exist.")
else:
    for filename in os.listdir(directory):
     file_path = os.path.join(directory,filename)
     if os.path.isfile(file_path) and filename.endswith(extension):
        try:
           os.remove(file_path)
           print(f"deleted{file_path}")
        except Exception as e:
         print(e)


