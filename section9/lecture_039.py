### 28 / 10 / 2016
### Tony Staunton
### Using the OR keyword to cjeck values in a list

# Names registered
registered_names = ['tony', 'frank', 'mary', 'peter']

username = input("Please enter the user name you would like to use.")

# Check to see if username is already taken
if username in registered_names:
    print("Sorry, username already taken.")
else:
    print("This username is available.")
