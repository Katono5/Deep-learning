#切片可用于对列表片段的调用
Names = ['王晓静','王红红','王晓静','王晓静','王华']

print(Names[0:2])
print(Names[2])
print(Names[:2])
print(Names[:-2])
print(Names[-2:])
print(Names[0:5:2])

print('Here are my first three gfs:')
for value in Names[:3]:

	print(value.title())
'''
for num in range(1,101):
	print(max[num])
'''

i = 0
for num in range(1,101):
	i += num
print(i)

Foods = ['curry', 'cheese', 'pizza']
favorite = Foods[:]

print(Foods)
print(favorite)

item = ['apple', 'banana', 'grape', 'pizza', 'curry']

print(item[0:3])
print(item[1:4])
print(item[2:5])

Foods.append('apple')

for value in Foods:
	print(f'My favorite food is {value}')



