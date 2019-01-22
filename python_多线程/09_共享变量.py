'''
共享变量
'''
import threading
import time

sum = 0
loopsum1 = 10000
loopsum2 = 200000

def myAdd():
    global sum, loopsum1
    # print(sum)
    # print(loopsum)
    for i in range(1,loopsum1):
        # print(i)
        sum += 1

def myMinu():
    global sum, loopsum2
    for i in range(1,loopsum2):
        sum -= 1


if __name__ == '__main__':
    print("Start......{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done......{0}".format(sum))


