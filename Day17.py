class Restaurant:
    def __init__(self, restaurant_info, cuisine_type, set_number_served, login_attempt=0, number_served=0,):
        """format the properties"""
        self.restaurant_info = restaurant_info
        self.cuisine_type = cuisine_type
        self.set_number_served = set_number_served
        self.number_served = number_served
        self.login_attempt = login_attempt

    def describe_restaurant(self):
        """Tell customers this cafe is about what"""
        print(f"The restaurant's name is {self.restaurant_info}")
        print(f"The restaurant is famous for {self.cuisine_type}")

    def open_restrant(self):
        """Tell customers this cafe is open"""
        print('This restrant is open now')

    def people(self):
        """Tell people how many people we served"""
        print(f"We have served {self.number_served} people")

    def update_people(self, people):
        """Update the numbers of people we served"""
        self.number_served += people
        print(f"There's {self.number_served} people here today")

    def set_number_served(self, set_number_served):
        """This is for user to set the amount of the people we can serve
            I think this is bullshit and useless tho"""
        print(f"This is how many people you've served{set_number_served}")

    def increment_number_served(self, addons):
        """This is for user to add the amount of the people we can serve"""
        self.number_served += addons


now = Restaurant('test', 'test', 12)
now.update_people(10)
# now.set_number_served(100)
now.increment_number_served(100)


class User:
    def __init__(self, first_name, last_name, login_attempt=0):
        """format attributeself"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = login_attempt

    def describe_user(self):
        """Give out the info we have about the user"""
        full_name = f'{self.first_name} {self.last_name}'
        print(f'So u r {full_name}')

    def greeting_user(self):
        """Greeting the user"""
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Hello {full_name}')

    def increse_login_attempts(self):
        """This is to add login attempts and print it out"""
        self.login_attempt += 1
        print(self.login_attempt)

    def reset_login_attempts(self):
        """This is to reset the attempts user tried to login"""
        self.login_attempt = 0
        print(self.login_attempt)


user = User('Katono', 'Wong')
user.increse_login_attempts()
user.increse_login_attempts()
user.increse_login_attempts()
user.increse_login_attempts()
user.reset_login_attempts()

class IceCreamStand(Restaurant):
    """Further add new feature"""
    def __init__(self, restaurant_info, cuisine_type, set_number_served):
        super().__init__(restaurant_info, cuisine_type, set_number_served)
        self.flavours = ['vanilla', 'grape', 'pineapple']
    def icecream(self, flavours):
        if flavours == 'vanilla':
            print("Add vanilla sourse")
        elif flavours == 'grape':
            print('Add grape sourse')
        else:
            print('Add pineapple sourse')


my_order = IceCreamStand('Ice creamy', 'icecream', 9)
my_order.icecream('grape')


class Admin(User):
    def __init__(self):
        super().__init__('admin', '')
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
user = Admin()
user.show_privileges()

