# 龙形曲线（分形龙）  Dragon curve
print('龙形曲线（分形龙）  Dragon curve')
'''
规则：
指令为 F L R 字符的组合，意义如下：
    F -> 向前移动一个单元格并画直线
    R -> 表示“右转”
    L -> 表示“左转”
  0 阶：F
  1 阶：F L F
  2 阶：FLF L FRF
  3 阶：FLFLFRF L FLFRFRF
  .......
第 n 次迭代后，其指令字符串相当于第 n-1 次指令加上 L 再加上第 n-1 次指令的反向移动
'''

def Dragon_curve(n): # 参数 n 表示要迭代的次数
    
    dragon = 'F'
    
    if n == 0 :
        return dragon
        
    for times in range(n):
        oprations = []
                
        for turned in dragon[::-1]:
            if turned == 'L':
                oprations.append('R')
            elif turned == 'R':
                oprations.append('L')
            else:
                oprations.append('F')
    
        dragon = dragon + 'L' +  ''.join(oprations)
    
    return dragon

    
TIME = input('请输入迭代次数\n')
print(Dragon_curve(int(TIME))) 