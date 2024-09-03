#update the entire string 
str1 = "Hello TechSorter"
print("Initial String : ", str1)

str1 = "Hy, TechSorter" #assing the string value to the same name
print("updated String : ", str1)


#delete a character from the String
"""
str2 = "100 days of Python"
print("Initial String: ", str2)
del str2[3] #Tthows error because string object does't support the del keyword
print("String after deleting the 3rd Index character: ", str2)

"""
#delete character using slice
str2 = "100 days of Python"
print("Initial String: ", str2)
str2_1 = str2[0:2] + str2[3:] # + is use to concatenate
print("String after deleting the 2nd Index character: ", str2_1)


#OUTPUT
'''
Initial String :  Hello TechSorter
updated String :  Hy, TechSorter
Initial String:  100 days of Python
String after deleting the 2nd Index character:  10 days of Python
'''
