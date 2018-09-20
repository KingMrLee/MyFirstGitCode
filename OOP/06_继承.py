'''
继承
'''

# 在python中，任何类都有一个object父类
class Person():
    name = "noname"
    age = 0
    _petname = "sec" # 小名，是受保护的，子类可以用，但是不可以共用
    __score = 39 # 分数是private的，子类也不可以访问，只能自己知道
    def sleep():
        print("sleeping")


# 定义一个教师类，父类是Person()
class Teacher(Person):
    teacher_id = '9527'
    def sleep2(self):
        print("I am sleeping")
    def makeTest(self):
        print("start testing")
# 可以看到这里继承Person()之后，t对象具有Person类中所有的属性和方法
t = Teacher()
'''
print(t.name)
print(t.age)
print(Teacher.name)
print(Teacher.age)
# 有self的时候下面这样调用不可以，绑定的类中方法，子类不可以调用，Person类才可以
# print(Teacher.sleep(self))
print(Person.sleep())
# 类本身才可以调用绑定的方法，也就是没有self的方法，对象可以调用有self的方法，没有的不可以调用
print(t.sleep2())
'''

# 子类可以调用父类中protected的成员_petname，但是不可以调用private的成员__score
print(t._petname)
# print(t.__score)
# 子类继承父类之后并没有将父类成员完全复制到子类中，而是通过引用关系访问调用，与java中的引用一样
# 子类引用指向父类的成员
print(id(t._petname))
print(id(Person._petname))



