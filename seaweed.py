"""1个海藻第三天会分裂成两个，分裂的海藻也是第三天分裂成2个 ，怎么定义计算n天后海藻的数量函数"""

day = int(input('How many days have passed:'))

if day == 1:
    seaweed = 1
elif day % 3 != 0:
    while day % 3 != 0:
        day = day - 1
    seaweed = 2 * day
else:
    seaweed = 2 * day / 3
print(f"There's {seaweed} seaweed")


