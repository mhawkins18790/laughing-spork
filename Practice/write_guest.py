filename = 'guest.txt'

while True:
    guest_name = input("Please enter your name. Type 'quit' to stop ")
    if guest_name == 'quit':
        break
    else:

        with open(filename, 'a') as file_object:
            file_object.write(guest_name + "\n")
        print("Hi " + guest_name + ", you've been added to the list.")
