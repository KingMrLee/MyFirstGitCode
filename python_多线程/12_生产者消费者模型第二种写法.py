'''
生产者消费之模型就是,比如一个包子铺,中的顾客吃包子,和厨师做包子,
不可能是将包子一块做出来,在给顾客吃,但是单线程只能这麽做,
所以用多线程来执行,厨师一边做包子,顾客一边吃包子,
当顾客少时,厨师做的包子就放在一个容器中,等着顾客来吃,
当顾客多的时候,就从容器中先取出来给顾客吃,厨师继续做包子
用队列来模拟这个容器
'''
import threading, time, queue
q = queue.Queue()
def Produce(name):
    count = 1   # conut表示做的包子总个数
    while count < 10:
        print('厨师%s在做包子中...'%name)
        time.sleep(2)
        q.put(count)   # 容器中添加包子
        # 当做完一个包子后就要给顾客发送一个信号,表示已经做完,让他们吃包子
        print('produce%s已经做好了第%s个包子'%(name, count))
        count += 1
        print('ok......')
def Consumer(name):
    count = 1    # count表示包子被吃的总个数
    while count < 10:
        time.sleep(2)  # 排队去取包子,
        if not q.empty():   # 如果存在
            data = q.get() # 取包子, 吃包子
            print('\033[32;1mConsumer %s已经把第%s个包子吃了...\033[0m' %(name, data))
        else:
            print('包子被吃完了...')
        count += 1
if __name__ == '__main__':
    p1 = threading.Thread(target=Produce, args=('A君',))
    c1 = threading.Thread(target=Consumer, args=('B君',))
    c2 = threading.Thread(target=Consumer, args=('C君',))
    c3 = threading.Thread(target=Consumer, args=('D君',))
    p1.start()
    c1.start()
    c2.start()
    c3.start()