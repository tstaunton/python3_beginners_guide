
### Tony Staunton
### Creating a new ereader class

class Ereader():
	"""A class to repesent an ereader."""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize the attributes to describe an ereader."""
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery = battery
		self.screen_type = screen_type

	def get_ereader_name(self):
		"""Return a formatted descriptive name for our ereader."""
		long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
		return long_name.title()

my_new_ereader = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustable Backlight', 'Several Months of Battery Life', '300 dpi')
print(my_new_ereader.get_ereader_name())
