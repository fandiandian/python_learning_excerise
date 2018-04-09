# text progress bar
# 刷新的关键是：之后打印的覆盖之前打印的数据

import time

scale = 100
print('start'.center(scale//2,'-'))
for i in range(scale + 1):
    a = '>>' * (i//10)
    b = ' _' * ((scale - i + 9)//10)
    c = i/scale
    print('[{}{}]{:^6.2%}'.format(a,b,c),end = '\r')
    time.sleep(0.1)
print('\n'+'finish'.center(scale//2,'-'))