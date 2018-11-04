
### Tony Staunton
### Using arbitrary keyword arguments

def seat_profile(first, last, **passenger_info):
	"""Build a dictionary containing all passenger informtation"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in passenger_info.items():
		profile[key] = value
	return profile

passenger_profile = seat_profile('tony', 'staunton', seat_number=36, breakfast_ordered='yes')

print(passenger_profile)
