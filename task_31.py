"""
装饰器（语法糖，注解）
"""
def func1(x):
    return x * 2

def func2(x):
    return x * 3

def func3(x, y, i, j):#函数的参数可以是一个函数
    return x(i) + y(j)

r = func3(func1, func2, 2, 3)#带括号时直接调用运行，不带括号表示引用
# print(r)

#简单装饰器的书写,无参数
import time
def runtime_noargs(function_name):
    def wrapper():
        start_time = time.time()
        print("函数运行前")
        function_name()
        print("函数运行后")
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

@runtime_noargs#装饰器不可以同时有多个
def function_demo1():
        time.sleep(1)
        print("demo1函数运行")

# function_demo1()

def args_is_str(function_name):#一个参数
    def wrapper(a):
        t = type(a)
        if  not isinstance(t(), str):
            print("参数错误")

        else:
            function_name(a)

    return wrapper

@args_is_str
def function_demo2(args):
    print(args)

# function_demo2("aaa")

#多个参数，*args表示不定长参数
def many_args(function_name):
    def wrapper(*args):
        print(*args)
        function_name(*args)

    return wrapper


@many_args
def function_demo3(*args):
    print(*args)

# function_demo3(1,2,3)
def dict_args(fuction_name):
    def wrapper(**dict):
        print(dict)

    return wrapper

@dict_args
def function_demo4(**kwargs):#**kwargs代表键值参数
    # print(kwargs)
    pass

# function_demo4(name = "aaa", age = 10, address = "北京")
def combo_args(function_name):
    def wrapper(*args, **kwargs):
        print(args, kwargs)

    return wrapper
    
@combo_args
def function_demo5(*args, **kwargs):
    pass

# function_demo5(1, 2,name = "aaa", age = 10, address = "北京")

def max_runtime(timeout):
    def out_wrapper(function_name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            i = function_name()
            end_time = time.time()
            use_time = end_time - start_time

            if use_time > timeout:
                print("函数运行超时")
            return i
        return wrapper
    return out_wrapper

@max_runtime(timeout = 1)
def function_demo6(*args, **kwargs):
    time.sleep(2)
    print("demo6运行")
    return 1

function_demo6()