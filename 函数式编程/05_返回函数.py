'''
返回函数
'''

# 定义一个普通函数

def myF1():
    print("In myF1")
    return None

myF1()
# 函数作为返回值返回，被返回的函数在函数体内定义
# 调用myF2，返回一个函数myF3，赋值给f
def myF2():

    def myF3():
        print("In myF3")
        return 3
    return myF3

f = myF2()
print(type(f))  # 是一个class function类型 ，<function myF2.<locals>.myF3 at 0x000002A0343BD1E0>
print(f)
print(f())

# 复杂一点的返回函数的案例
# args:参数列表

def myF4( *args):

    def myF5():
        rst = 0
        for i in args:
            rst += i
        return rst
    return myF5

f2 = myF4(1,2,3,4,5,6,7,8,9,0)
print(f2())


