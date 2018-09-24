'''
测试 __all__的用法，导入pkg02的包
'''
from pkg02 import *

# 因为pkg02中的 __init__.py文件中的 __all__中定义好了调用模块p01_学生模块，所以这里可以直接创建
stu = p01_学生模块.Student()
stu.say()

# 调用pkg02中__init__.py里定义的inInit()方法来检测这里是否调用了 __all__定义之外的方法或者模块
# 报错name is not defined
inInit()


