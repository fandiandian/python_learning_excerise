'''********************************'''  
# 二维数组的输出
# import random
# aa = [True,False]
# a = [[random.choice(aa) for i in range(10)] for j in range(10)]

# for b in range(11):
    # if b == 0:
        # print('   ',end = '')
    # else:
        # print('{:^3}'.format(b),end = '')
# print('')
# for ii in range(10):
    # print('{:^3}'.format(ii+1),end = '')
    # for jj in range(10):
        # if a[ii][jj]:
            # print(' * ',end = '')
        # else:
            # print(' _ ',end = '')

    # print('')
'''********************************'''  
# 展示了列表元素可变的性质 
# a = [0 for i in range(10)]
# for i in range(10):
    # a[i] = 9 -i
# print(a)
# for i in range(10):
    # print(a[i],a[a[i]])
    # a[i] = a[a[i]]
# print(a)

# print([ii for ii in range(10,-1)])

'''********************************'''  
# # 斐波那契数列
# n = 10 
# a = [0,1]
# for i in range(2,n):
    # a += [a[i-1] + a[i-2]]
# print(a)
 
'''********************************'''  
 # # 创建一个交错二维数组，并进行复制
# import random
# aa = [0,1]
# n = [x for x in range(6,10)]
# a = [[random.choice(aa) for i in range(1,random.choice(n))] for j in range(10)]

# for i in a:
    # print(i)

# b = []

# for i in range(len(a)):
    # b += [[]]
    # for j in range(len(a[i])):
        # b[i] += [a[i][j]]
# print(b)

# print(a == b)

'''********************************'''  
# # 二维数组的行列转置  （二维数组为方阵的时候），不用创建新的数组
# import random 
# n = [nn for nn in range(11,100)]
# a = [[random.choice(n) for i in range(5)] for j in range(5)]
 
# for i in a:
    # print(i)
# print()
# for ii in range(4):
    # for jj in range(ii+1,5):
        # a[ii][jj],a[jj][ii] = a[jj][ii],a[ii][jj]
# for i in a:
    # print(i)

'''********************************'''    
# # 二维数组的行列转置  二维数组（m 行，n 列）
# # 创建的时候，是先创建一行（5 个元素，即 5 行），在创建剩下的行

# import random   
# n = [nn for nn in range(11,100)]
# a = [[random.choice(n) for i in range(5)] for j in range(7)]

# b = [[0 for i in range(7)] for j in range(5)]

# for ii in range(7):
    # for jj in range(5):
        # b[jj][ii] = a[ii][jj]
               
# for i in a:
    # print(i)
# print()    
# for i in b:
    # print(i)
'''********************************'''    
# # 布尔方阵的点积
# # 方阵的运算 C = A*B 
# # 规则：C[i][j] 等于 A 的第 i 行和 B 的第 j 列 相应的元素的积的和
# import random
# n = [True,False]
# a = [[random.choice(n) for i in range(5)] for j in range(5)]
# b = [[random.choice(n) for i in range(5)] for j in range(5)]
# c = [[0]*5 for i in range(5)]

# for ii in range(5):
    # for jj in range(5):
        # for kk in range(5):
            # c[ii][jj] = c[ii][jj] or a[ii][kk] and b[kk][jj]

# for i in a:
    # print(i)
# print()
# for i in b:
    # print(i)
# print()
# for i in c:
    # print(i)

'''********************************'''
# a为一个 n*n 阶的方阵，元素为布尔值
# 如果 i 与 j 互质，则 a[i][j] 为 True，否则为 False
# 根据互质数的定义，如果连个数的公因数只有 1 ，那么这连个数互质
# 0 和 1 互质，因为 0 的因数有无数个，但 1 的因数只有一个，就是他本身，故公因数只有 1 ，所以 0 和 1 互质
######## python 逻辑运算符中 and 的优先级高于 or，not 最高
import random
n = [i for i in range(10,50)]
nn =  random.choice(n)
a = [[0]*nn for i in range(nn)]

for i in range(nn):
    for j in range(nn):
        if (i == 0 or j == 0) and i != 1 and j != 1:
            a[i][j] = 0
        elif i ==1 or j == 1:
            a[i][j] = 1
        else:
            k = 1
            ii,jj = i,j
            if jj > ii:
                ii,jj = jj,ii
            while k > 0:
                k = ii % jj
                ii,jj = jj,k
            if ii == 1:
                a[i][j] = 1
            else:
                a[i][j] = 0
for aa in a:
    print(aa)