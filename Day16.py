class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令蹲下"""
        print(f'{self.name} is now sitting')

    def roll_over(self):
        """模拟小狗收到命令打滚"""
        print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's name is {my_dog.age}")


my_dog.sit()


class Restaurant:
    def __init__(self, restaurant_info, cuisine_type):
        """format the properties"""
        self.restaurant_info = restaurant_info
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Tell customers this cafe is about what"""
        print(f"The restaurant's name is {self.restaurant_info}")
        print(f"The restaurant is famous for {self.cuisine_type}")

    def open_restrant(self):
        """Tell customers this cafe is open"""
        print('This restrant is open now')


Restrant1 = Restaurant('Queenland', 'cangroo')

Restrant1.describe_restaurant()
Restrant1.open_restrant()


class User:
    def __init__(self, first_name, last_name):
        """format attributeself"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Give out the info we have about the user"""
        full_name = f'{self.first_name} {self.last_name}'
        print(f'So u r {full_name}')

    def greeting_user(self):
        """Greeting the user"""
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Hello {full_name}')


user = User('Katono', 'Wong')
user.describe_user()
user.greeting_user()


class Car:
    """一次模拟汽车的初步尝试"""

    def __init__(self, make, model, year, odometer=0):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_descriptive_name(self):
        """返回简洁的描述性信息"""
        long_name = f'{self.year} {self.make}, {self.model}'
        return long_name.title()

    def read_odometer(self):
        """print info about the odometer"""
        print(f'Ur car has {self.odometer} miles on it')

    """An further try to perfect this class"""

    def update_odometer(self, miles):
        """Add extra odometer to the original"""
        self.odometer += miles

    def fill_tank(self):
        print('filled')


my_new_car = Car('audi', 'a4', '2019', 12)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('sabaru', 'outback', 2015, 12)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(80)
my_used_car.read_odometer()
print('\n\n')

class Battery:
    """An attempt to simulate the power tank in electric car"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print out a message about the battery"""
        print(f"This battery is {self.battery_size} kWh")

class ElectricCar(Car):
    """Special feathur about electric car"""
    def __init__(self, make, model, year):
        """This is to format all the stuffs here"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_tank(self):
        print('This car does not have a tank!')
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_tank()



