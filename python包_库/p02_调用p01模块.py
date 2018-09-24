'''
    impot module_name
    module_name.function_name
    module_name.class_name
'''

# 导入p01模块，在这里导入的时候，相当于把p01中的代码copy过来了，然后运行一遍，所以会先输出print语句，所以模块中外部不建议写print语句，
# 每当导入模块的时候，都会print
# impot module_name
# module_name 遵循变量命名的规则
# 借助import  importlib 导入以数字开头的模块名称
# 语法：Tuling = importlib.import_module("01")
import p01

# module_name.class_name
stu = p01.Student("xiaojing",19)
stu.say()

# module_name.function_name
p01.sayHello()


