alien_0 = {'color' : 'green','points' : 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just scored {new_points} points')

alien_0['x_positon'] = 0
alien_0['y_position'] = 250
print(alien_0)

#此工作可创建一个空的字典，便于后期debug
#alien_0 = {}
#此处
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}')

alien_0 = {'x_position': 0,'y_position' : 250,'speed' : 'medium'}

#向右水平移动外星人
#根据速度决定外星人移动远近

if alien_0['speed'] == 'slow':
    alien_0['x_position'] = 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] = 2
else:
    #this alien must move really fast
    alien_0['x_position'] = 3

print(alien_0['x_position'])

#以上结果虽然能跑，但是并不适用，直接覆盖了原量
#为了更科学，可以用书上的代码

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this alien must move really fast
    x_increment = 3

#此步规定好incresement以后只需要再把其与原函数相加

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])

#用del删除字典中键值对
del alien_0['y_position']
print(alien_0)

favorite_language = {
    'a' : 'python',
    'b' : 'c',
    'c' : 'ruby',
    'd' : 'golang',
    'e' : 'c#',
}

language = favorite_language['a'].title()

print(f"a's favorite language is {language}")

girlfriend = {'1st' : '王晓静','2nd' : '王柳柳'}
'''
此操作会报错KeyError
print(girlfriend['3rd'])
为解决此报错，对于一个没有内容的值，我们可以用get指定返回值
'''
Third_value = girlfriend.get('3rd' ,'None')
print(Third_value)

#此操作用于有时不知道一个值在不在字典里

Name = {'username' : '王晓静',
        'firstname' : '王',
        'lastname' : '晓静',
        }

for key,value in Name.items():
    print(f'Key : {key}')
    print(f'value :{value}\n')

Katono = {
    'FirstName' : 'Wong',
    'LastName' :'Bing',
    'age' : '18',
    'gender' : 'male',
}

print(Katono['FirstName'])
print(Katono['LastName'])
print(Katono['age'])
print(Katono['gender'])

Luck = {
    '王晓静' : '7',
    '王柳柳' : '8',
    '王花花' : '9',
}

for name,LuckyNum in Luck.items():
    print(f"{name}'s lucky number is {LuckyNum}")

for name in Luck.keys():
    print(name)

for LuckyNum in Luck.values():
    print(LuckyNum)

favorite_language = {
    '王晓静' : 'c',
    '王柳柳' : 'Python',
    '王花花' : 'Golang',
    '王红红' : 'c++'
}

friends = ['王晓静','王柳柳']

for name,language in favorite_language.items():
    if name in friends:
        print(f'Hello {name}')
        print(f'Your favorite language is {language} \n')
    else:
        print(f'Hello {name}\n')

if '王华' not in favorite_language.keys():
    print('王华 plz take ur roll')

favorite_language = {
    '王晓静' : 'c',
    '王柳柳' : 'Python',
    '王花花' : 'Golang',
    '王红红' : 'c'
}

print('These following languages are mentioned:')
for value in favorite_language.values():
    print(value)

for language in set(favorite_language.values()):
    print(language.title())

favorite_language = {
    '王晓静' : 'c',
    '王柳柳' : 'Python',
    '王花花' : 'Golang',
    '王华'  : 'c#',
    '王红红' : 'c',
}

for Name,language in favorite_language.items():
    print(f"{Name}'s language is {language}")

for Name in favorite_language.keys():
    print(Name)

for language in set(favorite_language.values()):
    print(language)

    

