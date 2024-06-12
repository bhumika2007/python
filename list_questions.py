        #LIST QUESTIONS
# Given a list of numbers. write a program to turn every item of a list into its square.
Given_list = [2, 5, 7, 9]
result = [x**2 for x in Given_list]
print(result)

# Concatenate two lists in the following order
Given_list1 = ["hello", "o7"]    
Given_list2 = ["world", "services"]
concatenate_list = [x + ' ' + y for x in Given_list1 for y in Given_list2]
print(concatenate_list)


# Add 10 to list after a 600

Given_list= [10, 20, [300, 400, [5000, 600], 500], 30, 50]
Given_list[2][2].append(10)
print("modified list :",Given_list)


# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.
Given_list = [5, 10, 15, 20, 25, 30, 20, 35]
c = Given_list.index(20)
Given_list.remove(20)
Given_list.insert(c,200)
print(Given_list)

# wap to input elements of the list from the user and print the smallest and greatest 
# element of the list.
lst =[]
num = int (input('How many numbers:'))
for i in range(num) :
    numbers = int (input("Enter numbers:"))
    lst.append(numbers)
a = max(lst)
b = min(lst)
print(a)
print(b)

# wap to print duplicate from a list of integers.
input = [10,20,30,20,20,30,40,50,-20,60,60,-21,-20]
seen = set()
duplicate = set()
for i in input :
    if i in seen :
        duplicate.add(i)
    seen.add(i)
if duplicate:
    print(duplicate)  
else:
    print("No duplicate found in the list")   

# wap to find second largest number in the list .
list = [60,90,20,10,50,45,30,70,32,20]
l = max(list)
final_output = list.remove(l)
d = max(list)
print(d)

# wap to count number of positive, negative number and strings in the list.
list = [3,-1,5,-8,2 ,7,-4,'cherry','banana']
positive_number = 0
negative_number = 0
string = 0
for i in list:
    if isinstance (i ,(int,float)) :
        if i > 0:
         positive_number += 1
        elif  i<0:
         negative_number += 1
    elif isinstance (i,str):
        string +=1
print(positive_number)  
print(negative_number) 
print(string)     

    




    
    

