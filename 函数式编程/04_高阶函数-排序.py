'''
高阶函数-排序
A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
可以提供一个自定义键函数来自定义排序顺序
反向标志可以设置为按降序请求结果
'''

# reverse默认是Flase，即是升序：从小到大，True是反过来，降序：从大到小
a = [322,455,634,654,75,757675,545,3,53,]
al = sorted(a,reverse=True)
print(al)

# 排序案例2-
# 按照绝对值进行排序
# abs是求绝对值的意思
# reverse = True是按照绝对值倒序排列

a2 = [-23,-44,55,34,5656.757,-6766]
al2 = sorted(a2,key=abs,reverse=True)
print(type(al2))
print(al2)

# sorted 案例3
# 字符串排序
astr = ['guollei','dana','Huangwen','yangguojin']

str1 = sorted(astr)
print(str1)

str2 = sorted(astr,key=str.lower)
print(str2)

