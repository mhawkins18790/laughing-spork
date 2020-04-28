import math
import random

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
if alien_0['speed'] == 'fast':
    x_increment = 3

# the new position of the alien is the old position plue the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0['points']
print(alien_0)

# for key, value in alien_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# alien_1 = {'color': 'green', 'points': 5}
# alien_2 = {'color': 'yellow', 'points': 10}
# alien_3 = {'color': 'red', 'points': 15}

# aliens = [alien_1, alien_2, alien_3]
# print(aliens)

aliens = []

for alien_number in range(30):
    random_number = random.randint(1, 4)
    if random_number == 1:
        new_alien = {'color': 'green', 'points': 5}
    elif random_number == 2:
        new_alien = {'color': 'yellow', 'points': 10}
    else:
        new_alien = {'color': 'red', 'points': 15}
    aliens.append(new_alien)

for alien in aliens[5:15]:
    print(alien)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'}
}

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
