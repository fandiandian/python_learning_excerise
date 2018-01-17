# Fibonacci sequenc
# 斐波那契数列


# 迭代的方式实现

def a(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return a(n-1) + a(n-2)

for i in range(10):
    print(a(i))
    
    
# for 循环的方式实现

# 给定次数 n
n = 10 
a = 0
b = 1

if n == 0:
    total = 0
    print(total)
elif n == 1:
    total = 1
    print(total)
else:
    print(0)
    print(1)
    for i in range(2,n):
        total = a + b
        a,b = b,total 
        print(total)