# 将十进制转化为二进制
# change decimal to binary
# 两种写法，那种更好？？？


'''
进制转换：
eg：19 = 16 + 2 + 1 = 2**4 + 0***3 + 0**2 + 2**1 + 2**0
  
'''
cc = int(input('请输入要转化的十进制数字'))
# 这是我写的
def decimal_to_binary(cc):
    total = 0
    l = []
    c = cc
    while c != 0:
        n = 0
        while c >= 2**(n + 1):
            n = n + 1
        l.append(n)
        c = c - 2**n
    
    for i in l:
        total = total + 10**i
    print('十进制：{} 转化为二进制：{}'.format(cc,total))

decimal_to_binary(cc)

# 这是书上写的,稍加改变，定义成函数
def decimal_to_binary_1(cc):
    v = 1
    while v <= cc // 2:   # // 是取整   % 是取余
        v = v * 2
    while v > 0:
        if cc < v:
            print(0,end = '')
        else:
            print(1,end = '')
            cc = cc - v
        v = v // 2
    print('')
print('十进制：{} 转化为二进制：'.format(cc),end = '')
decimal_to_binary_1(cc)
