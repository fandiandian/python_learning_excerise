# 哈达玛矩阵
# Hadamard matrix
'''
概述如下：
    在数学中，哈达马矩阵是一个方阵，每个元素都是 +1 或 −1，每行都是互相正交的。阿达马矩阵常用于纠错码，如Reed-Muller码
    n x n 阶的哈达玛矩阵 H(n) 定义为一个布尔矩阵，满足下列特点：
    n 为 2 的乘幂，阶数有：1,2,4,8...(2^0,2^1,2^2,2^3....)
    
    我觉得这样定义会比较好：
        以2的乘幂来定义哈达玛矩阵的阶数比较好：
        H(1) 即：2^0 ==> 0 阶
        H(2) 即：2^1 ==> 1 阶
        依次类推
        
    特点：矩阵中的行两两正交：H<i,j> = H[i][1]*H[j][1] + H[i][2]*H[j][2] + .... + H[i][n]*H[j][n] = 0
    推导出：任意两行元素不同的个数为： n/2 ==> 正交
    
    # 构建方法
    n = 1 时：H(1)是 1 x 1 的元素为 1 的矩阵
    当 n > 1 时，4 个 H(n) 按正方形排列后，在将右下角的 H(n) 的所有元素反转成 -1；即可得到新的 H(2n) 
'''

# 这里通过构建函数的方式来实现：
# 函数的运行完成后，如果没有返回值，返回值默认为：None，此时进行变量与函数调用绑定，变量的值是：None

print('这是哈达玛矩阵')

# 获取阶数，以我的自己的定义方式来写
n = int(input('请输入构建的哈达玛矩阵的阶数（非负整数）:'))
print() # 美化输出

# 构建0阶和1阶哈达玛矩阵
hdm_0 = [True]
hdm = [[True,True],[True,False]]

# 构建输出函数，需要传入两个参数：阶数和哈达玛矩阵
def hdm_print(n,hdm):
    print('{:^4}阶即({} x {})阶哈达玛矩阵如下：'.format(n,2**n,2**n))
    print()
    for i in range(2**n):
        for j in range(2**n):
            print('{:^7}'.format(str(hdm[i][j])),end = '')
        print()
        print()

# 构建2阶以上的哈达玛矩阵函数，需要传入两个参数：阶数和哈达玛矩阵
def hdm_metrix(n,hdm):

    # 构建阶数列表
    times = [2**x for x in range(2, n + 1)]
    
    # 根据哈达玛矩阵的规律，通过循环来构建
    for time in times:
        hdm_lst = [[True for i in range(time)] for j in range(time)]
        k = len(hdm)
        for i in range(k):
            for j in range(k):
                hdm_lst[i][j] = hdm[i][j]
                hdm_lst[i][j+ k] = hdm[i][j]
                hdm_lst[i + k][j] = hdm[i][j]
                hdm_lst[i + k][j + k] = not hdm[i][j]
        hdm = hdm_lst
        
    # 返回结果
    return hdm
        
# 判定阶数，如果是0阶或者1阶，直接输出结果，结束程序
if n < 0 :
    print('你输入的不是非负整数')
elif n == 0:
    print('1阶哈达玛矩阵如下：')
    print('True')
elif n == 1:
    hdm_print(n,hdm)
else:
    hdm_print(n,hdm_metrix(n,hdm))
    



    
