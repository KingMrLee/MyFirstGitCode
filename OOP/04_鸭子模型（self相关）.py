'''
鸭子模型
'''

class A():
    name = "wangxiaojing"
    age = 34

# 这是一个内置函数
    def __init__(self):
        self.name = "guolei"
        self.age = 24

    def say(self):
        # self.name = "mama"   这个模型中这里不能设置指定的值，某则下面代码输出结果一样，因为不论传什么参数进来，这里都重新赋值了
        # self.age = 48
        print(self.name)
        print(self.age)


class B():
    name = "bbbbb"
    age = 1000

a = A()
b = B()
# 此时，系统会默认把a作为第一个参数传入函数，所以这样调用时没问题的
print("*"* 50)
a.say()
print("*"* 50)

# 下面的传入参数的方法可以看出来，python中类去调用对应类中的方法时，传入的参数可以是对象a，可以是类A，可以是类B。当有self
# 的时候，不可以传空，见A.say()；当没有self的时候，只能用类名调用，可以使用A.say()
# A.say()
A.say(a)
print("*"* 50)
A.say(A)
print("*"* 50)
A.say(b)
print("*"* 50)

