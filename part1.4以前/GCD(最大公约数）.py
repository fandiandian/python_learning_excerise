# 两个数的最大公约数是指能同时整除它们的最大正整数
# 欧几里得算法：求取两个数字之间的最大公约数(辗转相除法)
# use Euclid's algorithm get two intgrate's Greatest Commom Divisor(GCD) 

'''
基本原理：
    设两数为a、b(a≥b)，求a和b最大公约数  的步骤如下：
    (1) 用 a 除以 b (a≥b)，得 a / b = q...r1 
    (2) 若 r1 = 0 , 则 (a,b) = b
    (3) 若 r1 != 0 , 则再用 b 除以 r1 ，得 b / r1 = q1....r2 
    (4) 若 r2 = 0 则 (a,b) = r2 
    (5) 若 r2 != 0 则继续用 r1 除以 r2   ....  如此下去，直到能整除为止。
    其最后一个余数为0的除数即为 (a,b) 的最大公约数。 
'''

print('欧几里得算法：求取两个数字之间的最大公约数(辗转相除法)')

a = int(input('请输入第一个数字:\n'))
b = int(input('请输入第二个数字:\n'))
n = 1
aa,bb = a,b

if b > a:
    a,b = b,a
    
while n > 0:
    n = a % b
    a,b = b,n

print(' {} 和 {} 的最大公约数是 {} '.format(aa,bb,a))