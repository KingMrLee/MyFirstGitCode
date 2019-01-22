'''
迭代器和可迭代对象
'''

from collections import Iterable
from collections import Iterator
# 可迭代对象
l = [i for i in range(6)]
for index in l:
    print(index)

# 迭代器，range()函数就是一个迭代器
for i in range(10):
    print(i)

# isinstance案例
ll = [1,2,3,4]
s = 'I love yuyu'
print(isinstance(ll,Iterator))
print(isinstance(ll,Iterable))

# 将ll转换之后就成为迭代器了
LL_iterator = iter(ll)

print(isinstance(LL_iterator,Iterator))
print(isinstance(LL_iterator,Iterable))

