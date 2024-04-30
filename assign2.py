#1.write a python function to reverse a string

s = "Hello"
reverse = s[::-1]
print(reverse)

#2.write a python function to check number is palidrome or not

a =input("Enter the string")
is_palidrome = a == a[::-1]
print(is_palidrome)

#3.write a python program to count number of vowels in string

a = "bhumika"
vowels ="a,e,i,o,u,A,E,I,O,U"
count = 0
for char in a:
    if char in vowels:
        count+=1
        print(count) 

#4.wap to remove all whitespaces in a string

a = "  hello World"
no_whitespaces = ""
for char in a:
    if char !=' ':
     no_whitespaces +=char 
print(no_whitespaces)

#5.wap to swap case in a string

a= "Hello world"
swap_case = a.swapcase()
print(swap_case)

#6.wap to check if a string is an anagram of another string

s1 = "abcd"
s2 ="dabc"
is_anagram = sorted (s1)==sorted(s2)
print(is_anagram)

#7.wap to convert a string to camel case

s = "hello_world"
camel_case = ""
capitialize_next = False
for char in s:
    if char == '_':
        capitialize_next = True
    elif capitialize_next:
        camel_case +=char.upper()
        capitialize_next= False
    else:
        camel_case +=char 
        print(camel_case)

#8.wap to check if a string contains only digit

s = "123455"
contains_only_digit = s.isdigit()
print(contains_only_digit)



