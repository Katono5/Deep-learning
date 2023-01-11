def make_album(artist, name, track=''):
    """
   Input the singer and the album's name
   Then we check the key and value
   Then we put them into a dictionary and return that to you
   """

    album = {
        'artist': artist.title(),
        'name': name.title(),
    }
    if track:
        album['track'] = track
    return album


print('When inputting,you can enter "q" anytime to quit')
while True:
    artist = input('The artist:')
    if artist == 'q':
        break
    name = input('The name of the album:')
    if name == 'q':
        break
    album = make_album(artist, name)
    print(album)


def greet_user(names):
    """greet any guest in the list"""
    for name in names:
        msg = f'Hell`o,{name.title()}'
        print(msg)


username = ['hannah', 'ty', 'margot']
greet_user(username)


def print_models(unprinted_designs, completed_designs):
    """
    模拟打印所有设计，知道打印完所有设计
    打印完每个设计，将其移入列表completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing {current_design}')
        completed_designs.append(current_design)


def show_completed_designs(completed_models):
    """显示打印好的所有模型"""
    print('The following list has been completed')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['a', 'b', 'c']
completed_designs = []
print_models(unprinted_designs, completed_designs)
# 用此方法可以使unprinted_design列表保持不变使用副本完成功能
# print_models(unprinted_designs[:], completed_designs)
show_completed_designs(completed_designs)

print(unprinted_designs)


def build_person(first_name, last_name):
    person = {
        'Firstname': first_name,
        'Lastname': last_name,
    }
    return person


while True:
    first_name = input('first name')
    if first_name == 'q':
        break
    last_name = input('last name')
    if last_name == 'q':
        break
    person = build_person(first_name, last_name)
    print(person)


def show_messages(messages):
    for message in messages:
        print(message)


lists = ['Happy New year', 'Good day', 'Best wishes']
show_messages(lists)


def send_messages():
    while lists:
        message = lists.pop()
        sent_messages.append(message)
sent_messages = []
send_messages()
print(sent_messages)
print(lists)
