# Foctoring   这是一个比较的重要的例子
# 素数分解
# 素数的定义：大于1且只能被1和自己本身整除的正整数，也称质数
# 依赖于计算机的强大计算能力，可以进行较大的素数分解
from datetime import datetime    # 用于测试程序运行的时间差

def Factoring(c):
    a = 2
    l = []
    while c > 1:        # 循环开始的条件
        if c % a == 0:     
            c = c / a
            l.append(a)
        else:
            a = a + 1
    return l
print(datetime.now())
print (Factoring(287994837222311))
print(datetime.now())

# 上面是我写的程序
# 下面是书上的程序
# 最主要的区别是：循环开始的条件，我试验一下运行速度，书上的的确是要比我写的要快

def Factoring_book(n):
    m = []
    factor = 2
    while n >= factor**2:    # 循环开始的条件
        while (n % factor) == 0:
            n = n // factor
            m.append(factor)
        factor = factor + 1
    m.append(n)
    return m
print(datetime.now())
print(Factoring_book(287994837222311))
print(datetime.now())

'''

经过实际测试，我写的程序用时7.5s左右，书上写的程序，用时4s左右
这个是一个非常的大的差距，总结发现，我写的程序，用了很多的时间计算无用数据，导致效率极低

关键在：程序的循环条件，素数分解的因子是从小往大进行计算的，同一个因子，完全分解提出后，才会进行更大的因子提取
    以 n 的平方根为界限，如果累加的 factor 大于 n 的平方根依旧没有提取到因子（即 factor**2 > n），
    则后续的就不会再有 因子 出现了，此时的 n 本身就是一个素数了，所以就不用再进行后后续的计算了
    如果 n 的数值本身比较大，则会严重拉低程序的运行效率

'''

'''
本试验目的是展示，循环结构提供了解决复杂问题的能力，但使用结构简单的循环程序也可能运行缓慢
    所以 使用循环结构的时候，对循环开始的条件要有充分的认识
         必须要充分考虑程序的性能因素
'''