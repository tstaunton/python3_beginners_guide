
### Tony Staunton
### Modifing a list in a function

def passengers(not_checked_in, checked_in):
	"""Simulate passengaers who are not checked in."""

	while not_checked_in:
		current_passenger = not_checked_in.pop()

		# Simulate a passenger checking in.
		print("Checking in passenger: " + current_passenger)
		checked_in.append(current_passenger)

def show_checked_in_passengers(checked_in):
	"""Show all the passengers who have checked in."""
	print("\nThe following passengers have been checked in.")
	for passengers in checked_in:
		print(passengers)

not_checked_in = ["Tony Staunton"]
checked_in = []

passengers(not_checked_in, checked_in)
show_checked_in_passengers(checked_in)
