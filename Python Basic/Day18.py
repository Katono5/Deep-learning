from Day17 import User


class Privileges(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        for privilege in self.privileges:
            print(f'You can do {privilege}')


class Battery:
    """An attempt to simulate the power tank in electric car"""

    def __init__(self, battery_health, battery_size=75):
        self.battery_size = battery_size
        self.battery_health = battery_health

    def describe_battery(self):
        """Print out a message about the battery"""
        print(f"This battery is {self.battery_size} kWh")

    def upgrade_battery(self):
        if self.battery_health != 100:
            self.battery_health = 100
            print('Fixed ur battery')
        else:
            print('Your battery is pretty healthy')


K50 = Battery(100)
K50.upgrade_battery()

