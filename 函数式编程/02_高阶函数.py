'''
高阶函数
'''

from functools import reduce
# 函数名称就是一个变量

def funcA():
    print("In  funcA")

# funcA和funcB两个变量指向同一块内存地址
funcB = funcA
funcB()

# 高阶函数举例
# 假定funcAA是普通函数，返回一致传入数字的100倍

def funcAA(n):
    return 100 * n

def funcBB(n):
    return funcAA(n) * 3

print(funcBB(5))

# 上面的例子可以使用高阶函数实现，具体如下：
def funcCC(n,f):  # f是传递一个函数
    return f(n) * 3

print(funcCC(5,funcAA))

### map举例
list1 = [i for i in range(10)]
print(list1)

list2 = []
for i in list1:
    list2.append(i*10)

print(list2)

## 用map实现
def mulTen(n):
    return n * 10

list3 = map(mulTen,list1)   # map类型是可迭代的，可以使用for循环打印出结果

print(type(list3))
for i in list3:
    print(i)
print("*" * 30)
### reduce举例
def myAdd(x,y):
    return x+y

rst = reduce(myAdd,[1,2,3,4,5,6])
print(rst)