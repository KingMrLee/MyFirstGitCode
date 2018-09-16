'''
self的含义和使用，鸭子模型见04.py
'''


class Student():
    name = "dana"
    age = 23

    # 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaa"
        self.age = 100
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))

    def sayAgain(s):
        # s.name = "aaa"
        # s.age = 100
        print("my name is {0}".format(s.name))
        print("my age is {0}".format(s.age))

print("*"* 50)
guoleilei = Student()
# 这里没有传入任何参数，但是实际上是默认传入self的，即传入第一个参数self到这个对象定义的say方法中
guoleilei.say()
# 这里可以看出，如果在定义方法的时候，定义了形式参数s,但是传入参数的时候没有传入参数，那么会把对象传进去，
# 即会调用guoleilei对象的本身self.name和self.age传入s.name和s.age输出。
guoleilei.sayAgain()
print("*"* 50)
class Teacher():
    name = "dana"
    age = 23

    # 注意say的写法，参数有一个self
    def sayTeacher(self):
        self.name = "aaa"
        self.age = 100
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
        print(__class__.name)
        print(__class__.age)

    def sayTeacherAgain():
        # 这里访问的就是Teacher类中的name和age了，
        # 使用类访问绑定类的方法时，如果累方法中需要访问当前类的成员，可以通过
        #     __class__.成员名
        print(__class__.name)
        print(__class__.age)
        print("hello,I am your teacher")

t = Teacher()
t.sayTeacher()
# 这里因为sayTeacherAgain()中没有传入self，所以不能这样调用
# t.sayTeacherAgain()
# 正确的调用应该是这样的，调用绑定类函数的时候要使用类名调用。
Teacher.sayTeacherAgain()
print("*"* 50)


