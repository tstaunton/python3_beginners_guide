
### Tony Saunton
### Working with while loops and lists

# create a list of unverified users
unconfirmed_users = ['tony', 'frank', 'mary']

# An empty list to hold confirmed users
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
