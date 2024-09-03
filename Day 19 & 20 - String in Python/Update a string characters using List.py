"""
Deleting and Updating from a String:
NOTE: In python string updation is not allowed directly because item assignment or character deletion from string is not supported by the Python.
Yes, we can completely delete the string using built-in keyword del.
a) Updating a string character: There is two possible ways to update the characters of the String:
i) Using Python List: Convert the String into list then update the characters as the list is mutable this operation can be performed.
"""

#Program
#Updating a string character
string1 = "Hello, Jyoti"

print("string ", string1)
#convert into list
strList = list(string1)
print("string in List: ", strList)

#update the charecter
strList[0] = 'Y'
print("updated string in List: ", strList)

#list to string
string2 = "".join(strList)
print("updated string: ", string2)

#OUTPUT
"""
string  Hello, Jyoti
string in List:  ['H', 'e', 'l', 'l', 'o', ',', ' ', 'J', 'y', 'o', 't', 'i']
updated string in List:  ['Y', 'e', 'l', 'l', 'o', ',', ' ', 'J', 'y', 'o', 't', 'i']
updated string:  Yello, Jyoti
"""
