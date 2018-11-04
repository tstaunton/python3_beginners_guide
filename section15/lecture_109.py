
### Tony Staunton
### Reading a file line by line

filename = 'movies_line_by_line.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
