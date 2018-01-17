# Newton Method
# 牛顿迭代法计算开方

'''
牛顿迭代法的思想：用切线近似曲线（在切点的附近，切线值与曲线值的差别很小，越靠近切点，值越接近）；
有 y = f(x) ，假设初始迭代点为 x0 则有（x0,f(x0))，
f(x) 在 x0 处的切线方程为 y = f(x0) + f'(x0)(x-x0)
    在 y = 0 时，切线的值 x1 = x0 - (f(x0) / f'(x0))
    
    再次在点（x1,f(x1)) 处做f(x)的切线，随着迭代的次数增加，求的 x(n) 越来接近函数的解
'''

# 给定一个数c，开平方

# y = x**2 -c  -->  x = c**0.5 (即根号c)
delta = 1e-15
def square_root(c):
    t = c
    while abs(t -c/t) > delta :
        t = (t + c / t) / 2
        print(t)
    
       
square_root(2)