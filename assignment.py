# Question 1.

# Write a python program that takes two strings input 's1' and 's2' from user ,
# and return a string containing the appear in both strings.

s1 = input("Enter the first string ")
s2 = input("Enter the second string ")
common = ""
for char in s1:
 if char in s2 and char not in common:
     common+=char
print(common)

# Question 2.

# Write a python program that takes sentence as a input and
# return the numbers of words in the sentence.words are separated by spaces.

sentence = input("Enter a sentence:") 
print(len(sentence.split()))

# Question 3.

# Write a python program that checks if two string 's1' and 's2' 
# are rotations of each other.

def are_rotations(s1,s2):
    if len(s1) != len(s2):
        return False
    s3 = s1 +s1
    if s2 in s3 :
        return True
    else:
        return False
s1 = input("Enter the first string")  
s2 = input("Enter the second string")  

if are_rotations(s1,s2):
    print("they are rotations of each other..")
else:
    print("they are not rotations of each other..")    

#Question 4.

# Write a python program that takes a string as input and returns the character
#that appears most frequently.if there are multiple characters with 
# the same maximum frequency return any one of them.

str = input("Enter a string:")
l = list (str)
print(l)
freq = [l.count(ele)for ele in l]
print(freq)
d = dict(zip(l,freq))
print(d)

# Question 5.

# Write a python program that converts a string from  snake_case to camel case.

snake_case = input("Enter a snake case string")
a = snake_case.split("_")
camel_case = a[0] +''.join(x.title() for x in a[1:])
print(camel_case)