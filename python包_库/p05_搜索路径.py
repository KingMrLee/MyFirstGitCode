'''
搜索路径
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在哪些地方寻找模块
- 系统默认的模块搜索路径：
    - import sys
        sys.path  属性可以获取路径列表
    - 案例见p05_搜索路径.py
    - 添加搜索路径：
        sys.path.append(dir)
'''
import sys

# sys.path是list列表类型，可以使用append()方法来添加搜索路径
print(type(sys.path))
for p in sys.path:
    print(p)



