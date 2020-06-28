"""
函数的参数：
- 必须参数、默认参数、组合参数
- 函数参数
- 对象参数
- **kwargs关键字参数
- *args 可变参数
"""

def function(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

# function(1, 2, 3, 4, 5, 6, name = "args", key = "123")

"""
命名关键字参数，*号后边的必须写名字
命名关键字参数是必须参数，如果不需要他是必须参数，可以给一个默认值
"""
def func2(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

# func2(1, 2, c = 3, d = 4)
# func2(1, 2, d = 4, c = 3)

def func3(a, b, c):
    print(a)
    print(b)
    print(c)

s = (1, 2, 3)
# func3(*s)#元组拆分
s1 = [4, 5, 6]
# func3(*s1)#字典拆分

kw = {"a":1, "b":2, "c":3}#键必须和函数参数的名字一致，否则报错
func3(*kw)#传键
func3(**kw)#传值

