'''
filter案例：
对于一个列表，对其进行过滤，偶数组成一个新的list
需要定义过滤函数
过滤函数要求有输入，返回布尔值。
'''

def isEven(a):
    return a % 2 == 0  # 返回偶数

list1 = [1,2,3,4,5,6,7,8,77,88,99,100]

rst = filter(isEven,list1)
print(type(rst))
print(rst)
print([i for i in rst])