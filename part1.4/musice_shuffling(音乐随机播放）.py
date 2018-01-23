# 音乐随机播放
# music random play(Music shuffling)

# 要求：随机播放 m 首歌各一次，然后重复。
# 估计不按顺序播放两首歌的概率（即歌曲 2 后面不播放歌曲 3 ，歌曲 9 后面不播放歌曲 10）

# 创建一个长度为 m 的数组，打乱顺序
# 不放回的随机取样，样本总量为 m ，抽取 m 个样本
# 还有一种是使用 random.choice() 得到样本，在原始数组中将其删除
# 最直接的方式 random,shuffle()
# 长度为 m ，间隔为 m-1，所需的结果为：连续的次数/ (m-1)

import random

m = int(input('请确定歌曲的数量：\n'))

# 连续歌曲计数
n = 0

# 创建歌曲数组
music_repositories = [i for i in range(1,m+1)]

# 乱序
'''
# 第一种 最简单的
# random.shuffle(music_repositories)

# 第二种 random.choice()
# music_repositories_copy = []

# for ms in range(m):
    # musics = random.choice(music_repositories)
    # music_repositories_copy += [musics]
    # music_repositories.remove(musics)
'''
# 第三种 通过循环，数组的元素依次与后面的元素进行互换
# random.randint(m,n)：包括上下限，random.randrange(m,n)：不包括上限
# randint(m,n) 的实现方式通过调用 randrange(m,n+1) 实现的
for ms in range(m):
    mss = random.randrange(ms,m)
    music_repositories[ms],music_repositories[mss] = music_repositories[mss],music_repositories[ms]

for i in range(m-1):
    if music_repositories[i] + 1 == music_repositories[i + 1]:
        n += 1
print(music_repositories)
print(' {} 首歌随机播放，其中连续播放的有 {} 次，概率是：{:.2f}%'.format(m ,n ,(n/(m-1))*100 ))