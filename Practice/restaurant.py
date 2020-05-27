class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialization including restaurant's name and style."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(self.restaurant_name + " is a " +
              self.cuisine_type + " restaurant.")

    def set_numbrer_served(self, set_number):
        """Allows user to set the number of people served in the restaurant."""
        if set_number >= 0:
            self.number_served = set_number

    def increment_number_served(self, increment_number):
        """Allows user to add people to the number served figure."""
        if increment_number >= 0:
            self.number_served += increment_number
