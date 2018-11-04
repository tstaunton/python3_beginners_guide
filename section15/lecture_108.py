
### Tony Staunton
### File paths

file_path = '/Users/tonystaunton/Desktop/Code examples/Files/text_files/copy_of_movies.txt'

with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.strip())
