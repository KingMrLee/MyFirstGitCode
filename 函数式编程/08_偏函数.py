'''
偏函数
'''
import _functools
# 把字符串转换成十进制数字

print(int("123456"))  # int()函数将字符串转换成int

# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字
'''
class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
'''
def int16(x,base = 16):
    return int(x,base )

print(int16("123456"))  # 传入的参数不传base的时候，就默认是16进制，即字符串“123456”对应的十六进制数字是 1193046

# 偏函数，在这里就是把int函数中原来默认base = 10 改为base = 16，以后调用这个方法就是直接16进制转换
init16 = _functools.partial(int,base = 16)