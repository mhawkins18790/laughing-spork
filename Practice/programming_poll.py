filename = 'pollResponse.txt'

responses = []

while True:
    pollQuestion = input("What do you like about programming? ")
    responses.append(pollQuestion)

    continueQuestion = input("Would you like to continue answering? (y/n) ")
    if continueQuestion == 'n':
        break

with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write(response + "\n")
