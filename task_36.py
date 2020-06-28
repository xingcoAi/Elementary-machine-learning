#yield_generator
def demo1():
    l = [x for x in range(1000)]
    return l

a = demo1()
# print(a)

#另一种写法
def yield_demo1():
    for i in range(3):
        yield i

a = yield_demo1()#generator object
# print(a)
# for i in a:
#     print(i)

#多生成器
