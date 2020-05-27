from dice import Dice

my_dice = Dice(8)

print(str(my_dice.cast()))

for x in range(6):
    print(str(my_dice.cast()))

my_dice.update_num_sides(20)

for x in range(6):
    print(str(my_dice.cast()))
