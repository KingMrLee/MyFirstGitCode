'''
面向对象
'''
class Person():
    # name是共有的成员
    name = "guolei"
    # age是私有成员
    __age = 23


p = Person()
print(p.name)
# 这里可看出来私有变量是不可以被访问到的，注意报错信息说的意思是没有这个属性__age
# print(p.__age)
# 可以这样来访问，注意Person__age的前面只有一个下划线_
print(p._Person__age)
# 或者通过类的成员检测来访问到
print(Person.__dict__)