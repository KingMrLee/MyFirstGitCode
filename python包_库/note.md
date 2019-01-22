# 1、模块
- 一个模块就是一个包含python代码的文件，后缀名为.py，模块就是python文件
- 为什么要使用模块
    - 程序太大，编写维护不方便，需要拆分维护
    - 模块可以增加代码重复使用的方式，复用方便
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通python文件，任何代码可以直接写
    - 不过根据模块的规范，最好在模块中编写以下内容：
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码（方便使用模块的开发者测试功能）
- 如何使用模块
    - 模块直接导入
        - 加入模块名以数字开头，借助import  importlib 导入以数字开头的模块名称
    - 语法：
        impot module_name
        module_name.function_name
        module_name.class_name
    - import 模块 as 别名 ，之后可以直接使用别名
        - 导入的时候给模块起一个别名
        - 其余用法和上面一致
        - 案例就不写了，只是名字不同
    - from module_name import func_name,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
        - 案例p03_模块部分导入.py
    - from module_name import *   全部导入   
        - 这种导入方法不需要加前缀
        - 但是有前缀的写法可以清楚的看出是调用的哪个模块，防止命名冲突
        - 案例p04_全部导入
    - if __name__ == '__main__'
        - 可以有效避免模块代码被导入的时候被动执行的问题
        - 建议在入口中都加上上述代码
# 2、模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在哪些地方寻找模块
- 系统默认的模块搜索路径：
    - import sys
        sys.path  属性可以获取路径列表
    - 案例见p05_搜索路径.py
    - 添加搜索路径：
        sys.path.append(dir)
    - 模块的加载顺序：
        - 1、搜索内存中已经加载好的路径
        - 2、搜索python的内置模块
        - 3、搜索sys.path的路径
        
# 3、包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包，模块就是python文件
- 自定义包结构：
  
      |-- 包(Python Package，不是Directory)
      |--|-- __init__.py  包的标志性文件（有且只能有一个，在当前路径下）
      |--|-- 模块1
      |--|-- 模块2
      |--|-- 子包（子Python Package）
      |--|--|-- __init__.py  包的标志性文件
      |--|--|-- 子包模块1
      |--|--|-- 子包模块2
- 包的导入操作
    - import package_name
        - 注意这里的两种导入方法访问的内容是默认对__init__.py中内容的导入，实际情况下这个文件只是
        作为包的标志文件来使用，里面并没有内容，我们实际想调用的是包中其他的内容
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是：
            
                package_name.func_name
                package_name.class_name.func_name()
        - 此种方式的访问内容是：__init__.py中写的内容
        - 案例pkg01.py，p06_包的导入.py
    - import package_name  as p 别名
        - 具体用法跟作用方式，跟上述简单导入一致，只是使用的名称不一样
    - import package_name.module  从包中的具体模块中导入
        - 导入包中某一个模块
        - 使用方法：
        
                package_name.module.func_name
                package_name.module.class_name.func_name
                package_name.module.class_var
        - 案例见p08_包的导入（模块）.py
    - import package_name.module as pm   别名，与上述一致
    
- from ...... import 导入
    - from package_name import module1，module2，module3，.........
    - 此种方式导入的时候不执行__init__中的内容
        
            from pkg01 import p01 
            p01.sayHello
    - from package_name import  *
        - 导入当前包__init__.py文件中所有的函数和类，要注意这种导入方法导入的内容
        - 使用方法：
                
                func_name()
                class_name.func_name()
                class_name.var
        - 案例p09_包的导入（from语句导入*）.py
    - from package_name.module import * 
        - 导入包中指定的模块的所有内容
        - 使用方法：            
                
                func_name()
                class_name.func_name()
                class_name.var
- 在开发环境中经常会用到其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径、
- __all__ 的用法
    - 在使用from package_name import * 的时候，* 可以导入的内容，__all__可以做这个设置
    - __init__.py中如果为空，或者没有 __all__，那么可以把__init__中的内容导入（空的也导入）
    - __init__ 如果设置了 __all__ ，那么按照 __all__ 指定的子包或者模块进行导入，如此就不会载入
    __init__ 中其他未定义的内容了
        - __all__ = ['modele1','module2','module3',......]
    - 案例见p10_all的用法.py
# 命名空间
- 用于区分不同位置不同功能但是名称相同的函数或者变量的一个特定前缀
- 作用是防止命名冲突
        
        setName()
        Student.setName()
        Dog.setName() 
        所属各不相同
- 包的作用其实就好理解命名空间了，不同的包中展示出了相同类、相同方法、相同变量的所属。
        
    
    