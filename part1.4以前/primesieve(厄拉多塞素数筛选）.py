# 厄拉多塞素数筛选法
# sieve if Eratosthenes
# 因子分解法（无法分解的数即为素数）虽然可以达到目的，但是运行的消耗较大，如果是大数，效率则会很低

# 厄拉多塞素数筛选法，采用先行构造一个指定（n + 1）长度的列表，列表中的元素全为 True
# 通过双重 for 循环，及 if 控制（控制条件为：迭代的列表的元素值为 True）
# 通过因子相乘得到的结果作为所构造列表的下标，将对应的位置的元素由 True 更改为 False 
# 当循环到列表的元素的值为 False 时，跳过，因此可以节约大量的运行时间
# 当然，先行构造的列表，会占用较大的内存空间，本程序是一个 空间 换 时间 的例子

print('厄拉多塞素数筛选法')
n = int(input('请输入一个数，控制筛选范围：\n'))

# 构造一个长度为 n + 1 的列表(第一位的下标为0，不进入计算，仅占位，实际是从第二位开始），元素值均为 True
isprime = [True for i in range(0,n + 1)]

# for循环的终止条件时 （n//2 + 1），在内嵌的for循环中, [i*j] 可以完成的整个列表的循环
for i in range(2, n//2 + 1):
    if (isprime[i]):
        for j in range(2, n//i + 1):
            isprime[i*j] = False

count = 0
prime = []
for i in range(2, n + 1):
    if (isprime[i]):
        count += 1
        prime.append(i)
print(count)
# print(prime)