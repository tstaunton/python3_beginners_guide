
### Tony Staunton
### Editing & deleting values in a dictionary

terms = {'integer' : 'Is a number that contains a decimal place.', 'string' : 'a sequence of characters.'}

terms['integer'] = 'A whole number'

# Delete statement
# del terms['integer']
# print(terms)


print(terms.get('integer'))
