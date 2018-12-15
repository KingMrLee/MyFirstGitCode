'''
- 与操作系统相关，主要是文件操作
- 与操作系统相关的操作，主要包含在三个模块里
    - os 操作系统目录相关
    - os.path 系统路径相关操作
    - shutil 高级文件操作，目录树的操作，文件赋值，删除，移动
'''

import os

# getcwd() 获取当前的工作目录
# 格式：os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作时，默认查找文件的目录

mydir = os.getcwd()
print(mydir)

# chdir() 改变当前的工作目录
# 格式：os.chdir(path)
# 返回值：无
os.chdir('/home/mydirtest') #改变的这个目录需要存在，否则报错
mydir = os.getcwd()
print(mydir)

# listdir() 获取一个目录中所有子目录和文件夹的名称列表
# 格式：os.listdir(path)
# 返回值：所有子目录和文件夹的名称列表
os.listdir()

# makedirs() 递归创建文件夹
# 格式：os.makedirs(递归的路径)
# 详细可以使用help(os.makedirs)查看详细参数以及使用方法

# getenv()获取指定的系统环境变量值

