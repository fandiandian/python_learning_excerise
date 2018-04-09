from pprint import pprint
import random
''' ####### 优惠券收集问题（coupon collector）#######'''

# 集齐 n 种不同类型的优惠券需要购买的优惠券的数量为 n*H(n)
# 优惠券收集问题涉及到：
    # 调和级数的问题
    # 随机变量的和的期望等于这些随机变量的期望的和:E(X1+X2) = E(X1)+E(X2)
# 例如：集齐一副扑克牌（52张），平均大概要抽取235张牌
# 收取数量 = 52*(1+1/2+1/3+...+1/52) 约等于 52*H(52)
# 调和级数 H(n) = ln(n) + γ + ε(n)（γ为欧拉常数0.57722，ε(n)约为 (1/2n)）
# 使用集合去重的办法，集合的长度达到优惠券的种类时完成收集过程
# 也可已使用列表，判断如果优惠券不在列表当中，则添加到列表当中，循环计数+1，存在则不做列表操作，循环计数+1
    # 当列表的长度优惠券的种类时完成收集过程
# 代码如下：

# 获取试验进行次数及优惠券的种类
times = int(input("试验进行的次数："))
kind_of_coupons = int(input('优惠券的种类'))

# 定义函数
def coupon_collector(times,kind_of_coupons):
    # 循环计数总和
    sum_coupon = 0
    for i in range(times):
        # 构建获得的优惠券种类的集合，循环执行次数计数count
        coupon_set = set()
        count = 0
        # 循环条件：集合的长度小于优惠券的种类
        while len(coupon_set) < kind_of_coupons:
            coupon_x = random.randint(1,kind_of_coupons)
            coupon_set.add(coupon_x)
            count += 1
        sum_coupon += count
    # 结果输出
    print('收集齐{}中优惠券，平均需要的次数是{:^5}'.format(kind_of_coupons,((sum_coupon//times)+1)))
            
# 函数调用
coupon_collector(times,kind_of_coupons)