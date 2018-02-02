
# 倒序排列
'''
# inverse permutation
# 将一个数组进行倒序

n =  int(input('确定数组的长度：\n'))

a = [i for i in range(n)]
b = [0 for i in range(n)]
print(a)
for ii in range(n):
    b[n-ii-1] = a[ii]
print(b)

for i in range(n):
    if a[b[i]] == b[a[i]] == n-i-1:
        print(True)
'''
        
# 这个是书上的解答，有点理解不了 
'''      
import stdio
import sys
import stdarray

# Accept a permutation of integers from the command line and write the
# inverse permutation to standard output.

# Accept the permutation.
perm = []
for i in range(1, len(sys.argv)):
    perm += [int(sys.argv[i])]
n = len(perm)

# Make sure the permutation is valid.
exists = stdarray.create1D(n, False)
for i in range(n):
    if (perm[i] < 0) or (perm[i] >= n) or exists[perm[i]]:
        stdio.writeln("Not a permutation")
        sys.exit(0)
    exists[perm[i]] = True

# Invert the permutation.
permInverted = [0] * n
for i in range(n):
    permInverted[perm[i]] = i

# Write the inverted permutation.
for element in permInverted:
    stdio.write(str(element) + ' ')
stdio.writeln()
'''

# 哈达玛矩阵
# Hadamard matrix
# 已提取成单独文件

'''###########################################################'''

# 谣言 Rumor

# # Alice 与其他 n 个客人（包括 Bob）开一个派对，Bob 制造了一个关于 Alice 的谣言，并告诉其中的一个客人
# # 第一次听到的人会立即告诉下一个人（除 Alice 和告诉他的人之外）
# # 第二次听到的人则会停止传播这个谣言

# # 估计谣言停止传播前，除Alice之外都听到这个谣言的概率，同时估计听到这个谣言的客人预计数量

# # 类似于有放回的随机抽样

# import random

# n = int(input('参加party的人数：'))
# m = int(input('party开启的次数：'))

# # 听到谣言的客人的数量的数组
# Rumors = []

# # 执行 m 次
# for r in range(m):

    # # 构建及初始化人员数组
    # rumors = [False for i in range(n)]
    
    # # 随机Bob的位置，开始谣言
    # r1 = random.randrange(n)
    # rumors[r1] = True
    # # 变量说明：r1 ==> 谣言的开始的位置或者刚完成传播的位置；r2 ==> 正要传播谣言的人；r3 ==> 将被谣言传播的人
    # r2 = r1
    
    # # 听到谣言的客人的数量
    # Rumor = 1

    # # 构建循环
    # while True:
        # r3 = random.randrange(n)
        # if r1 != r3 and not rumors[r3]: 
            # rumors[r3] = True
            # # 位置变换，要传播谣言者 晋升 为刚完成传播者，将被谣言传播者 晋升 要传播谣言者
            # r1 = r2
            # r2 = r3
            # Rumor += 1
        # # 刚完成谣言传播者与将要被谣言传播的人的情况剔除
        # elif r1 == r3:
            # continue
        # else:
            # break
            
    # Rumors.append(Rumor)

# # 结果计算

# # 所有人都听到谣言
# all = 0

# for RR in Rumors:
    # if  RR == n:
        # all += 1

# print(Rumors)
# print('所有人都听到谣言的概率：{}'.format(all/m))
# print('同时听到谣言的人数：{}'.format(sum(Rumors)/m))

# 总感觉自己写的程序超级长

'''#######################################################'''

# 重复值查找 Find a duplicate
# 给定一个包含 n 个元素的数组，元素值位于 1 到 n 之间
# 实现：判断数组的元素是否存在重复，要求不使用其他数组，但可改变已知数组的内容

# 创建一个数组，元素在 1 到 n 之间随机，长度为 n 
# 依据要求：将数组进行排序，然后通过循环，如果 a[i] == a[i+1] 成立，则该数组存在重复的元素

# 这里就牵扯的数组排序的问题了
# 传说中的 八大排序法 ———— 有待学习研究


# 用于产生乱序序列
import random
# 用于测试运行的时间，主要用到其中的 datetime.datetime.now() 函数
# 通过前后时间相减，在调用 .seconds() 方法即可得到运行的时间
import datetime

# 创建一个乱序的数组
lst = [x for x in range(50000, 0, -1)]
random.shuffle(lst)
lst1 = lst[:]
lst2 = lst[:]
lst3 = lst[:]

''' #### 冒泡排序法 Bubble Sort #### '''

# 思路：通过邻位比较，大的上升或者小的上升（比较双方依据规则交换位置）
# 通过双循环，就可以将数组完成升序或者降序排序
# 升序

def Bubble_Sort(lst):
    
    # 只需比较 len(lst) - 1 次就够了
    for i in range(len(lst) - 1):
        # 添加一个标记，如果整个循环，均没有发生位置交换，则说明已完成排序，则跳出循环（此为优化版，我借鉴的）
        Flag = True
        # 内部循环：循环截止：len(lst1) - 1 - i ，下标索引超过：len(lst1) - 1 - i 就是已经冒泡确定位置的
        for j in range(len(lst) - 1 - i):
            # 大于冒泡得到升序，小于冒泡得到降序
            if lst1[j] > lst[j + 1]:   
                lst[j],lst[j + 1] = lst[j + 1],lst[j]
                Flag = False
    
        if Flag:
            return lst
    
    return lst

''' #### 选择排序（Selection sort） #### '''

# 是一种简单直观的排序算法。它的工作原理大致是将乱序的数组的元素最小（大）元素一个个取出然后按顺序放置。
# 升序

def selection_sort(lst):
    n = len(lst)
    # 外部循环，循环 n - 1 此就可以完成所有元素的比较与位置变换
    for i in range(n - 1):
        max = i
        # 内部循环：从 i + 1 位置开始，与 i 位置的元素进行比较，
        for j in range(i + 1, n):
            # 通过循环，获取最大值的索引
            if lst[max] < lst[j]:
                max = j
        # 将最大值与第 i 位置的元素进行位置调换
        lst[i],lst[max] = lst[max],lst[i]
    # 循环完成，返回结果
    return lst

''' #### 插入排序（Insertion Sort） #### ''' # 此排序方法有运行时间的比较
# 一个乱序的序列，默认第一个元素有序，将此序列分成两段，前面的有序，后面的乱序
# 将乱序的序列最后一个元素与前面有序的元素依次比较，在合适的位置插入，重复操作，即可完成排序
# 列表的元素值插入和切片操作：
    # 1、单个下标索引得到的值是一个元素，不是列表，切片操作得到的是列表，相加的时候要考虑到这一点
    # 2、切片操作的范围：包括开始位置，不包括结束位置 ==> [a,b)，需要注意结束位置的索引值
# 升序
nn0 = 0
def insertion_sort(lst,nn0):
    n = len(lst)
    # 循环 n - 1 次即可完成排序
    for i in range(n - 1):
        # 判定 lst[n - 1] 是否是已完成排序序列的最大值，是的话直接完成插入操作，重新开始排序
        if lst[n - 1] >= lst[i]:
            lst = lst[:i + 1] + [lst[n - 1]] + lst[i + 1:n - 1]
            nn0 += 1
            continue
        # 内部循环：依次比较，如果小于等于lst[j]，则进行插入操作，跳出内部循环，重新开始
        for j in range(0,i+1):
            if lst[n - 1] <= lst[j]:
                lst = lst[:j] + [lst[n - 1]] + lst[j:n - 1]
                nn0 += 1
                break
                                             
    return nn0,lst
    
a = datetime.datetime.now()
print(a)   
print(insertion_sort(lst,nn0)[0])
b = datetime.datetime.now()
print(b)
print((b-a).seconds)
print('#############################################')

#   ''' ### 上面是我自己写的，将无序序列的最后一个元素与前面的有序序列（从前向后）比较后插入正确位置 ###''' 
#   ''' ### 下面是网上的思路，将无序序列的第一个元素与前面的有序序列（从后向前）比较后插入正确位置 ###'''
#   代码段稍有区别：我的是通过序列切片的方法实现，网上的是通过元素位置调换实现的（有点类似冒泡）
#   将通过一个比较大的序列排序，对比运行时间来看，那种的运行效率更高 
nn1 = 0
def insertion_sort_1(lst,nn1):
    n = len(lst)
    for i in range(1,n):
        # 从后往前开始比较
        for j in range(i,0,-1):
            # 判定位置
            if lst[j] < lst[j - 1]:
                lst[j],lst[j - 1] = lst[j - 1],lst[j]
                nn1 += 1
            elif lst[j] >= lst[j - 1]:
                break
    return nn1,lst


a1 = datetime.datetime.now() 
print(a1)
print(insertion_sort_1(lst1,nn1)[0])
b1 = datetime.datetime.now()
print(b1)
print((b1-a1).seconds)
print('#############################################')
nn2 = 0
def insertion_sort_2(lst,nn2):
    n = len(lst)
    for i in range(1,n):
        # 判定即将开始插入的元素是否大于有序序列的最大值，不大于则开始内部循环
        if lst[i] < lst[i - 1]:
            temp = lst[i] # 保存 i 位置的值
            index = i # 保存变化的下标值
            # 从后往前开始比较，从 i - 1 开始与要插入的值比较，如果插入值要小，则进行位置变换
            # 位置变换：将大的元素往后一位保存至 j + 1 的位置，然后将空出的下标 j 保存到 index中
            for j in range(i-1,-1,-1):
                # 判定位置
                if lst[j] > temp:
                    lst[j + 1] = lst[j]
                    index = j
                    nn2 += 1
                else:
                    break
            # 内部循环结束后，将插入值 tamp 保存到空出的下标 index 当中，完成一轮插入排序
            lst[index] = temp
    return nn2,lst

a2 = datetime.datetime.now()
print(a2)
print(insertion_sort_2(lst2,nn2)[0])
b2 = datetime.datetime.now()
print(b2)   
print((b2-a2).seconds)
print('#############################################')
'''
经过运行时间测试，第一种的运行速度是最快的，第三种慢上几秒，第二种要比第一种慢上一倍左右
总结一下：
    1、第二种排序中用到了类似冒泡排序的方法，两两交换比较费计算
    2、第一种是通过直接找到插入的位置，通过切片的方式重新拼接得到新的序列
    3、第三种通过将插入的元素的值提取出来，变相将此位置空出来，通过循环，将大的值一位一位的往后移动，同时将空出位置的下标值保存到 index 变量中
       找到插入的位置后，该位置的值以往后移了一位，将位置空了出来，将插入值通过空白的下标保存到这个位置，完成一次循环
    
    由此可见：冒泡排序，两两交换，运行效率最低
    至于第一种为什么是最快的，不知道是不是走到空间换时间的路子还有待考证（我现在还是搞不清）
'''

################################################

''' #### 希尔排序（Shell sort） #### '''
# 插入排序法和冒泡排序法的结合版
# 冒泡排序法的步长是 1 ，临近的两个元素两两交换
# 希尔排序：通过一个逐渐缩小的步长来把间隔值是步长的元素的两个值进行比较和位置交换，直到步长变成 1 ，在进行冒泡排序
# 在步长变小的过程中，通过较少的比较，可以得到一个相对有序的序列，当步长为 1 时，计算量也不会很大
# 相应的，步长的选取对希尔排序的运行速度有一定的影响

nn3 = 0
def shell_sort(lst,nn3):
    n = len(lst)
    # 确定步长   
    for m in range(4,-1,-1):
        span = 2**m - 1
        # 根据步长，将数据分组，确定循环次数
        for i in range(span):
            # 遍历取间隔为span的元素
            for j in range(i + span,n,span):
                # 如果后面的数小于前面的数，开始循环
                if lst[j] < lst[j - span]:
                    # 计入开始循环时的初始位置的值及该位置的下标
                    index = j
                    temp = lst[j]
                    # 开始循环遍历，如果后面的数比前面的小，前面的数保存到后面位置上
                    for k in range(j - span, -1, -span):
                        if lst[k] > temp:
                            lst[k + span] = lst[k]
                            index = k
                            nn3 += 1
                        else:
                            break
                    lst[index] = temp
            
    return nn3,lst
          
a3 = datetime.datetime.now() 
print(a3)
print(shell_sort(lst3,nn3)[0])
b3 = datetime.datetime.now()
print(b3)
print((b3-a3).seconds)

            
            
        

