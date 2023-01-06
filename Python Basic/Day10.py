#用range创造30个机器人in a row
aliens = []

for alien_number in range(10):
    new_alien = {'color' : 'green','points' : '5','speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)

print(f'Total number of aliens is {len(aliens)}')
print(aliens)
for alien in aliens[0 : 3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'mediun'
    else:
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
print(aliens)

import sys
print (sys.version)

pizza = {
    'curst' : 'thick',
    'toppings' : ['mushroom','peanuts'],
}


print(f"Your ordered a {pizza['curst']}-curst pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

favorite_language = {
    '王晓静' : ['c','java'],
    '王柳柳' : ['Python','php'],
    '王花花' : ['Golang','Python'],
    '王华'  :  ['c#','ruby'],
    '王红红' : ['c','c++'],
}

for name,languages in favorite_language.items():
    print(name)
    for language in languages:
        print(f'{language.title()}')
    print('\n')

users = {
    'Katono' : {
        'first' : 'Katono',
        'last' : 'Wong',
        'Location' : 'Huojia',
        },
    'Miracle' : {
        'first' : 'Miracle',
        'last' : 'Lee',
        'Location' : 'USA',
        },

    }

for username,user_info in users.items():
    print(f'Username = {username}')
    fullname = f"{user_info['first']} {user_info['last']}"
    Location = f"{user_info['Location']}"

    print(f'\t{fullname}')
    print(f'\t{Location}')

users = {
    'Katono' : {
        'first' : 'Katono',
        'last' : 'Wong',
        'Location' : 'Huojia',
        },
    'Miracle' : {
        'first' : 'Miracle',
        'last' : 'Lee',
        'Location' : 'USA',
        },

    }

for username,user_info in users.items():
    print(f"username = {username}")
    print(f"firstname = {user_info['first']}")
    print(f"last name = {user_info['last']}")
    print(f"location = {user_info['Location']}")

pets = {
    'dog' : {
        'owner' : 'Katono',
        'name' : 'dog',
        },

    'cat' : {
        'owner' : 'Me',
        'name' : 'cat',
    },
}

for pet,pet_info in pets.items():
    print(f"pet is {pet}")
    print(f"pet's owner is {pet_info['owner']}")
    print(f"pet's name is {pet_info['name']}")


favorite_place = {
    'Katono' : 'China',
    'Hamari' : 'Indie',
    'Eminem' : 'USA',
}

for name,place in favorite_place.items():
    print(f"He/She is {name}")
    print(f"His/Her favorite place is {place}")

LuckyNum = {
    'a' : [4,7],
    'b' : [3,6],
    'c' : [1,7],
}

for man,Lucky in LuckyNum.items():
    print(f"He/She is {man}")
    print(f"His/Her lucky numbers are {Lucky}")

city = {
    'Xinxiang' : {
        'country' : 'China',
        'population' : '1million',
        'fact' : 'shitty place',
        },
    'Chicago' : {
        'country' : 'USA',
        'population' : '500000',
        'fact' : 'rich',
        },
    'Tokyo' : {
        'country' : 'Japan',
        'population' : '1500000',
        'fact' : 'anime',
        },
}

for city,info in city.items():
    print(f"This city is {city}")
    print(f"This city is in {info['country']}")
    print(f"This city has a population of {info['population']}")
    print(f"This city is famous for this fact that"
            "{info['fact']}")











