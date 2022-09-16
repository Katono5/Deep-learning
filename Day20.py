# This could be wrong and return a Traceback,a ugly one
# print(5/0)
# so we wanna do sth to make it explict and neat

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divede by zero")

    print('Gimme two number and I will devide them')
    print('Press q to quit')

try:
    while True:
        a = int(input("The first number:"))
        if a == 'q':
            break
        b = int(input('The second number'))
        if b == 'q':
            break
        answer = a/b
        print(answer)
except ValueError:
    print('What u input is not a number')
except ZeroDivisionError:
    print('You can not devide 0')

try:
    filename = 'alice.txt'

    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'There no existing file {filename}')

title = 'Alice in Wonderland'
print(title.split())

with open('Alice in Wonderland.txt') as alice:
    contents = alice.read()
    length = len(contents.split())
    print(f"Alice in wonderland has {length} words")

def count_words(filename):
    """count the number of the words in a document"""
    try:
        with open(filename) as file:
            content = file.read()
    except FileNotFoundError:
        print(f"There's no file {filename}")
    else:
        length = len(content.split())
        print(length)


count_words('Alice in Wonderland.txt')

files = ['Alice in Wonderland.txt', 'Programming file.txt', 'NotExisting.txt']
for file in files:
    count_words(file)

# adding method v1.0
try:
    print("Gimme two numbers and I'll add them up")
    TheFirstNum = int(input('The first:'))
    TheLastNum = int(input('Another:'))
    result = TheFirstNum + TheLastNum
except ValueError:
    print('What u input seems not to be a number')
else:
    print(result)

# adding method v2.0
while True:
    try:
        print('Give me the first number')
        TheFirstNum = int(input('The first number:'))
    except ValueError:
        print('This is not a number,please retry')
        TheFirstNum = int(input('Retry:'))
    try:
        print('Give me the second number')
        TheLastNum = int(input('The second number:'))
    except ValueError:
        print('This is not a number,please retry')
        TheLastNum = int(input('Retry:'))

    result = TheFirstNum + TheLastNum
    print(result)
    break

# adding method v3.0
# not original
def ask_num(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print('This is not a number,please retry')

one = ask_num('number one:')
two = ask_num('number two')

cat = 'cats.txt'
dog = 'dogs.txt'
try:
    with open(cat) as cat:
        cat = cat.read()
        print(cat)
except FileNotFoundError:
    pass

try:
    with open(dog) as dog:
        dog = dog.read()
        print(dog)
except FileNotFoundError:
    print(f"There's no existing file {dog}")
