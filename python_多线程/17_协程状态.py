'''
协程状态
'''

def simple_coroutine(a):
    print("coroutine starting")
    # b接受send传回来的值
    b = yield a

    print("-------->recived",a,b )
    c = yield  a+b

    print("-------->recived",a,b,c)
    d = yield a+b+c

g = simple_coroutine(5)
# 预激
aa = next(g)
# 先遇到yield，返回a赋值给aa，打印
print(aa)
# 然后send发送了6 赋值给b，然后执行了print("-------->recived",a,b )，又遇到yield，返回了a+b = 11
bb = g.send(6)
print(bb)
# 最后又send7给到c，然后执行print("-------->recived",a,b,c)，又遇到yield，返回了a+b+c = 18
cc = g.send(7)
print(cc)
