# 写在前面的话
    - 邮箱
        - 会使用python发送邮件
        - 对邮箱进行设置，通过邮箱地址和授权码就能发送邮件
- 前端知识的学习

# OOP-python 面向对象
    - python面向对象编程
        - 基础
        - 公有私有
        - 继承
        - 组合，Minxi
     - 魔法函数
      - 魔法函数概述
      - 构造类魔法函数
      - 运算类魔法函数
      
# 1、面向对象概述（object Oriented,oo）
    - oop 思想
    - 几个名词：
        - oo：面向对象
        - ooA：面向对象的分析
        - OOD：面向对象的设计
        - OOI：面向对象的实现
        - OOP：面向对象的编程
        - OOA—>OOD—>OOI：面向对象的实现过程 
        
    - 类和对象的概念
        - 类：抽象名词，代表一个集合，共性的内容
        - 对象：具象的事物，单个个体
        - 类和对象的关系
            - 一个对象是一个类的实例化
    - 类的内容
        - 表明事物的特征，叫做属性（变量）
        - 表明事物的功能或者动作，称为成员方法（函数）
        
# 2、类的基本实现
    - 类的命名
        - 遵守变量的命名规则
        - 大驼峰，由一个或者多个单词构成，单词首字母大写
        - 尽量避开系统使用的一些命名
     - 如何声明一个类
        - 必须使用class关键字
        - 类由属性和方法构成，其他不允许出现
        - 成员属性定义可以直接使用变量赋值，如果没有值，则赋值为None
        - 案列 01.py 
    - 实例化
        - 变量 = 类名（）# 实例化一个对象
    - 访问对象成员
        - 使用.操作符
            obj.成员属性名称
            obj.成员方法
    - 可以通过内置默认变量检查类和对象的所有成员
        - 对象所有成员检查
            # dict前后有两个_
            obj.__dict__
        - 类所有的成员：
            # dict前后有两个_
            class_name.__dict__            

# 3、anaconda 基本使用
    - anaconda主要是一个虚拟环境管理器
    - 还是一个安装包管理器  
    - conda list ：显示anaconda安装的包
    - conda env list 显示anaconda 的虚拟环境列表  
    - conda create  -n xxx python=3.6 ：创建python版本为3.6的虚拟环境，名称为xxx