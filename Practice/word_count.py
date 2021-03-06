def count_words(filename):
    """Count the approximate number of words in a text file."""
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


def count_specific_word(filename, specific_word):
    """Count the number of instances a specific word appears in text."""
    try:
        with open(filename, encoding='utf-8') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("No file exists with name " + filename + "!")
    else:
        # count the number of words in the text
        words = contents
        instances = words.lower().count(specific_word)
        print("The file " + filename + " has about " +
              str(instances) + " of the word " + specific_word + ".")
