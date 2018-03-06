from pprint import pprint
import random

''' #### 扫雷游戏（Minesweeper） #### '''

# 习题 1.4.31
# 程序自带三个参数 m,n,p 创建一个 m x n 的布尔数组，各元素占用的概率为 p ；
# 在扫雷游戏中，占用状态的单元格表示地雷，空白单元格表示安全单元格
# 输出数组，使用星号(*)表示地雷，使用英文句点(.)表示安全单元格
# 然后，替换安全单元格的内容为邻居单元格中包含地雷数量（邻居单元格为该单元格周围的8个单元格），并输出结果

# 关键点：通过构建(m+2) x (n+2) 的矩阵来，扩大一圈避免特殊情况的的处理

# 导入模块
import random

# 获取参数，生成相应的矩阵
m = int(input('请输入扫雷地图的长度')) 
n = int(input('请输入扫雷地图的宽度')) 
p = int(input('请输入每一百个单元格出现地雷个数')) 

# 实际上地雷个数为(向上取整)：((m*n*p)//100)+1
mines = ((m * n * p) // 100) + 1
# 构建地图
# 1、构建矩阵
minemap = [['.' for i in range(n + 2)] for j in range(m + 2)]
# 2、随机埋入地雷
maplist = [(i,j) for i in range(1,m+1) for j in range(1,n + 1)]
minelist = random.sample(maplist,mines)
for mine in minelist:
    minemap[mine[0]][mine[1]] = '@'
# 打印埋入地雷后的地图
for i in range(1,m+1):
    for j in range(1,n+1):
        print('{:^3}'.format(minemap[i][j]),end = '')
    print()
    
print()

# 替换安全单元格的内容为相邻单元格中包含的地雷的个数
for i in range(1,m+1):
    for j in range(1,n+1):
        count = 0
        if minemap[i][j] == '.':
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if minemap[ii][jj] == '@':
                        count += 1
            minemap[i][j] = str(count)

# 打印替换后的地雷图
for i in range(1,m+1):
    for j in range(1,n+1):
        print('{:^3}'.format(minemap[i][j]),end = '')
    print()