
### Tony Staunton
### Using a while loop to quit a prgram

prompt = "\nTo end this program enter 'q'."
prompt += "\nPlease enter your name: "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)
