# 泰勒级数：用多项式逼近光滑的曲线
# Taylor series
# 计算机计算sinx,cosx...都是通过泰勒公式算的的近似值
# 本程序计算 e^x = 1 + x + x^2/2! + x^3/3! + ....


print('本程序是用于近似计算 e^x 的值')
x = int(input('请输入x的值：\n'))
n = int(input('请输入多项式的项数：\n'))

total = 1
term = 1
# 通过for循环计算出 x^n/n!,并累加求和
for i in range(1,n + 1):
    term *= x/i
    total = total + term
    print(total)
print(i)    
    
# 使用 while 循环可以省略一下不必要循环

total1 = 1
term1 = 1.0
n = 1

# 当 term1 的变化太小，在精准度内不在改变 total1 的值时，则中断循环
while total1 != total1 + term1:     
    term1 *= x / n
    total1 += term1
    n += 1
    print(total1)
print(n)

# 当x = 1 ， n = 50 时
# for循环运行50次
# while循环运行了19次（数值不在变化）
# 在此印证了循环体的开始条件选取是非常重要的，选的好可能事半功倍


# 三角函数 sinx = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - .....
# cosx = x - x^2/2! + x^4/4! - x^6/6! + x^8/8! - .....
# 同样的方法，可以使用泰勒公式进行计算，到数值不在变化时，结束循环