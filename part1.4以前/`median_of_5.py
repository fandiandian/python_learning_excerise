# 五个数的中值，排序，找到第三个数
# 



# 给定 a,b,c,d,e 五个数

import random

lst1 = [11,34,25,76,89]
random.shuffle(lst1)

lst2 = lst1
lst3 = []

for i in range(5):
    a = 0
    for j in lst2:
        if j > a :
            a = j
    lst2.remove(a)        
    print(a)
    lst3.append(a)
print(lst3)

