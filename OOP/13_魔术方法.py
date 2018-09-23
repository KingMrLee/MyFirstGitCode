'''
魔术方法
'''

class A():

    def __init__(self,name):
        self._name = name

    def __call__(self,name):
        print("哈哈，我是一个对象，被当做方法调用了，因为我用了魔法函数__call__")

    def __str__(self,name):
        return "我本来是对象，现在是用字符串打印出来了"

    
    def __getattr__(self, item):
        # 没找到的属性默认赋值为空
        self.item = None
    

    # 这里的两个参数key和value不会用，后续继续研究下
    def __setattr__(self, key, value):
        #         # self.key = key
        #         # self.value = value
        print("设置属性{0}为{1}".format(key,value))
        #         # 下面的语句会导致死循环
        #         # self.key = value
        super().__setattr__(key,value)



a = A("a")
# 把对象当做函数来调用
a("a")
print(a("a"))
# 没有属性age，在访问的时候赋值为None
# print(a.age)

# 打印出a中所有的方法，以dict字典方式显示
print(a.__dict__)
# print(a.Education)
a.Education = "大学本科"


'''
 - __gt__：进行大于判断的时候触发
        - self
        - 第二个参数是第二个对象
        - 返回值可以是任意值，推荐返回布尔值
'''
class Person():
    def __init__(self,name):
        self.name = name

    def __gt__(self, other):

        print("{0}会比{1}大吗？".format(self.name,other.name))
        return self.name >other.name

p1 = Person("one")
p2 = Person("two")
print(p1 > p2)
