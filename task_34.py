#lambda表达式，又叫匿名函数
#格式： lambda 参数列表：表达式

f = lambda x: x + x
# print(f(2))

#map函数(函数， 可迭代对象)
map_demo = map(lambda x: x + x, [1, 2, 3, 4])
# print(list(map_demo))

# print(list(map(str, [1, 2, 3, 4])))

#reduce函数
from functools import reduce
r = reduce(lambda x, y: x+y, [1, 2, 3, 4])
# print(r)

#filter函数
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8])))