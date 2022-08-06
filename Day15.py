def show_messages(messages):
    for message in messages:
        print(message)


lists = ['Happy New year', 'Good day', 'Best wishes']
show_messages(lists)


def send_messages(list1, list2):
    while lists:
        message = lists.pop()
        sent_messages.append(message)


sent_messages = []
send_messages(lists[:], sent_messages)
print(sent_messages)
print(lists)


def make_pizza(*toppings):
    """Print all stuffs in the lists"""
    print("You've added these toppings in ur pizza")
    for topping in toppings:
        print(f"--{topping}")


make_pizza('Peanut')
make_pizza('mushroom', 'green purple', 'extra cheese')


def make_pizza(size, *toppings):
    """描述要制作的披萨"""
    print(f"Making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f'{topping}')


make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'extra cheese')


def build_person(first_name, last_name, **user_info):
    """创建一个字典，字典中包括我们知道的用户一切个人信息"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user_profile = build_person('Katono', 'Wong',
                            location='princeton',
                            field='physics')
print(user_profile)


def make_sandwich(*toppings):
    """收集所有三明治信息"""
    print('You ordered the following topping on ur sandwich:')
    for topping in toppings:
        print(f'--{topping}')


make_sandwich('1', '2', '3')


print(f"Your name is {user_profile['first_name']} {user_profile['last_name']}")
print(f"Your location is {user_profile['location']}")
print(f"Your field is {user_profile['field']}")

# def make_car(manufacturer, model, **options):
#     car_dict = {
#         'manufacturer' : manufacturer,
#         'model' : model,
#     }
#     for option, value in options.items():
#         car_dict[option] = value
#     return car_dict

import MyCar
# 用此方法导入特定函数
# from MyCar import make_car

mycar = MyCar.make_car('sabaru', 'outback', color='blue, tow_package=True')
from MyCar import make_car as mc
car = mc('sabaru', 'outback', color='blue, tow_package=True')
print(mycar)
print(car)
