'''
属性
'''
# 创建Student类，描述学生类，学生具有Student.name属性，但是name格式并不统一
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # 不用重新调用方法，这里可以在构造函数中直接调用，对name做格式化
        self.setNmae(name)

    def intro(self):
        print("I am {0},I am {1} years old".format(self.name,self.age))

    def setNmae(self,name):
        self.name = name.upper()

s1 = Student("guolei",24)
s2 = Student("yangguojing",24)
s1.intro()
s2.intro()

'''
property案例
定义一个Person类，有name,age属性
需求：1、对于任意输入的姓名，希望用大写方式保存；
      2、年龄用统一整数保存
x = property(fget,fset,fdel,doc) 
'''
class Person():
    '''
    这是一个人的类
    '''
    def fget(self):
        return self._name

    def fset(self,name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget,fset,fdel,"这是对name的初始化数据清洗操作")

p1 = Person()
p1.name = "huangwen"
print(p1.name)

'''
# 类的内置属性
- __dict__：以字典的方式显示类的成员组成
- __doc__：获取类的文档信息
- __name__：获取类的名称，如果在模块中使用，获取模块的名称
- __bases__：获取某个类的所有父类，以元组的方式显示 
'''

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)

