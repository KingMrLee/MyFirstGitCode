'''
抽象类
- 抽象方法：没有实现内容的方法就是抽象方法
- 抽象方法的主要意义是规范了子类的行为和接口
- 抽象类的使用需要借助abc模块
    - import abc
- 抽象类：包含抽象方法的类叫做抽象类，通常称为abc
在父类中不实现方法，在子类中实现，多态
'''

'''
class Animal():

    def sayHello(self):
        pass

class Dog(Animal):

    def sayHello(self):
        print("闻一下对方")

class Person(Animal):

    def sayHello(self):
        print("hi,how are you")

dog = Dog()
dog.sayHello()
person = Person()
person.sayHello()
'''

import abc

# 声明一个类并且制定当前类的元类
class Hunman(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义抽象类的方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态的抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("sleeping")

class Person(Hunman):

    def smoking(self):
        print("smoking")

    def drink(cls):
        print(cls)
        print("drinking")

    def play(self):
        print("playing")


p = Person()
p.smoking()
#  Person.smoking() 实例方法是不能通过类调用的，没有self，有self的方法不可以通过类名调用
print("*"*30)
p.drink()
Person.drink(p)
print("*"*30)
p.play()
Person.play(p)

