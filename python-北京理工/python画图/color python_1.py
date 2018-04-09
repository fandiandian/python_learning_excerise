# python 绘制 python
# 主要使用turtle模块

import turtle
import random

# turtle支持RGB,好像是0到1之间的分配，构造颜色随机函数
def RGBcolor():
    return tuple([random.randint(0,255) for i in range(3)])  # randint(a,b),取上下限，即： a <= x <= b
turtle.colormode(255) # 切换rgb模式
# setup():前两个参数用于确定画板窗体的规格（长*宽 = 600*350），后面为窗体的左上角与屏幕的左上角的相对位置（像素)-->向右100，向下50
# 如果后面的两个参数不加，则会在屏幕的中间位置
turtle.setup(1000, 600,100,50)
turtle.speed(10)  # 画笔的移动的速度，1到10之间，1最慢，10最快
turtle.penup()   # 画板在创建好了之后，画笔会出现在画板的中间，抬起画笔
turtle.goto(-420,-50)  # 将画笔向后移动470个像素
turtle.pendown() # 放下画笔
turtle.hideturtle() # 隐藏画笔（那个三角箭头）
turtle.pensize(30)  # 画笔的粗细
turtle.pencolor(RGBcolor()) # 画笔的颜色，支持RGB颜色
turtle.fd(10)
turtle.pencolor(RGBcolor())
turtle.seth(-90)   # 画笔的方向逆时针旋转50度，负的代表正时针旋转50度：：默认（default)的是0度，水平向右开始画
for i in range(4):  # 循环,画出彩色的
    for j in range(1, 11):  # 循环分段画，一个半圆弧分成10份，每份所对应的圆心角为18度
        turtle.pencolor(RGBcolor())
        turtle.circle(40, 18)  # 画圆弧，半径为40，圆心角为180度，半径为正，逆时针开始画，为负顺时针开始画
    for k in range(1, 11):
        turtle.pencolor(RGBcolor())
        turtle.circle(-40, 18)  # 顺时针画圆弧
for i in range(5):  # 逆时针转90度，使画笔的方向转为水平向右
    turtle.pencolor(RGBcolor())
    turtle.circle(40, 18)
for i in range(10): # 向前画100个像素
    turtle.pencolor(RGBcolor())
    turtle.fd(10)
for i in range(18): # 画半个圆
    turtle.pencolor(RGBcolor())
    turtle.circle(40, 10)
for i in range(5): # 向前画100个像素
    turtle.pencolor(RGBcolor())
    turtle.fd(10)
turtle.penup()
turtle.goto(-180,100)   # 将画笔到指定的像素点，以设置的画版的中间为原点，即可确定相对的位置
turtle.pendown()
# turtle.write(s [,font=("font-name",font_size,"font_type")])
# 写文本，s为文本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项
s = 'color python'
for i in range(len(s)):  # 写字
    turtle.pencolor(RGBcolor())
    turtle.write(s[i],font=('consolas', 50, 'normal'))
    turtle.penup()
    turtle.goto((-180+35*(i+1)),100) # 每写一个字，将画笔向右移动一定的距离
    turtle.pendown()
turtle.done()   # 函数图像完成会之后，不会自动退出，需要手动关闭画布窗口，无此函数，在完成绘制后，会自动退出
