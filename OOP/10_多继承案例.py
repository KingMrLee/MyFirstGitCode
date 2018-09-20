'''
单继承和多继承
'''


# 多继承的案例中，子类拥有父类的所有方法，private的属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name

    def swim(self):
        print("I am swimming")

class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print("I am flying")

class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("I am working")

# 这个类的父类是Person、Fish、Bird
# SuperMan()括号内的父类名顺有要求，MRO算法，保证多继承中不会出现菱形问题，
class SuperMan(Bird,Person,Fish):
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name):
        self.name = name


s = SuperMan("guolei")
s2 = Student("wangxiaoyu")
s.work()
s.fly()
s.swim()
# 单继承调用
s2.work()


'''
菱形问题
'''
class A():
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass
