### 24 / 10 / 2016
### Author: Tony Staunton
### Using the pop() method

subcribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
print(subcribers)

popped_subsriber = subcribers.pop() 

print(subcribers)

print(popped_subsriber)

subcribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
first_subscriber = subcribers.pop(0)

print("Your first subscriber was " + first_subscriber + ".")

subcribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
print(subcribers)

subcribers.remove('john@example.com')

print(subcribers)

subcribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
subscribed_by_mistake = 'tony@example.com'
subcribers.remove(subscribed_by_mistake)

print(subcribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")



