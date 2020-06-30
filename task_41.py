#多线程类

from threading import Thread

# class Hello(Thread):#继承Thread类
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#     def run(self):
#         print("hello %s " % self.name)

# t = Hello("我是一个线程的类")
# t.start()
# print("我是主线程")

"""
进程和线程的区别
"""
from multiprocessing import Process
import os

def work():
    print(os.getpid())

if __name__ == "__main__":
    #在主进程下开启多个线程,每个线程的pid都一样,即在一个进程下工作
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print("住进程------> 线程PID", os.getpid())
    
    #开启多个进程,每个进程有独立的PID'
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print("主进程-----> 线程 PID", os.getpid())