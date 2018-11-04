
### Tony Staunton
### Using positional and arbitrary keyword arguments

def assign_seat(seat, *requests):
	"""Assign a seat and requests to a passenger."""
	print("\nAssign seat number " + str(seat) + " the following passenger requests: ")
	for request in requests:
		print("- " + request)

assign_seat(36, 'window seat')
