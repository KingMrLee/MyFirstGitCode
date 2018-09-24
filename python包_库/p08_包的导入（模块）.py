'''
- import package_name.module  从包中的具体模块中导入
        - 导入包中某一个模块
        - 使用方法：
            package_name.module.package_name.module.func_name
            package_name.module.class_nameclass_var
'''

import  pkg01.p01_学生模块

stu = pkg01.p01_学生模块.Student()

stu.say()
pkg01.p01_学生模块.sayHello()

