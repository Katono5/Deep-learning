from math import pi
print(pi)

message = input('Tell me sth,wait for my echo:')
print(message)

age = int(input('请输入年龄:'))

print(age)

if age >= 18:
    print('adult')
else:
    print('underage')
#求模运算符
#此运算符用于算出余数
print(4 % 3)
print(5 % 3)
print(9 % 3)

number = int(input('请输入一个数字'))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

cartype = input('Tell me what u wanna buy')

print(f'Let me see if I can find u a {cartype}')

Customers = int(input("How many guys u've got?\n"))

if Customers <= 8:
    print('Let me check in for u')
else:
    print('Sorry but u can come next time')

Number = int(input('Gimme a number:'))

if Number % 10 == 0:
    print(f'{Number}是10的整数倍')
else:
    print(f'{Number}不是10的整数倍')

current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1


prompt = '\nTell me sth and I will repeat it back to u\t'
prompt += 'Enter "quit" to end the program:'
'''
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
'''

#上边的方法虽然可用，但输入quit会返回quit显得冗余
#因此可以这样修改
#Ver1
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
#Ver2
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = '\nPlease enter a city u have visited:'
prompt += 'If u wanna quit just enter"quit"'

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f'I have been {city}')

current_number = int(input('Gimme a number'))
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

toppings = 'Tell me what u wanna eat\n'
toppings += 'Enter quit to finish ur order'

recipe = input(toppings)

active = True
while active:
    if recipe == 'quit':
        print("Okay that's what u want")
        break
    else:
        print(f'Alreay added {recipe}')
'''
def tp():

 toppings = 'Tell me what u wanna eat\n'
 toppings += 'Enter quit to finish ur order:'
 recipe = input(toppings)
 active = True
 while active:
    if recipe == 'quit':
        print("Okay that's what u want")
        break
    else:
        print(f'Already added {recipe}')
        active = False

tp()
'''
age = int(input('Your age:'))

if age < 3:
    price = 'free'
elif age < 12:
    price = '12USD'
else:
    price = '15USD'

print(f'U ticket is {price}')








