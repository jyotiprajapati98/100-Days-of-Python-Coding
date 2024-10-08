def duplicate_characters(string):
	chars = {}
	for char in string:
		if char not in chars:
			chars[char] = 1
		else:
			chars[char] += 1

	duplicates = []
	
	for char, count in chars.items():
		if count > 1:
			duplicates.append(char)

	return duplicates

print(duplicate_characters("Hello Google"))

#OUTPUT
"""
['e', 'l', 'o']


...Program finished with exit code 0
Press ENTER to exit console.

"""
