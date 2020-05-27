from random import randint


class Dice():
    """Mimics a die for chance based games."""

    def __init__(self, sides_of_dice=6):
        """Initializes the dice class."""
        self.sides_of_dice = sides_of_dice

    def cast(self):
        """Mimics casting a dice, which returns a random number based
        on the number of sides the dice has."""

        x = randint(1, self.sides_of_dice)

        return x

    def update_num_sides(self, sides_of_dice=6):
        """User can update the number of sides the die has - default is 6."""

        self.sides_of_dice = sides_of_dice

