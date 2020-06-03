from word_count import count_words, count_specific_word

filenames = ['alice.txt', 'siddhartha.txt', 'sherlock.txt', 'treasure.txt']

for filename in filenames:
    count_words(filename)
    count_specific_word(filename, 'grass')
