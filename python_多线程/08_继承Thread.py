'''
继承threading.Thread创建多线程
'''
import threading
import time

# 继承threading.Thread
class MyThread(threading.Thread):

    def __init__(self,arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 重写run函数
    def run(self):
        time.sleep(2)
        print("the args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("MainThread is done!!!!!")
        