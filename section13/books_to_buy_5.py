### 010 / 11 / 2016
### Tony Staunton
### Our module / Importing an entire module

def books_available(*books):
	"""Show a list of books available to buy."""
	for book in books:
		books_in_stock = "The following title is available to buy " + book.title() + "."
		print(books_in_stock)

def book_description(author_name, book_type="non-fiction"):
	"""Display book information."""

	print("\nThis is a " + book_type + " book.")
	print("The author of this book is " + author_name.title() + ".")
