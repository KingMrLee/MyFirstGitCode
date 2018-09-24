'''
 - from module_name import *   全部导入
        - 这种导入方法不需要加前缀
        - 但是有前缀的写法可以清楚的看出是调用的哪个模块，防止命名冲突
'''
from p01 import *
stu = Student()
stu.say()
sayHello()