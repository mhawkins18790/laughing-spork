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


my_restaurant = Restaurant("Matt's", "pizza")

my_restaurant.describe_restaurant()

your_restaurant = Restaurant("Tim's Table", "American food")
Laur_restaurant = Restaurant("Laur's", "burnt food")

your_restaurant.describe_restaurant()
Laur_restaurant.describe_restaurant()


class User():

    def __init__(self, first_name, last_name, age=0, height=0, weight=0, login_attempts=0):
        """Establishes a new User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = login_attempts

    def calc_BMI(self):
        BMI = 0
        if (self.height > 0 and self.weight > 0):
            BMI = 703 * (self.weight / (self.height ** 2))

        return BMI

    def describe_user(self):
        """Print a statement about the user"""
        age_str = "--"
        height_str = "--"
        weight_str = "--"
        BMI_str = "--"

        if (self.age > 0):
            age_str = self.first_name.title() + "'s age is " + str(self.age)

        if (self.height > 0):
            height_str = self.first_name.title() + "'s height is " + \
                str(self.height)

        if (self.weight > 0):
            weight_str = self.first_name.title() + "'s weight is " + \
                str(self.weight)

        if (self.calc_BMI() > 0):
            BMI_str = self.first_name.title() + "'s BMI is " + \
                str(self.calc_BMI())

        print("\nDescription: \nName: " + self.first_name.title() +
              " " + self.last_name.title() + "\nAge: " + age_str +
              "\nHeight: " + height_str + "\nWeight: " + weight_str +
              "\nBMI: " + BMI_str)

    def login_attempt(self):
        """Adds one login attempt"""
        self.login_attempts += 1

    def reset_login_attempt(self):
        """Resets number of attempts to zero."""
        self.login_attempts = 0


my_user = User("Matt", "Hawkins")

my_user.describe_user()

my_user_2 = User("Matt", "Hawkins", 29, 76, 282)

my_user_2.describe_user()

for x in range(6):
    my_user.login_attempt()

print(str(my_user.login_attempts))

my_user.reset_login_attempt()

print(str(my_user.login_attempts))

# my_int = my_user_2.calc_BMI()

# print(str(my_int))


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


bigone = IceCreamStand('The Big One', "Ice Cream")
bigone = flavors = ['vanilla', 'chocolate', 'black cherry']
