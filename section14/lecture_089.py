
### Tony Staunon
### Creating our first class

class Book():
	"""A class to create a book."""

	def __init__(self, name, price, publisher):
		"""Initialize the name, price and publisher atrributes."""

		self.name = name
		self.price = price
		self.publisher = publisher

	def hardback(self):
		"""Simulate a hardback book."""
		print(self.name.title() + " is a hardback book.")

	def softback(self):
		"""Simulate a book being a softback book."""
		print(self.name.title() + " is a softback book.")

	def ebook(self):
		"""Simulate an ebook."""
		print(self.name.title() + " is an ebook.")

	def ebook_reader(self):
		"""Simulate an ebook reader."""
		print("Library: " + " "+ self.name.title() + ", $" + str(self.price) + ", " + self.publisher.title() + ".")

# Creating an instance of our book class.
my_book = Book('elon musk', 14.99, 'virgin books')
your_book = Book('the everything store', 9.99, 'virgin books')

# Calling our ebook_reader method
my_book.ebook_reader()
your_book.hardback()
