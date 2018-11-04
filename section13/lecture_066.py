
### Tony Staunton
### Passing info to a function

# Creating our function
def book_description(book_type, author_name):
	"""Display book informatio"""
	print("\nThis book is " + book_type + ".")
	print("The author of this book is " + author_name.title() + ".")

book_description('non-fiction', 'ashlee vance')
book_description('fiction', 'dan brown')
