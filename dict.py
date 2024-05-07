            # ASSIGNMENT ON DICTIONARY
# wap to create following list
# a = ['a','b','c']
# b = ['d','e','f']

a = ['a','b','c']
b = ['d','e','f']
result = [a+b for a,b in zip(a,b)]
print(result)


# WAP to create following structure
#Sample lists: ["Black", "Red", "Maroon", "Yellow"],
#  ["#000000", "#FF0000", "#800000", "#FFFF00"]

colour_name = ["Black","Red","Maroon","yellow"]
colour_code = ["#000000","#FF0000","#800000","#FFFF00"]
result = [{"colour_name":colour_name[i],"colour_code":colour_code[i]}
for i in range(len(colour_name))]
print(result)

# WAP to find the subject with second highest marks in
#  {'eng': 100, 'hindi': 20, 'social': 45, 'punjab': 85}

marks = {'eng':100,'hindi':20,'social':45,'punjabi':85}
print("highest marks :",sorted(marks.values())[-1])
print("second highest marks :",sorted(marks.values())[-2])
