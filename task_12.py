# 默认参数
def my_func_2(name = "zhou", age = 30):
    print(name)
    print(age)

#my_func_2()  #默认参数的优先级比传入的参数低
my_func_2("li", 40)

def my_func_3(name, age = 50):
    print(name)
    print(age)

#my_func_3() #这种调用出错，缺少必须参数name
my_func_3(2, 3)

#递归 ：自己调用自己（在函数内部调用）,必须明确递归结束条件
# def my_func_4(x):
#     print(x)
#     my_func_4(x+1)

# my_func_4(1)

#函数返回值

def f(x):
    return "你输入的参数是"+str(x)

r = f(1)
print(r)

def f(x):
    # 明确递归结束条件
    if x == 1:
        return 1

    print("计算"+str(x)+"+"+"f("+str(x-1)+")")
    return x + f(x-1)

r= f(5)
print(r)