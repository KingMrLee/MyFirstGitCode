'''
构造函数
'''

class Animal():
    def __init__(self):
        print("Animal")

class PaXingAnimal(Animal):
    def __init__(self,name):
        print("PaXingAnimal {0}".format(name))

class Dog(PaXingAnimal):
    def __init__(self):
        # __init__就是构造函数
        # 每次实例化的时候第一个被自动调用
        # 主要的作用是进行初始化，构造函数的写法是固定的，至少有一个参数self
        print("I am init in dog")
# 运行时候会直接打印出print中的内容
# 实例化的时候，括号内的参数需要跟构造函数参数匹配；会直接调用Dog中的构造函数，，没有调用父类PaXingAnimal中的构造函数
kaka = Dog()

# 继承中的构造函数

class Cat(PaXingAnimal):
    pass

# Cat中没有构造函数，此时应该调用父类PaXingAnimal中的构造函数，没有再向上查找Animal中的构造函数了
# 参数要匹配，下面这么调用就不可以了
# c = Cat()
# 正确的应该传入两个参数如下：
c = Cat("Cat")


