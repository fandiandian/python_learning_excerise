# 计算圆周率
# 并用turtle画出随机点出现的过程

import turtle as t
from random import random
from time import perf_counter

times = 100 * 100
hits = 0

start = perf_counter()
t.setup(1000,500,100,50)
t.pensize(1)
t.color('black')
t.begin_fill()
for i in range(4):
    t.fd(200)
    t.left(90)
t.end_fill()
t.fd(200)
t.left(90)
t.pencolor('white')
t.circle(200,90)
t.hideturtle()
    
for i in range(times + 1) :
    x,y = random(),random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1 :
        hits += 1
        t.pencolor("yellow")
        t.pu()
        t.goto(x*200, y*200)
        t.pd()
        t.dot(2.5)
    else :
        t.pencolor("red")
        t.pu()
        t.goto(x*200, y*200)
        t.pd()
        t.dot(2.5)
pi = 4 * hits / times 
t.pu()
t.goto(-350,215)
t.pencolor('blue')
t.write('圆周率是：{:^14.12f},程序运行的时间是：{}'.format(pi,perf_counter() - start), font=('Arial', 18, 'normal'))
t.done()


