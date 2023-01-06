import json

with open('Alice in Wonderland.txt') as Alice:
    content = Alice.read()
    times = content.count('a ')
    print(times)

numbers = [2, 3, 4, 5, 7, 11]

filename = 'number.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)
with open(filename) as file:
    numbers = json.load(file)

print(numbers)

username = input("What is ur name:")

filename = 'username.json'
with open(filename, 'w') as file:
    json.dump(username, file)
    print(f"We'll remember you when u come back,{username}")

with open(filename) as file:
    json.load(file)
    print(f'Welcome back {username}')

# The code following would try to load the username file
# if there's no file like that,we would create it and keep it

try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input('Tell me your name:')
    with open(filename, 'w') as file:
        json.dump(username, file)
else:
    print(f'Welcome back {username}')


def get_stored_user():
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_users():
    username = input('Your name')
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username


def greet_user():
    username = get_stored_user()
    if username:
        print(f"Hello {username}")
    else:
        username = get_new_users()
        print(f"Hello {username}")

greet_user()


FavoriteNum = input('Tell me your favorite number:')
filename = 'FavoriteNum.json'
with open(filename, 'w') as file:
    json.dump(FavoriteNum, file)
with open(filename) as file:
    number = json.load(file)
print(f'Your favorite number is {number}')


def favorite_number():
    try:
        with open(filename) as file:
            number = json.load(file)
    except FileNotFoundError:
        with open(filename, 'w') as file:
            number = input('Your favorite number:')
            json.dump(number, file)
    else:
        print(f'Your favorite number is {number}')

favorite_number()

