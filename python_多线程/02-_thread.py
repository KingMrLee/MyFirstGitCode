'''
配合01_threading.py做线程测试使用
'''

import time

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

def main():
    print("Starting at:", time.ctime())
    loop1()
    loop2()
    print("ALL done at:", time.ctime())

if __name__ == '__main__':
    main()