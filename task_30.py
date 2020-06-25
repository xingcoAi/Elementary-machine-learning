"""
闭包：外部函数的返回值是内部函数的应用
"""

def outer(a):
    b = 10
    def inner():
        print(a + b)
    #外部函数的返回值是内部函数的引用
    return inner #有括号时直接调用该函数

# inner_func = outer(3)
# inner_func()