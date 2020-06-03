import json

filename = 'numbers.json'
with open(filename) as file_object:
    contents = json.load(file_object)

print(contents)
