'''
自定义类
'''

'''
用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，而是在内存中创建一个link指向外部的方法，
在创建实例的时候这个link也会被复制。

本文来自 yuanyangsdo 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/yuanyangsdo/article/details/60776612?utm_source=copy 
'''
import abc

from types import MethodType

class Student(object):
    pass

def set_name(self, name):
    self.name = name

s1 = Student()
s2 = Student()
s3 = Student()
#将set_name方法绑定到s1实例上
s1.set_name = MethodType(set_name,Student)
s2.set_name = MethodType(set_name,Student)
s1.set_name('tom')
s2.set_name('tony')
print(s1.name)
print(s2.name)
# 这里两个name一致是因为set_name是共有的，类似于static的概念，s1先设置为tom，s2又将name设置为tony了

'''
借助type创建一个类
感觉这种方法也很复杂啊，为什么不直接定义呢，这里还是写一下这个知识点吧
语法：
    class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
'''

def say(self):
    print("saying")

def talk(self):
    print("talking")

# 这里第二个参数是一个元组，一个元素的时候后面需要有个逗号,
B = type("MyName",(object,),{"My_say":say,"My_talk":talk})

print(type(B))
b = B()
b.My_say() #  如果是b.say()，这里会报错“'MyName' object has no attribute 'say'”，因为类中的方法名字是My_say
b.My_talk()

'''
可以利用元类实现：Metaclass
'''

class TulingMetaClass(type):
    # 注意以下的写法
    def __new__(cls,name,bases,attrs):
        # 自己的业务处理
        print("哈哈哈，我是元类啊")
        attrs['id'] = '000000'  #元类中定义id，继承之后也有这个属性
        attrs['addr'] = "北京海淀区" # 元类中定义地址，继承之后也有这个属性
        return type.__new__(cls,name,bases,attrs)

# 元类定义完就可以使用，注意写法：
class Teacher(object,metaclass=TulingMetaClass):
    pass

t = Teacher()
print(t.__dict__)
print(t.id)
print(t.addr)

