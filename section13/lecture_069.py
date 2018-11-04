
### Tony Staunton
### Returning a value in a function

def formatted_name(first_name, last_name):
	"""Return a formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

teacher = formatted_name('tony', 'staunton')
print(teacher)

def get_formatted_username(email_address):
	"""Return a formatted username"""
	username = email_address.strip()
	return username
user = get_formatted_username('tony@example.com      ')
print(user)
