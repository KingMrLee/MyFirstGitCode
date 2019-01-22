'''
多线程
'''

import time
import _thread


def loop1():
    # ctime()得到当前时间
    print("Start loop1 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2():
    # ctime()得到当前时间
    print("Start loop2 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop2 at:", time.ctime())

# 下面的代码一共有三个线程，主线程，线程1、线程2
def main():
    print("Starting at:", time.ctime())
    # 启动多线程的意思是用多个线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数有两个：一个是需要运行的函数名称，第二个是函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    _thread.start_new_thread(loop1, ())

    _thread.start_new_thread(loop2, ())

    print("ALL done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)