# python 使用 turtle 模块绘制五角星

import turtle as t
import random

def rgb_color():    # RGB颜色
    return tuple([random.randint(0,255) for i in range(3)])
def star(lenght):   # 画一个五角星
    for i in range(5):
        t.fd(lenght)
        t.left(72)
        t.fd(lenght)
        t.right(144)
t.colormode(255)    # 颜色模式，使用0-255
t.pensize(1)
t.hideturtle()
t.pu()
t.goto(-130.9016994,19.155534)  # 将起始点移至固定位置
t.pd()

for i in range(5):  # 画五个同心五角星，并填充颜色
    t.color(rgb_color())    # t.color(pen_color,fill_color),有两个参数，一个是笔的颜色，一个是填充的颜色
    t.begin_fill()
    star(200-40*i)
    t.end_fill()
    t.pu()
    t.right(18)
    t.fd(27.5276384*2)
    t.left(18)
    t.pd()
    
t.done()
