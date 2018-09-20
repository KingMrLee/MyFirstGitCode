class Person():
    name = "noname"
    age = 0
    _petname = "sec" # 小名，是受保护的，子类可以用，但是不可以共用
    __score = 39 # 分数是private的，子类也不可以访问，只能自己知道
    def sleep():
        print("sleeping")
    # 定义一个人的工作
    def work(self):
        print("I am working,make some money")


# 定义一个教师类，父类是Person()
class Teacher(Person):
    teacher_id = '9527'
    name = '周星星'
    def sleep2(self):
        print("I am sleeping")
    def makeTest(self):
        print("start testing")
    def work(self):
        # 扩充父类的功能只需要调用父类相同的函数就可以了，这里self在调用时候传入的就是Teacher的对象t，self必须加上，
        # 注意和下面super().work()的区别
        Person.work(self)
        # super()代表得到父类 ，这里self不可以传，为什么？
        # super().work()
        self.makeTest()
# 可以看到这里继承Person()之后，t对象具有Person类中所有的属性和方法
t = Teacher()

# 当子类中定义的成员和父类中定义的成员名称冲突时，优先使用子类中的成员
print(t.name)
# 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，
t.work()