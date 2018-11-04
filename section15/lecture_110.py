
### Tony Staunton
### Making a list from a file

filename = 'movies_line_by_line.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())
