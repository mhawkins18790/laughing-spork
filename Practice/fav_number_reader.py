from fav_number_writer import set_favorite_number, get_favorite_number

try:
    number = get_favorite_number()
except FileNotFoundError:
    set_favorite_number()
    number = get_favorite_number()


print("Your favorite number is " + str(number) + "!")
