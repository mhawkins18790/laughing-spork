import json

numbers = [2, 3, 4, 2, 5, 3, 2, 4, 3, 21, 45, 67, 7, 8, 544, 33, 2]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
