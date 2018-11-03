
### Tony Staunton
### Using a list within a dictionary

my_ordered_car = {
	'type' : 'standard four saloon',
	'extras' : ['alloy wheels', 'climate control', 'leather heated seats'],
}

# Print order summary

print("The car you ordered is a " + my_ordered_car['type'] + " with the following extras:")

for extra in my_ordered_car['extras']:
	print("\t" + extra)
