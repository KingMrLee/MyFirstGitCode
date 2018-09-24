'''
模块部分导入
- from module_name import func_name,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
'''

from p01 import Student,sayHello

stu = Student()
stu.say()
sayHello()