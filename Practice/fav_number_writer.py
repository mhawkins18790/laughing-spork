import json


def set_favorite_number():
    number = input("Please enter your favorite number: ")
    filename = 'fav_number.json'
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)


def get_favorite_number():
    filename = 'fav_number.json'
    with open(filename) as file_object:
        number = json.load(file_object)
        return number

