
### Tony Staunton
### The else block

print("Please enter two numbers to be divided? ")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break

	second_number = input("Second Number: ")
	if second_number == 'q':
		break

	answer = int(first_number) / int(second_number)
	print(answer)
