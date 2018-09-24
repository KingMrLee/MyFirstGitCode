'''
- from package_name import  *
        - 导入当钱包__init__.py文件中所有的函数和类，要注意这种导入方法导入的内容
        - 使用方法：

                func_name()
                class_name.func_name()
                class_name.var
'''

from pkg01 import *

# 这个方法是 __init__.py中定义的方法，在这里是被调用了的
inInit()

# 这是在模块p01_学生模块中定义的方法，但是这里没有调用
sayHello()
