#用sort函数永久修改列表顺序

Girls = ['王娜娜','王晓静','王圆圆','王柳柳']

Girls.sort()

print(Girls)

#中文按ASCII码排序
#英文按首字母排序

Alphabet = ['a','c','b','d']

Alphabet.sort()

print(Alphabet)

Alphabet.sort(reverse = True)

print(Alphabet)

#souted函数可以让列表顺序暂时被排序

Girls1 = ['王娜娜','王晓静','王圆圆','王柳柳']

print(sorted(Girls1))

print(Girls1)



#reverse函数可以让列表中元素完全反转并且不可逆
#如果想要逆转过来，再用一次reverse就完事了呗
Girls.reverse()

print(Girls)

len(Girls)

places = ['India','Turkey','Russia','USA','UK']

print(places)

print(sorted(places))

#此处我发现排列顺序为大写比小写等级更高

places.reverse()

print(places)

places.sort()

print(places)

places.sort(reverse = True)

print(places)

print(places[2])

print(len(Girls))










