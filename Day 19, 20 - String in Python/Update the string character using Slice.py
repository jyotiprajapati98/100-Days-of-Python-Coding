"""
This is another way to update the string characters in python as string is unmutable in Python. 
Slicing allows us to update the characters, slice the character before you want to update then,
add the new character and finally add the other part of string.
"""

#EXAMPLE
#Initial string 
string1 = "Welcome to Techsorter"
print("Initial string: ", string1)

string2 = string1[0:2] + 'J' + string1[3:]
print(string2)

#OUTPUT
"""
Initial string:  Welcome to Techsorter
WeJcome to Techsorter
"""
