"""
An example of writing to a file
"""

import os

# Init the my_dir
my_dir = os.path.dirname(os.path.realpath(__file__))


my_filename = 'fred.txt'


# read lines of file
with open(my_dir + '/' + my_filename, 'r') as my_file:
	for line in my_file:
		print(line)

exit(0)

# read whole file
with open(my_dir + '/' + my_filename, 'r') as my_file:
	stuff = my_file.read()
print(stuff)



# Read lines
with open(my_dir + '/' + my_filename, 'r') as my_file:
	lines = my_file.readlines()
print(lines)


# read words

with open(my_dir + '/' + my_filename, 'r') as my_file:
	words = my_file.read().split()
print(words)





# Write a file
outfilename = 'fred.out.txt'

with open(my_dir +'/' + outfilename, 'w') as outfile:
	for word in words :
		outfile.write(word)


		# outfile.write(word + ', ')
