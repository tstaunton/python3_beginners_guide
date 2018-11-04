
### Tony Staunton
### Returning a Dictionary

def build_book(name, author, publisher):
	"""Create a dictionary of book information."""
	book = {'name' : name, 'author' : author, 'publisher' : publisher}
	return book

my_book = build_book('elon musk', 'ashlee vance', 'virgin books')
print(my_book)
