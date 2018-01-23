# 输出一个 n*n 的列表，对于第 i 行第 j 列的为值，如果两个数互质（最大公约数为1），则输出 *，其余输出空白
# GCD的花式应用

n = int(input('请输入一个数字：\n'))

def gcd(a,b,m = 1):
    if a < b:
        a,b = b,a
    while m > 0:
        m = a % b
        a,b = b,m
    return a
for i in range(1,n+1):
    for j in range(1,n+1):
        if gcd(i,j) == 1:
            print('* ',end = '')
        else:
            print('  ',end = '')
    print()