# 二维数组的应用实例：自回避随机行走（本例所使用的的数组为矩阵，不考虑交错数组）
# self-avoiding random walk
# 一个城市的道路上,假设该城市的道路网络为矩阵，一只AlphaGo在该城市随机行走，走到已走过的点即为失败,请问AlphaGo走出的概率是多大
# 以交叉路口为节点（False），先行构建一个 m*n 的二维数组，所有的值均为False，在 AlphaGo 经过的节点，修改成True
# 自回避：前进的方向上的下一节点为True时（说明该节点已经走过），回避此方向（抛弃这个方向）

'''
与书上的稍有区别，书上的对方向的选择上，会出现回头，但是不做操作

还有在二维的数组构建过程中，出现了一个问题
最初的所写的代码是：
    roads = [[False for i in range(n)]*m]
    得到的结果是一个一维数组
改进后的代码是：
    roads  = [[False for i in range(n)]]*m
    得到的解结果虽然是一个二维数组，但是是一维数组的重复（不是复制体），更改其中一行的某个元素，其他的的行的相应位置的元素也同时改变
    
    这应该是python列表的映射机制导致的
    分析结果如下：
        此二维列表的的第一行是由推导生成的，没有问题，问题出现在由一维扩展到二维的时候出现的
        第二行后面的行，在内存中的表现是：保存的元素的对象引用（id，内存地址）是第一行的元素的对象引用
        所以，此二维数组的中的行均指向第一行中的元素
        故改变其中一行的中的某个元素，其他行的相应位置的元素均发生改变
    
    再次改进后，是通过列表相加的得到的，产生的是全新的列表，与原来的第一行的元素的对象引用是不同的
'''
# 书上的程序放在最下面了
# 2018年1月11日 进行修改，修改后与书上的运行结果差不多了，显得有点长啰嗦，毕竟跟书上不一样

import random

# 预设条件
print('Alphago的自回避随机行')
m = int(input('请预设该城市的横向道路（行）的数量：\n'))
n = int(input('请预设该城市的纵向道路（列）的数量：\n'))
walk_times = int(input('请预设行走的次数：\n'))

# 死亡计数，走出计数，走出步数列表
death_time_steps = []
walk_out_steps = []

# 开始不回头的随机行走
for times in range(walk_times):
    
    # 构建及重置这个城市的道路节点矩阵
    roads = [[False]*n for _r in range(m)]
    
    # 预设及重置 AlphaGo 在地图的中心点（附近）坐标（m//2, n//2)
    x = m//2 
    y = n//2
    roads[x][y] = True
    
    # 初始化行走次数
    steps = 0 
    
    # 走出的条件（循环控制条件），AlphaGo 触及边界
    while (x > 0) and (x < m - 1) and (y > 0) and (y < n - 1):
        
        # 构建移动操作计算字典表
        move = {
            'east': lambda x : x + 1,
            'west': lambda x : x - 1,
            'north': lambda y : y + 1,
            'south': lambda y : y - 1 }
        
        # 初始方向列表
        directions = []
        
        # 构建方向列表数据，前进方向方节点没有走过（False），加入方向列表中，自回避
        if not roads[x+1][y]:
            directions.append('east')
        
        if not roads[x-1][y]: 
            directions.append('west')
            
        if not roads[x][y+1]: 
            directions.append('north')
            
        if not roads[x][y-1]: 
            directions.append('south') 
        
        # 如果方向的列表长度为0，则说明进入了死胡同，终止 while 循环,更新死亡是的步数
        if len(directions) == 0:
            death_time_steps.append(steps)
            break
        
        # 行走方向随机选择
        turned = random.choice(directions)
        
        # 根据方向 turned 进行坐标运算
        if turned == 'east' or turned == 'west':
            x = move[turned](x)           
        else:
            y = move[turned](y)
           
        # AlphaGo行走至新的坐标节点，及行走步数增加
        roads[x][y] = True
        steps += 1         
        
    # 判定是否走出，用于数据分析
    if not ((x > 0) and (x < m - 1) and (y > 0) and (y < n - 1)):
        walk_out_steps.append(steps)
print(walk_out_steps)
print('在 {} X {} 的网格中,共行走了：{} 次，走出了：{} 次'.format(m,n,walk_times,len(walk_out_steps)))
print('平均走出的步数结果是：{:.2f}：'.format(sum(walk_out_steps)/len(walk_out_steps)))
print('无法走出的次数：{} 次，无法走出的概率是：{:.2f}'.format(len(death_time_steps),len(death_time_steps)/walk_times*100))
if len(death_time_steps) > 0:
    print('平均无法的步数结果是：{:.2f}：'.format(sum(death_time_steps)/len(death_time_steps)))
    
''' 
# 这是书上的版本 
import random

print('Alphago的自回避随机行')
m = int(input('请预设该城市的横向道路（行）的数量：\n'))
n = int(input('请预设该城市的纵向道路（列）的数量：\n'))
walk_times = int(input('请预设行走的次数：\n'))

death_end = 0
for t in range(walk_times):
    a = [[False]*n for _r in range(n)]
    x = y = n//2
    while (x > 0) and (x < m - 1) and (y > 0) and (y < n - 1):
        # Check for dead end and make a random move
        a[x][y] = True
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            death_end += 1
            break
        r = random.randrange(1,5)
        if   (r == 1) and (not a[x+1][y]): x += 1
        elif (r == 2) and (not a[x-1][y]): x -= 1
        elif (r == 2) and (not a[x][y+1]): y += 1
        elif (r == 2) and (not a[x][y-1]): y -= 1
        
print('{}% dead ends'.format(100*death_end/walk_times))
'''
