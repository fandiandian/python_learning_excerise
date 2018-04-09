from pprint import pprint
import random
# 2018/03/07

''' ####### 生日问题（birthday problem）#######'''

# 有一个足够大的房间，现每次进入一个人，直到进入的人中有两个人的生日相同，则停止进入
# 问题：平均进入多少个人，才能有两个人有相同的生日？
# 问题简化：生日在1~365之间（不考虑闰年），房间看做已个列表数组
# 问题的关键是：数组的元素重复的查找，判断一个元素是否在这个数组中（可以用 in 来进行判断）

# 代码如下：

import random
# 获取试验进行次数
times = int(input("试验进行的次数："))

# 定义函数
def birthday_problem(times):
    #　保存每次试验进入的人数的列表，以及进入人数的求和
    number_person = []
    sum_person = 0
    for i in range(times):
        # 构建房间数组,进入的人数计数
        room = []
        persons = 0
        while True:
            person_x = random.randint(1,365)
            if person_x not in room:
                room.append(person_x)
                persons += 1
            else:
                persons += 1
                break
        number_person.append(persons)
        sum_person += persons
    # 结果输出
    print('一个房间中平均进入{:^5}个人，就会有两个人有相同的生日'.format((sum_person//times)+1))
    # print('每次进入的人数结果如下：')
    # 美化输出结果（５个一行）
    # for time in range(1,times+1):
        # print(number_person[time-1],end = '  ')
        # if time % 5 == 0:
            # print()
            
# 函数调用
birthday_problem(times)