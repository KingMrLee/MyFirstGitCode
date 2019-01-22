'''
生成器
'''

L = [ x*x for x in range(5) ]
# 这是最简单的生成器案例，在括号中，这种格式的
g = (x*x for x in range(5) )

print(type(L))
print(type(g))

# 因为odd()函数中有yield关键字，所以这个函数是一个生成器
# yield 关键字就是，当前生成器中，在发现这个关键字时，返回yield后面的值，然后会记录下函数odd()执行的状态，
# 再次调用时，继续往下执行
def odd():
    print("step1")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3

# 案例1；每次都生成生成器的时候，都是从入口处执行
'''
结果如下：
    step1
    1
    step1
    1
    step1
    1
'''
one = next(odd())
print(one)
two = next(odd())
print(two)
three = next(odd())
print(three)

# 案例2；只生成一个生成器，记录执行状态，继续执行
'''
结果如下：
    step1
    1
    step2
    2
    step3
    3
'''
gg = odd()
one = next(gg)
print(one)
two = next(gg)
print(two)
three = next(gg)
print(three)

# for循环调用生成器，如下样例
ggg = odd()
for i in  range(6):
    rst = next(g)
    print(rst)
