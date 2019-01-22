'''
守护线程
'''

import time
import threading

'''
普通线程案例1

def fun():
    print("Staring fun")
    time.sleep(2)
    print("Ending the fun")

print("Main Starting")

# 主线程启动之后，睡一秒，就打印结束，此时子线程fun还在睡，查看结果
t1 = threading.Thread(target=fun, args=())
t1.start()
time.sleep(1)

print("Main End")

'''

'''
守护线程案例
'''
def fun():
    print("Staring fun")
    time.sleep(2)
    print("Ending the fun")

print("Main Starting")

# 主线程启动之后，睡一秒，就打印结束，此时子线程fun还在睡，查看结果
t1 = threading.Thread(target=fun, args=())
# 在start之前设置为守护线程，可以看到当主线程结束的时候，子线程就不会执行了，后面的print没有执行
t1.setDaemon(True)
t1.start()
time.sleep(1)
