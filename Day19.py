# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents[:52].rstrip())
#
# with open("C:/Users/Katono/Desktop/python/pi_digits.txt") as file_object:
#     contents = file_object.read()
# print(contents[:52])
#
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line[:52].rstrip())
#         print(len(line))
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#     pi_string = ' '
#
#     for line in lines:
#         pi_string += line.strip()
#     print(pi_string[:52])
#     print(len(pi_string))
#
#
# You_birthday = input('Tell me ur birthday')
# if You_birthday in pi_string:
#     print('You birthday is in pi')
# else:
#     print('Not here')


filename = 'programming file.txt'
with open(filename, 'w') as file_object:
    file_object.write('This is good')

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

filename = 'programming file.txt'
with open(filename, 'w') as file_object:
    file_object.write('This is good\n')
    file_object.write('Could be better\n')

with open(filename) as file_object:
    content = file_object.read()
    print(content)

with open(filename, 'a') as file_object:
    file_object.write("Always could not be the best")

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

while True:
    guest = input("What's ur name:")
    if guest != 'quit':
        with open('guests.txt', 'a') as file_object:
            file_object.write(guest)
            file_object.write('\n')
        with open('guests.txt') as file_object:
            content = file_object.read()
            print(content)
    else:
        break
with open('guests.txt') as file_object:
    content = file_object.read()
    print(content)