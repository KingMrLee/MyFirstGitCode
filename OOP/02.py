'''
类的基本定义和使用
'''

# 类的所有成员检查
class Student():
    name = "guolei"
    age = 18


print(Student.__dict__)  # 查看类Student中的成员（属性、方法）

# 实例化，对象的成员检查
yueyue = Student()
print(yueyue.__dict__) # 可以看出，虽然yueyeu对象的成员检查为{}空，但是因为她是Student类，所有具有Student类的两个属性，即name和age
print(yueyue.age)
print(yueyue.name)

# 这个案例可以看出来，实例a中name和age的id一样，值也是一样，说明a中age和name指向的内存就是类A中age和name的内存地址。
# 类的属性和其对象的属性，如果对象中没有对对象的属性做更改，则对象的属性和类的属性指向是同一块内存地址，可以理解为指向同一个变量
class A():
    name = "dana"
    age = 23

    # 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaa"
        self.age = 100

print("*"* 30)
print(A.name)
print(A.age)
print("*"* 30)

print(id(A.name))
print(id(A.age))
print("*"* 30)

a = A()
print(A.__dict__)
print(a.__dict__) # 给a对象的name和age赋值之前查看成员是{}，没有的
print(id(a.name))
print(id(a.age))
print("*"* 30)

a.name = "guolei"
a.age = 99
print(a.__dict__) # 在给a中name和age赋值之后，a中的成员检查就是有值的了
print(a.name)
print(a.age)
print(id(a.name)) # 会发现重新给a对象中的name和age赋值之后，id是不同的
print(id(a.age))
print("*"* 30)


