#列表推导式：x for x in a
y = [x + 1 for x in [1, 2, 3, 4]]
# print(y)
# print(list(x + 1 for x in [1, 2, 3, 4] if x > 2))

# 集合推导式
y = {x + 1 for x in [1, 2, 3, 4]}
# print(y)

#字典推导式
d = {x:y for x, y in {"a":1, "b": 2}.items()}
print(d)
# print(d.items()) items()返回由字典键值对组成的元组所构成的列表
#取出字典的键
d_key = {x for x, y in {"a": 1, "b": 2}.items()}
print(d_key)
#取出字典的值
d_value = {y for x, y in {"a": 1, "b": 2}.items()}
print(d_value)