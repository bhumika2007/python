            #QUESTIONS ON LIST COMPREHENSION..

#Find all the numbers from 1 to 1000 that are divisible by 7 using list comprehension.

list = [i for i in range (1,1000) if i % 7 == 0]
print(list)

#Count the numbers of spaces in a string using list comprehension

a = "hello world python is very interesting"
spaces= [i for i in a if i == ' ']
print(len(spaces))
 
#Find the common numbers in two list without using tuple or set.

list1 = [1,2,3,4]  
list2=[2,3,4,5]
in_list2 =[x for x in list1 if x in list2]
print(in_list2)

#Find all the words in a string that are less than four letters

words = ["apple","mango","pear","pea","fig"]
words_in_string = [i for i in words if  len(i) < 4]
print(words_in_string)

#Produce a list of tuples consisting of only the matching number in these list .
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]
result = [(a,b)for a in list_a for b in list_b if a==b]
print(result)

#Given numbers = range(20),produce a list containing the word 'even' 
#if a number in numbers is even ,and the word 'odd' if the number is odd.

result = ['even' if i % 2 == 0 else 'odd' for i in range(20) ]
print(result)