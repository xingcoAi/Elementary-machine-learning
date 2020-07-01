"""
事件(event):
线程间的通信
"""

import threading, time

class Boss(threading.Thread):
    def run(self):
        print("Boss:我们要996啦.")
        #事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("Boss:大家干完啦,不用996啦.")
        print(event.isSet())
        event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker:怎么还996了呢.")
        event.clear()
        event.wait()
        print("Oh yeah!!!")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())

    for t in threads:
        t.start()