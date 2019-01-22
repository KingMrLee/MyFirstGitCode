'''
线程属性
'''
import time
import threading

def loop1():
    # ctime()得到当前时间
    print("Start loop1 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(6)
    print("End loop1 at:", time.ctime())

def loop2():
    # ctime()得到当前时间
    print("Start loop2 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(1)
    print("End loop2 at:", time.ctime())

def loop3():
    # ctime()得到当前时间
    print("Start loop3 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print("End loop3 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())

    t1 = threading.Thread(target=loop1, args=())
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t1.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t1.setName("THR_3")
    t3.start()

    time.sleep(3)
    for thr in threading.enumerate():
        print("当前正在运行的线程有{0}：".format(thr.getName()))

    print("当前正在运行的线程数为{0}".format(threading.active_count()))

    print("ALL done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)