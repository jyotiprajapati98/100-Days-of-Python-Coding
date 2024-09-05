string1 = "|{:<10}|{:^10}|{:>10}|".format('Hello','World', 'Jinny')

print("string after left, center, and right alingment: ", string1)

string1 = "\n{0:^16} was founded in {1:<4}!".format("Hello", 2024)
print(string1)

#OUTPUT
"""
string after left, center, and right alingment:  |Hello     |  World   |     Jinny|

     Hello       was founded in 2024!
"""
