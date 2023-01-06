def display_message():
    print('Im learning python')


display_message()


def favorite_books(book):
    print(f'One of my favorite books is {book.title()}')


favorite_books('Secret')


def describe_pet(animal_type='Dog', pet_name='Cat'):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('Dog', 'Cat')
describe_pet(pet_name='Dog', animal_type='Cat')
describe_pet()


def full_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = full_name('Katono', 'Wong')
print(musician)

# Plz put the middle name into the last position
def full_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


name = full_name('Katono', 'Wong')
print(name)
name = full_name('Katono', 'Wong', 'NoMidName')
print(name)


def personal_info(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = personal_info('Katono', 'Wong', '19')
musician1 = personal_info('晓静', '王')
print(musician)
print(musician1)


# def full_name(first_name, last_name):
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# while True:
#     print('\nplz tell me ur name')
#     print('enter "q" anytime to quit')
#
#     f_name = input('First Name:')
#     l_name = input('Last Name:')
#
#     if (f_name or l_name == 'q'):
#          break
#     full_name = full_name(f_name, l_name)
#     print(full_name)
def full_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()


while True:
    print('\nplz tell me ur name')
    print('enter "q" anytime to quit')

    f_name = input('First Name:')
    if f_name == 'q':
        break

    l_name = input('Last Name:')
    if l_name == 'q':
        break
    Fullname = full_name(f_name, l_name)
    print(Fullname)


def city_country(city, country):
    Output = f'{city}, {country}'
    return Output.title()

while True:
    city = input('City:')
    if city == 'quit':
        break
    country = input('Country')
    if country == 'quit':
        break
    Output = city_country(city, country)
    print(Output)
