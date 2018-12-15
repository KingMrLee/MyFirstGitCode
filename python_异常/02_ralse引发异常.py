'''
raise 引发异常
'''


try:
    print("我爱你")
    print(222222)
    raise ValueError
    print("手动引发异常")
except NameError as e:
    print("名字输入有问题")
    print(e)
    exit()
except AttributeError as e:
    print("属性有问题")
    print(e)
    exit()
except ValueError as e:
    print("Value Error")
    exit()
except BaseException as e:
    print("不知道什么异常，直接输出")
    print(e)
finally:
    print("我一定会被执行的")
'''

'''
# 自己定义异常
# 需要注意：自定义异常必须是系统异常的子类


class GuoLeiError(ValueError):
    pass

try:
    print("我爱你")
    print(222222)
    raise GuoLeiError
    print("手动引发异常")
except NameError as e:
    print("名字输入有问题")
    print(e)
    exit()
except AttributeError as e:
    print("属性有问题")
    print(e)
    exit()
except ValueError as e:
    print("Value Error")
    exit()
# 如果没有下面的捕获语句，会捕获父类ValueError，ValueError没有的时候，捕获BaseException
except GuoLeiError as e:
    print("GuoLei Error")
    print(e)
except BaseException as e:
    print("不知道什么异常，直接输出")
    print(e)
finally:
    print("我一定会被执行的")


'''
# else语句执行案例
'''

try:
    num = int(input("please  input  your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(num))
except BaseException as e:
    print("异常了")
else:
    print("没有异常")
finally:
    print("我一定会被执行")
