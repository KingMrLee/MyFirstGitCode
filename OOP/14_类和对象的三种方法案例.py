'''
# 8、类和对象的三种方法 见14_类和对象的方法.py
- 实例方法
    - 需要实例化对象才能使用的方法
- 静态方法
    - 不需要实例化，通过类直接访问
- 类方法
    - 不需要实例化，传入对象
'''

class Person():
    name = "dana"
    # 实例方法
    def eat(self):
        print(self)
        print("eating")

    # 类方法 类方法的第一个参数，一般命名为cls，与self区别
    # @classmethod
    def play(cls,x):
        print(cls)
        print(cls.name * x)

    # 静态方法
    # 不需要使用第一个参数表示自身或者类
    # @staticmethod
    def say():
        print("saying")

    def add(a,b):
        print(a + b)

guolei = Person()

# guolei 可以访问实例方法
guolei.eat()
# 类方法
Person.play(guolei,3)
guolei.play(2)
# 静态方法
Person.say()


