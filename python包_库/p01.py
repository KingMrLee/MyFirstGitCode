'''
包含一个学生类，一个sayHello函数；一个打印语句
'''

class Student():
    def __init__(self,name = "NoName",age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("hi,how are you")

# 当是本身文件中作为主进程调用的时候才会执行print语句，这样在其他文件中导入p01的时候就不会打印这个语句了
# 此判断语句建议一直作为程序调用的入口
if __name__ == '__main__':
    print("我是第一个模块文件p01.py")
