Girls = ['王娜娜','王晓静','王圆圆','王柳柳']

for girl in Girls:
	print(girl)

for girl in Girls:
	print(f'{girl.title()} is my ex')
	print(f'I really love u {girl.title()}\n')

print('Thx for giving me amazing period')




PizzaType = ['Neapolitan Pizza','Chicago Pizza','New York-Style Pizza']

for pizza in PizzaType:

	print(f'This is {pizza}')

print('I love Pizza')

Animal = ['Cats','Dogs','Rabbits']

for pet in Animal:
	print(f'{pet} would make good pets')

print('Any of these animals would make good pets')


for value in range(1,5):

#range函数打印[1,5),不会打印5出来

	print(value)

#range只指定一个参数则从0开始打印

list1 = list(range(6))

print(list1)

#除了前两个参量可以规定范围，可以再规定第三个参数作为步长

#打印偶数
for number in range(2,10,2):

	print(number)

squares = []

for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

#another version
squares = []

for value in range(1,11):
	squares.append(value ** 2)

print(squares)

dig = [1,2,7,6,4,8,9,0]

print(min(dig))
print(max(dig))
print(sum(dig))

squares = [value ** 2 for value in range(1,11)]

print(squares)

for number in range(1,21):
	print(number)

Number = list(range(1,1000001))
print(Number)

print(min(Number))

print(max(Number))

print(sum(Number))


Numbers1 = range(1,20,2)
for Number1 in Numbers1:
	print(Number1)


Numbers2 = range(3,31,3)
for Number2 in Numbers2:
	print(Number2)

SimNum = range(1,11)
for value in SimNum:
	value = value ** 3
	print(value)

value = [value ** 3 for value in SimNum]
print(value)


help(max)








