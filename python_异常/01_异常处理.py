'''
异常处理
'''

'''
# 简单的异常处理
try:
    num = int(input("please  input  your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(num))
except :
    print("输入的数据不合法，请重新输入")
    # exit()是程序退出的意思
    exit()
'''

# 简单的异常处理
# 给出提示信息
try:
    num = int(input("please  input  your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(num))
# 捕获异常之后，把异常实例化，异常信息也会在实例里面
# 注意以下写法：
# 如果是多种error的情况，需要把越具体的错误，越往前放。
# 是子类的异常要放在父类异常的前面，异常报错越具体，越好解决问题
# 在异常处理的时候，一旦拦截到某一个异常，则不再继续往下查看，直接进行下一段代码，有finally执行finally，没有则继续往下执行
except ZeroDivisionError as e :
    print("输入的数据不合法，请重新输入")
    # 打印出异常报错的信息：division by zero
    print(e)
    # exit()是程序退出的意思
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("属性有问题")
    print(e)
    exit()
# Python所有的错误都是从BaseException类派生的，
except BaseException as e:
    print("我也不知道是什么异常了，直接打印异常，然后退出吧")
    print(e)
    exit()
finally:
    pass

