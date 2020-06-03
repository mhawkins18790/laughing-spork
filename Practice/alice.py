filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print("No file exists with name " + filename + "!")
else:
    # count the number of words in the text
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
