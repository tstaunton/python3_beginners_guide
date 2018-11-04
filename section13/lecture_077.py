
### Tony Staunton
### Using arbitrary keyword arguments

def create_passenger(*requests):
	"""Summarize passenger requests."""
	print("\nThis passenger has requested: ")
	for request in requests:
		print("- " + request)

create_passenger('window seat', 'seat near front of plane', 'breakfast')
