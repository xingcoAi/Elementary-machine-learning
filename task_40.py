#多线程
import  threading
import time
import random

def my_print(info):
    time.sleep(random.randint(1, 10))
    print("执行事件" + info)

if __name__ =="__main__":
    t1 = threading.Thread(target=my_print, args =("线程1",))
    #target为要运行的函数,args为要传入运行函数的参数
    #当参数为一个函数时只能进行函数的引用而不能调用函数,即不能在函数名后面家括号
    #用元组形式进行传参时,且元组内只有一个变量时,需要在后面加上逗号,即(变量1, )
    t2 = threading.Thread(target=my_print, args = ("线程2", ))#定义一个线程对象
    t3 = threading.Thread(target=my_print, args = ("线程3", ))
    t4 = threading.Thread(target=my_print, args = ("线程4", ))
    t5 = threading.Thread(target=my_print, args = ("线程5", ))

    t1.start()#启动线程
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    print("主线程")