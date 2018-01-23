# 最小置换
# minima in permutation

# 生成一个长度为 n ，个数为 m 的二维随机数组，输出生成的排列中从左至右极小数的数量的平均值

# 通过定义函数的，调用函数的方式实现

# （我对这个题目的理解可能有问题）
import random

m = int(input('请输入数组的行数\n'))
n = int(input('请输入数组的列数\n'))

# 随机数的范围定在 [1,20]

# 构建函数
def minima_in_permutation(a,b):
    
    # 构建随机数组
    rand_list = [[random.randrange(1,21) for i in range(b)] for j in range(a)]
    
    # 保存最小值 mimima 及其个数 time 的列表 times
    times = []
    
    for ii in range(a):
        # 计数 time 及 最小值
        time = 0
        minima = min(rand_list[ii])
        
        for jj in range(b):
            if rand_list[ii][jj] == minima:
                time += 1
        
        times += [(minima,time)]
    print(times)
    total = 0
    for iii in range(len(times)):
        total += times[iii][1]
    print('极小值的个数的为：{}'.format(total/len(times)))

# 调用函数
minima_in_permutation(m,n)