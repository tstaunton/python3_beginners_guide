
### Tony Staunton
### Read an entire file

with open('movies.txt') as file_object:
	contents = file_object.read()
	print(contents.strip())
