'''
装饰器
- 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数。
- 装饰器的使用：使用@语法，即在每次要扩展到函数定义前使用@+函数名
'''
# 要打印时间需要先导入时间模块
import time

def hello():
    print("helloworld")

f = hello
print(f.__name__)
print(hello.__name__)


# 现在有一个新的需求：对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# 使用装饰器
'''
定义一个装饰器：写法固定，不理解暂时先记住
'''
def printTime(f):
    def wrapper( *args, **kwargs):
        print("Time:",time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 使用的时候@+函数名放在需要装饰的方法之前，是python的语法糖，感觉放在前面就是贴在这个方法hello2的前面，调用的时候作为整体调用
@printTime
def hello2():
    print("Helloworld!!!")

hello2()

# 上面对函数的装饰使用了系统定义的语法糖，下面开始手动执行下装饰器

def hello3():
    print("Helloworld3，我是手动执行的")

hello3()
hello3 = printTime(hello3)
hello3()



