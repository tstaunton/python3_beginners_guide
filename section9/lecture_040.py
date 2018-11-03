### 28 / 10 / 2016
### Tony Staunton
### Checking if a value is not in a list

# Admin users
admin_users = ['tony', 'frank']

# Ask for username
username = input("Please enter your username?")

# Check if user is an admin user
if username not in admin_users:
    print("You do not have access.")
else:
    print("Access granted.")
