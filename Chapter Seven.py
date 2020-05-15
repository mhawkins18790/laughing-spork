# message = input("Tell me something, and I will repeat it back to you")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# active = True

# message = ""
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

prompt = "\nPlease enter in your pizza topping:"
prompt += "\n(Enter 'quit' to finish your order"

active = True
message = ""

while active:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print("We will add " + message + " to the pizza")
