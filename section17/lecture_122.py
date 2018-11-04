
### Tony Staunton
### Working with json.load() function

import json

filename = 'phone_number.json'
with open(filename) as file_object:
	phone_numbers = json.load(file_object)

print(phone_numbers)
