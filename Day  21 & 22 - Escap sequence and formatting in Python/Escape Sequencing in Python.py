"""
Escape Sequencing in Python: To print the single or double quotes the escape sequence or triple quotes is needed.
As the print with single or double quotes give syntax error.
"""

#EXAMPLE:
string1= '''Hello TechSorter'''
print("initial string", string1)

#Escap single quotes
string1 = 'I\'m Jyoti'
print("escap single quotes: ", string1)

#escap double quotes
string1 = "I'm \"Jyoti\""
print("escap double quotes: ", string1)

#print path with escape sequence
string1 = "c:\\jyoti\\program\\python"
print("print path: ", string1)

#print path with tab
string1 ="Hi \tTech sorter"
print("\nTab: ", string1)

#print new line
string1 = "Tech\nSorter"
print("\nnew line: ", string1)


#OUTPUT
"""
initial string Hello TechSorter
escap single quotes:  I'm Jyoti
escap double quotes:  I'm "Jyoti"
print path:  c:\jyoti\program\python

Tab:  Hi        Tech sorter

new line:  Tech
Sorter
"""
