'''
06_闭包结构经典案例-大坑
出现的问题：
- 造成下属状况的原因是：返回函数引用变量i，i不是立即执行的，而是等到三个函数都返回的时候才统一使用，此时i已经是3了，所以打印结果如下
- 此问题可以发现：返回闭包时，返回函数不能引用任何循环变量
- 解决方案：再创建一个函数，用该函数参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变
'''

def count():
    # 定义一个空list，用于存放返回值
    fs = []
    for i in range(1,4):
        def myF5():
            return i*i
        fs.append(myF5)

    return fs

print(count())
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())


# 解决方案
def count2():

    def f(j):
        def myF6():
            return j*j
        return myF6
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

print(count2())
f4,f5,f6 = count2()
print(f4())
print(f5())
print(f6())



