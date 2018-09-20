'''
Mixin设计模式：就是编译的时候把一段代码复制到另一个地方的意思
    python 对于 mixin 命名方式一般以 MixIn, able, ible 为后缀。
    由于 mixin 是组合，因而是做加法，为已有的类添加新功能，而不像继承一样,下一级会覆盖上一级相同的属性或方法。
    但在某些方面仍然表现得与继承一样， 例如类的实例也是每个 mixin 的实例。
    mixin 使用不当会导致类的命名空间污 染，所以要尽量避免 mixin 中定义相同方法。
    对于相同的方法，有时很难区分 实例到底使用的是哪个方法。
下面的例子很经典，先记下来
【一个例子走近 Python 的 Mixin 类：利用 Python 多继承的魔力】
【https://blog.csdn.net/u012814856/article/details/81355935】

'''
class Mixin1(object):
    # 如果Myclass2中没有定义test方法，在c2调用的时候会不会调用Mixin2中的test方法呢，下面测试一下
    '''
    def test(self):
        print("mixin 1")
    '''
    def which_test(self):
        self.test()

class Mixin2(object):
    def test(self):
        print("mixin 2")

class MyClass1(Mixin1, Mixin2):
    pass                        # 按从左到右顺序从 mixin 中获取功能并添加到 MyClass

class Myclass2(Mixin1, Mixin2):
    # 如果Myclass2中没有定义test方法，在c2调用的时候会不会调用Mixin2中的test方法呢，下面测试一下
    '''
    def test(self):             # 已有 test 方法，因而不会再添加 Mixin1, Mixin2 的 test 方法
        print("my class 2")
    '''

'''
将之前案例都注释一下，重新写个案例
c1 = MyClass1()
c1.test()                       #  "mixin 1"
c2 = Myclass2()
c2.test()                       #  "my class 2"
c2.which_test()                 #  "my class 2"
print(isinstance(c1, Mixin1))          #  True
print(issubclass(MyClass1, Mixin2))    #  True
'''
# 这个案例可以看出来，c2和c3都是Myclass2类，他们的父类是Mixin1和Mixin2，在调用test方法时，优先调用本类中的test方法
# 当本类和Mixin1父类中找不到test方法的时候，会去Mixin2中去找test方法。
c3 = Myclass2()
c3.test()

'''
经典博客代码
'''
class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")

'''
经典解释：见有道云笔记Mixin设计模式
'''