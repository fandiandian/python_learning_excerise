# 素数的个数
# primecounter 
# 应用因数分解的方法，将无法分解的数筛选出来，即为素数（此方法可能比较笨）

print('这是一个寻找素数的程序，给定一个上限（默认下限为0），将其间所有的素数找出')
n = int(input('请输入一个数字：\n'))
m = 0
def yinshifenjie(n):n     # 因数分解
    factor = 2
    while factor**2 <= n:
        while (n % factor) == 0:
            n //= factor
        factor += 1
    return n

for i in range(1,n+1):
    if i == yinshifenjie(i):
        print(i)
        m = m + 1

print(' 0 到 {} 以内，共有 {} 个素数'.format(n,m))