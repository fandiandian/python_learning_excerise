# 2D随机行走
# 2D random walk
# 在一个平面2n*2n正方形空间，随机产生一个点，然后随机四个方向行走一个单位，最后触及正方形边界，结束，返回行走次数

import random

print('2D随机行走')
n = int(input('请输入一个数字，以确定正方形的范围：\n'))

# 以直角坐标原点为一个正方形的角，x,y 轴为正方形的边，在第一象限内生成一个 2n*2n 的正方形

x = random.randint(0,2*n)
y = random.randint(0,2*n)
print('初始坐标是：({},{})'.format(x,y))

# turned = {
    # '东' : lambda x : x + 1,
    # '西' : lambda x : x - 1,
    # '北' : lambda y : y + 1,
    # '南' : lambda y : y - 1
# }

# turns_tunred = ['北','西','南','东']

# steps = 0

# while x > 0 and x < 2*n and y > 0 and y < 2*n:
    # turns = random.choice(turns_tunred)
    # if turns == '东' or turns == '西' :      
        # x = turned[turns](x)
    # else:
        # y = turned[turns](y)
    # steps += 1
    # print('向 {} 前进一步，前进后的坐标是： ({},{}) '.format(turns,x,y))
    
# print('走出 {} X {} 的正方形，共用了 {} 步'.format(2*n,2*n,steps))


#  为什么使用下面这个表格的时候会出现错误？？？？？？？？
turned = {
    '东' : x + 1,
    '西' : x - 1,
    '北' : y + 1,
    '南' : y - 1
}

turns_tunred = ['北','西','南','东']

steps = 0

while x > 0 and x < 2*n and y > 0 and y < 2*n:
    turns = random.choice(turns_tunred)
    if turns == '东' or turns == '西' : 
        print(x)
        x = turned[turns]
        print(x)
    else:
        print(y)
        y = turned[turns]
        print(y)
    steps += 1
    print('向 {} 前进一步，前进后的坐标是： ({},{}) '.format(turns,x,y))
    
print('走出 {} X {} 的正方形，共用了 {} 步'.format(2*n,2*n,steps))
 
