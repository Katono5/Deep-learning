dimensions = (1,2,3)
print(dimensions[0])
print(dimensions[1])

'''
dimensions[0] = 3
This would raise an error called 
'tuple' ebject doesn't support item assignment'
tuple remains always the same,unchangeable
'''

#尽管元组本身不可以被改变，所用的元组变量却可以被改变
OriginalDimensions = (1,2)
for dimension in OriginalDimensions:
	print(dimension)
print('\n')

ModifiedDimensions = (3,4)
for dimension in ModifiedDimensions:
	print(dimension)

foods = ('chicken','apple','banana','curry','icecream')
for food in foods:
	print(food)

#foods[0] = 'shit'

foods_new = ('chicken','fish','banana','apple','curry')
print('u can choose food from our new menu\n')
for food in foods_new:
	print(food)

for food in foods:
	if food == 'curry':
		print(food.upper())
	else:
		print(food)

car = 'BMW'
print(car == 'BMW')

car = 'BMW'
print(car == 'bmw')

#此操作可以忽略大小写
print(car.lower() == 'bmw')
 #!=用于检查不相等
print(car.lower() != 'audi')


car = 'subaru'
print('Is car == "subaru"? I predict True.')
print(car == 'subaru')

print('\nIs this car == "audi"? I predict False')
print(car == 'audi')


age = input()
if age < 4:
	print("It's free for you")

elif age  <18:
	print("half price")

else:
	print('Full price') 

color = ['green','yellow','red']
for alien_color in color:
	if alien_color == 'green':
		print('You scored 5 points')
	else:
		print('You suck')

