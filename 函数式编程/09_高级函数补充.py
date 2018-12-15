'''
高级函数补充
'''
# 案例：将学生姓名和学生的得分组合在一起
# zip案例
import collections
from collections import deque
from collections import defaultdict
from collections import Counter

list1 = ["guolei","yangguojin","manan"]
list2 = [88,99,67]
list3 = zip(list1,list2)


for i in list3:
    print(i)

# enumerate
list4 = [11,22,33,44,55]
em = enumerate(list4)

list5 = [i for i in em ]
print(list5)

em2 = enumerate(list4,start=100)  # 从100开始

list6 = [i for i in em2]
print(list6)

'''
collections模块
'''
# 实例化namedtiple
Point = collections.namedtuple("point",['x','y'])
p = Point(11,22)
print(p)
print(p.x)
print(p.y)
print(p[0]+p[1])

#定义圆
Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,50,50)
print(c)
print(type(c))

# namedtuple 是tuple的实例
print(isinstance(c,tuple))

'''
deque
'''
q = deque(['a','b','c'])
print(q)

q.append('d')
print(type(q))
print(q)

q.appendleft('x')
print(q)

'''
defaultdict
当直接读取dict不存在的属性时，直接返回默认值
'''
d1 = {"one":1,"two":2,"three":3}
# lambda 表达式：返回一个字符串
func = lambda :"郭磊"
# 如果调用的dict中没有该属性，则调用func方法
d2 = defaultdict(func)
d2["one"] = 1
d2["two"] = 2
print(d2["one"])
print(d2["four"])

'''
Counter
- 统计字符串的个数，以对应字符串为键值
    - 需要括号里的内容是可迭代的
'''
c = Counter("asdfsdfsdfsdafadfasd")
print(c)

s = ["guolei","love","love","hahaha"]
c1 = Counter(s)
print(c1)