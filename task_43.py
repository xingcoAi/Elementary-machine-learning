#多线程锁
from threading import Thread,currentThread,RLock,Lock
import time

#互斥锁
mutexA = Lock()
mutexB = Lock()

#递归锁
# mutexA = RLock()
# mutexB = RLock()

class House(Thread):
    def run(self):
        self.room1()
        self.room2()

    def room1(self):
        mutexA.acquire()#获取锁
        print(currentThread().name + "房间1拿到A锁")
        mutexB.acquire()
        print(currentThread().name + "房间1拿到B锁")
        mutexB.release()
        print(currentThread().name + "房间1释放了B锁")
        mutexA.release()
        print(currentThread().name + "房间1释放了A锁")

    def room2(self):
        mutexB.acquire()
        print(currentThread().name + "房间2拿到B锁")
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + "房间2拿到A锁")
        mutexA.release()
        print(currentThread().name + "房间2释放了A锁")
        mutexB.release()
        print(currentThread().name + "房间2释放了B锁")

# if __name__ == "__main__":
#     for i in range(10):
#         t = House()
#         t.start()

#多线程作业
import  threading
import time

condition = threading.Condition()
products = 20

class Producer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products <= 10:
                    products += 1
                    print("{}:{}库存不足商品数量小于等于10,现在的产品数量是{}".format("生产者", threading.currentThread().getName(), products))
                    condition.notify()#这个函数唤醒一个等待的线程notifyall唤醒所有

                else:
                    print("{}:{}库存充足上商品数量大于10,现在的产品数量是{}".format("生产者", threading.currentThread().getName(), products))
                    condition.wait()#线程等待
                condition.release()
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("{}:{}->我消费了一件商品,现在商品的数量是{}".format("消费者", threading.currentThread().getName(), products))
                else:
                    print("{}:{}->没有库存了,现在商品的数量是{}".format("消费者", threading.currentThread().getName(), products))
                    condition.wait()
                condition.release()
                time.sleep(2)

if __name__ == "__main__":
    for i in range(3):
        p = Producer()
        p.start()

    for i in range(10):
        c = Consumer()
        c.start()