'''
time模块
只例举几个方法，待具体使用详细的方法的时候，再查资料深入了解
'''
import time

# 时间模块的属性
# timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔，东八区是-28800
# altzone:当前时区和UTC时间相差的秒数，在有夏令时的情况下的间隔，是-32400
print(time.timezone)
print(time.altzone)

# 得到时间戳
print(time.time())

# 获取当前时间,可以通过点号操作符河道相应的属性元素，如tm_hour
print(time.localtime())
print(type(time.localtime()))
print(time.localtime().tm_hour)

# sleep()是程序进入睡眠，n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)

# strftime：将时间元组转换为自定义的字符串格式
# Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。

