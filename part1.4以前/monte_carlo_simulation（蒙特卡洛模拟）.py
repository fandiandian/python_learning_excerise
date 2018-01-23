# Monte Carlo simulation
# 蒙特卡洛模拟

'''
蒙特卡洛模拟
通过计算机模拟现实世界可能发生的情况
    通过随机变量来模拟事件A的变化因数，设定变化的次数，即可得到一组模拟的结果
    通过多次（1000次或者10000次）模拟，结果的平均值具有参考价值
    对多次模拟的值进行数学分析，服从正态分布

即：通过大量的随机取样，所得结果的越接近真实值

模拟和理论计算彼此可以相互验证，在实际应用中，模拟的值可以作为难以用分析方法求解的复杂问题的推荐结果

股票的波动问题，依据实际环境，设定随机变量的范围，多次模拟的均值有参考意义
'''
# 模拟在区间[0,1]，（√x - x） 所为围起来的面积 积分结果为1/6

import math,random

def monte_carlo(m):
    n = 0
    for tick in range(m):
        x = random.random()
        y = random.random()
        if (y >= x) and (y <= math.sqrt(x)):
            n = n + 1
    return n / m

# monte_carlo(1000000)  
l = [monte_carlo(1000000) for i in range(100)]
print(l)
print(sum(l) / len(l))

    

