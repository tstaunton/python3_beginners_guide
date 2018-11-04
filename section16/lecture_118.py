
### Tony Staunton
### FileNotFoundError

filename = 'tony.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	message = "Sorry, the file " + filename + " cannot be found."
	print(message)
