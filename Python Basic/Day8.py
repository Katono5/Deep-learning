['green', 'yellow', 'red']
for alien_color in color:
	if alien_color == 'green':
		print('You scored 5 points')
	else:
		print('You suck')

age = int(input())

if age <= 2:
    print('baby')
elif age <= 4:
    print('kid')
elif age <= 13:
    print('child')
elif age <= 20:
    print('teen')
elif age <= 65:
    print('adult')
else:
    print('old guy')

favorite_fruits = ['banana', 'apple', 'orange']

if 'banana' in favorite_fruits:
    print('You really love banana')
if 'apple' in favorite_fruits:
    print('You really love apple')
if 'orange' in favorite_fruits:
    print('You really love orange')
if 'grape' in favorite_fruits:
    print('You really love grape')
if 'pumpkin' in favorite_fruits:
    print('You really love pumpkin')

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'adding {requested_topping}')

print('Your pizza finished')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry our green pepper ran out')
    else:
        print(f'adding {requested_topping}')

print('Your pizza finished')


# 此代码用于检查列表内容是否为空，如果为空返回False不空则True
requested_topping = []
# 核心在于if 检查列表
if requested_topping:
    for requsted_topping in requested_toppings:
        print(f'adding {requested_topping}')
    print('Your pizza finished')

else:
    print('You sure about a plain pizza?')

available_toppings = ['mushroom', 'olives', 'peppers'
                      'pineapple', 'extra cheese', 'onion']

requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'adding {requested_topping}')
    else:
        print(f"We don't have {requested_topping},Sorry")
print('\nYour pizza done')

user = ['user1', 'user2', 'user3', 'use4', 'admin']

for customer in user:
    if customer == 'admin':
        print('Hello admin,wanna see a status report?')
    else:
        print(f'Hello {customer},thank u for logging in')

user = []

if user:
    if customer == 'admin':
        print('Hello admin,wanna see a status report?')
    else:
        print(f'Hello {customer},thank u for logging in')
else:
    print('We found no users')

current_users = ['user1','user2','user3','user4','user5']
new_users = ['uSer5','user6','user7','user8','user9']
'''
错误示范
for new_user in new_users:
    for current_user in current_users:
        if new_user.title() == current_user.title():
            print(f'{new_user} has already been used')
        else:
            print('Register sucessful')
'''
current_user = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_user:
        print(f'Sorry {new_user} this name is taken')
    else:
        print(f'Congrats,this name is available')





