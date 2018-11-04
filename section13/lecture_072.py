
### Tony Staunton
### using a while loop in a function


def get_formatted_name(first_name, last_name):
	"""Return a full name neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
        print("\nWhat is your name?")
        print("(Press 'q' at any time to quit this program.)")

        first_name = input("First Name: ")
        if first_name == 'q':
                break

        last_name = input("Last Name: ")
        if last_name == 'q':
                break

        formatted_name = get_formatted_name(first_name, last_name)
        print("\nHello, " + formatted_name + "!")
