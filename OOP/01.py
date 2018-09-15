'''
类的定义
'''
# 定义一个空类
class Student():
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，表示听python的类
class  PythonStudent():
    # 用None赋值
    name = None
    age = 8
    course = "python"

    # 系统默认有一个self参数
    # 方法需要与变量齐平
    def dohomework(self):
        print("我在做作业")
        # 推荐在函数末尾使用return语句
        return None

# 实例化
guolei = PythonStudent()
print(guolei.name)
print(guolei.age)
# 注意这里调用方法的时候没有传入参数，是可以使用的
guolei.dohomework()