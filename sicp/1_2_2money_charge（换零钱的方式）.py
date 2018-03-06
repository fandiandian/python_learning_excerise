# sicp 中的实例用python实现
# sicp 1.2.2 树形递归中的实例：换硬币的计算方式
# 实例内容：1美元（100美分）换成零钱（50，25,10,5,1这 5 种币值的硬币，共有多少种换算方案

# 递归思想：
'''
按树形递归的方式来实现：
100美分换成零钱的方式等于以下列两种交换方法数目之和：
    1、用不包含 50 美分的四种硬币来换零钱的方式
    2、用包含 50 美分的五种硬币来换零钱的方式
    而以第二种方法换算的种类数 也等于 （100 - 50）用五种硬币来换算零钱的方式
    
    递归的等式可以写成如下样式
    f(a,n) = f(a,(n-1)) + f((a - value(n)),n)  其中 value(n) 代表第 n 种硬币的币值
    经过递归可以形成一个二叉树
    
    递归的中止条件：
    书上的条件是：
        1、a = 0 时，刚好全部兑换，算 1 种兑换方式
        2、a < 0 时，表示整钱 a 不足以使用目前的硬币币值来兑换，算 0 种兑换方式
        3、n = 0 时，没有币种参与兑换，算 0 种兑换方式
        经过递归推导，发现会有相当一部分的冗余计算产生在 n = 1 这种情况
            分析发现：n = 1 时，只有 1 种币种（1美分）参与兑换，所以只能算作一种兑换方式
            经过递归计算，发现以 n = 0 作为终止条件，计算出来的也是一种，是相符的
            此时就可以以 n = 1 作为中止递归的条件，算做一种兑换方式,可省去较多的冗余计算
'''

# 代码如下：

def value(n):
    if n == 5:
        return 50
    elif n == 4:
        return 25
    elif n == 3:
        return 10
    elif n == 2:
        return 5
    else:
        return 1

def count_charge_numbers(moneys,n):
    if moneys == 0:
        return 1
    elif moneys < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return count_charge_numbers(moneys,(n-1)) + count_charge_numbers((moneys - value(n)),n)

print(count_charge_numbers(600,5))       


## 运行结果展示 ##
# print(count_charge_numbers(100,5)) ==> 292 结果正确