unconfirmed_users = ['Alice', 'Bob', 'Cello']

confirmed_users = []

while unconfirmed_users:
    users = unconfirmed_users.pop()

    print(f'Verifying user : {users.title()}')
    confirmed_users.append(users)


print(confirmed_users)


ex = ['王晓静', '王晓静', '王晓静']
print(ex)
while ex:
    ex.remove('王晓静')

print(ex)

responses = {}

# Flag
polling_active = True
while polling_active:
    name = input('\nWhat is ur name')
    response = input('Which mountain u wanna climb:')

    responses[name] = response
    
    repeat = input('Would u like to let another person respond?(yes/no)')
    if repeat == 'no':
        polling_active = False


print('\n ------Poll Results------')
for name, response in responses.items():
    print(f'{name} would love to climb {response}.')


sandwich_orders = ['a', 'b', 'c']

for sandwich in sandwich_orders:
    print(f'I made ur {sandwich} sandwich')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'{finished_sandwich} is finished')

sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'pastrami']

print('Our pastrami has been sold out')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

responses1 = {}
print('Where u wanna visit')

active = True
while active: 

    user = input("What's ur name")
    response = input('The place?')
    responses1[user] = response

    repeat = input('Else?(yes/no)')
    if repeat == 'no':
        active = False
print('\n-------rolling------')
for user, response in responses1.items():
    print(f'{user} wanna vist {response}')


def greet_user():
    # 打个招呼
    print('Hello')


greet_user()


def greet(username):
    print(f'Hello {username}')


greet('Jesse')
