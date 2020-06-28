"""
什么是异常？
运行时代码抛出的错误
BaseException是所有异常的基类
异常的处理方式：
try:
    代码块
except 异常名字:
    代码块：你要如何去处理这个异常
else:
    代码块
"""

try:
    file = open("aaa", "r")

except FileNotFoundError as e:
    print("发生异常")#只针对FileNotFoundError的异常
    print(e)
else:
    print("没有发生异常")

#异常的分级
try:
    file = open("aaa", "r")

except FileNotFoundError as e:
    print("发生异常")#只针对FileNotFoundError的异常
    print(e)

except ReferenceError as e:
    print("异常2")

except  Exception:#权限大的异常放在后面
    print("发生异常了")
else:
    print("没有发生异常")


"""
异常的处理原则：
能处理的异常才捕获，不能处理的异常直接抛出
"""
try:
    file = open("aaa", "r")

except FileNotFoundError as e:
    print("发生异常")#只针对FileNotFoundError的异常
    print(e)

except ReferenceError as e:
    print("异常2")

except  Exception:#权限大的异常放在后面
    print("发生异常了")
else:
    print("没有发生异常")

finally:
    print("不管有没有捕获异常，这个无论如何都会被执行")

#手动抛出异常
# raise Exception("手动抛出一个异常")

try:
    raise Exception("手动抛出一个异常")
except:
    print("捕获一个异常")

#自定义异常
class MyDefineError(BaseException):
    pass
try:
    raise MyDefineError("抛出一个自定义异常")
except MyDefineError as e:
    print(e)