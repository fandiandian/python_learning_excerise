# unicode编码：9800 到 9812 对应的字符为 12 星座的符号
# 使用的是 chr() 函数
# cmd中显示是存在乱码，需要改变字体，就可正常显示：SimSun-ExtB 这款字体就可以正常显示

# chr(number) : 将 数字 转换成对应的 unicode编码中 所对应的 字符
# ord(number) : 将 字符 转换成对应的 unicode编码中 所对应的 数字

# 例如：在 unicode 中： "♉" 对应 9801
print(chr(9801))
print(ord("♉"))

ii = '白羊座、金牛座、双子座、巨蟹座、狮子座、处女座、天秤座、天蝎座、射手座、摩羯座、水瓶座、双鱼座'
iii = ii.split("、")
for i in range(12):
    print('{} --> {}'.format(iii[i],chr(9800 + i)))
    
'''   
白羊座 --> ♈
金牛座 --> ♉
双子座 --> ♊
巨蟹座 --> ♋
狮子座 --> ♌
处女座 --> ♍
天秤座 --> ♎
天蝎座 --> ♏
射手座 --> ♐
摩羯座 --> ♑
水瓶座 --> ♒
双鱼座 --> ♓
'''