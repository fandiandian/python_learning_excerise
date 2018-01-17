# pepys's problem
# 佩皮斯问题------佩皮斯日记（可读）

# 一个质地均匀的塞子，抛掷六次或者更多次，每一面出现的次数是否一致
# 随之抛掷的次数的增加，接近1/6

import pprint
import random

n = int(input('请输入你要抛掷的次数:\n'))

l = [1,2,3,4,5,6]
a = b = c = d = e = f = 0

for i in range(n):
    x = random.choice(l)
    
    if x == 1:
        a += 1
    elif x == 2:
        b += 1
    elif x == 3:
        c += 1
    elif x == 4:
        d += 1
    elif x == 5:
        e += 1
    else:
        f += 1

end = {
    1 : a,
    2 : b,
    3 : c,
    4 : d,
    5 : e,
    6 : f
}
print('抛掷 {} 次的结果如下'.format(n))
for k,v in end.items():
    print('得到点数 {} 的次数是：{} 次，所占的比重是：{}  '.format(k,v,v/n))