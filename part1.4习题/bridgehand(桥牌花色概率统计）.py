from pprint import pprint
import random

''' #### 桥牌花色统计（bridge hand） #### '''

# 桥牌：一副扑克去掉大小王，剩余的52张牌发给4个人，每人13张
# 统计每手牌中不同花色的数量
# 四种花色分别为：黑桃（spade），红桃（heart），梅花（club），方块（diamond）
# 问题：统计出现：5-3-3-2，4-4-3-2,4-3-3-3出现的概率，那种牌出现的概率最大

# 模拟一副扑克牌，并乱序洗牌，按照现实发牌的方式，发给四个人
# 问题可以简化个一维数组，52个元素，四种类别，每种类别13个

times = int(input('牌局的次数'))
# 构建牌型数组
kindsofcards = []
# 构建一副扑克
pokers = ['S' for i in range(13)] + ['H' for i in range(13)] + ['C' for i in range(13)] + ['D' for i in range(13)]
# 开始循环发牌
for time in range(times):
    random.shuffle(pokers)
    # 以东（E），南（S），西（W），北（N）代表四个选手，构建发牌后的数组
    E,S,W,N = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    for i in range(0,52,4):
        # 选手东的手牌统计
        if   pokers[i] == 'S': E[0] += 1
        elif pokers[i] == 'H': E[1] += 1
        elif pokers[i] == 'C': E[2] += 1
        elif pokers[i] == 'D': E[3] += 1
        # 选手南的手牌统计
        if   pokers[i+1] == 'S': S[0] += 1
        elif pokers[i+1] == 'H': S[1] += 1
        elif pokers[i+1] == 'C': S[2] += 1
        elif pokers[i+1] == 'D': S[3] += 1
        # 选手西的手牌统计
        if   pokers[i+2] == 'S': W[0] += 1
        elif pokers[i+2] == 'H': W[1] += 1
        elif pokers[i+2] == 'C': W[2] += 1
        elif pokers[i+2] == 'D': W[3] += 1
        # 选手北的手牌统计
        if   pokers[i+3] == 'S': N[0] += 1
        elif pokers[i+3] == 'H': N[1] += 1
        elif pokers[i+3] == 'C': N[2] += 1
        elif pokers[i+3] == 'D': N[3] += 1
    
    # 牌型统计汇总
    kindsofcards.append(sorted(E,reverse = True))
    kindsofcards.append(sorted(S,reverse = True))  
    kindsofcards.append(sorted(W,reverse = True))  
    kindsofcards.append(sorted(N,reverse = True)) 

# 牌型数据分析
time_a,card_a = 0,[5,3,3,2]
time_b,card_b = 0,[4,4,3,2] 
time_c,card_c = 0,[4,3,3,3]

for card in kindsofcards:
    if   card == card_a: time_a += 1
    elif card == card_b: time_b += 1
    elif card == card_c: time_c += 1
    
print('牌型：{}出现的概率是：{:^5.2f}'.format(card_a,((time_a*100)/(times*4))))
print('牌型：{}出现的概率是：{:^5.2f}'.format(card_b,((time_b*100)/(times*4))))
print('牌型：{}出现的概率是：{:^5.2f}'.format(card_c,((time_c*100)/(times*4))))