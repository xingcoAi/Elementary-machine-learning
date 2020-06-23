# # """
# # 正则表达式是用来操作字符串的一种逻辑公式
# # """

import  re
# s = "贪心学院的官网是http://www.greedyai123.com"
# # reg = "http://[w]{3}\.[a-z0-9]*\.com"

# # result = re.findall(reg, s)
# # print(result)

# s = "Hello World"
# reg = "Hello"
# print(re.findall(reg, s))

# #元字符
# """
# . 代表除换行符意外的所有字符
# \w 匹配字母或数字或下划线
# \s 匹配任意的空白符
# \d 匹配任意的数字 0-9
# ^匹配字符串的开头
# $ 匹配字符串的结束
# """

# s = "adklfjk好的kjd34$$%%__3    33cjklv"
# print(re.findall("\w", s))
# print(re.findall("\d", s))
# print(re.findall("\s", s))
# print(re.findall("^a", s))
# print(re.findall("^\d", s))


# #反义代码
# """
# \W 不是\w匹配的东西
# \S
# \D
# """

# # 限定符
# """
# * 代表的是它前面的正则表达式重复0次和多次
# + 重复1次或多次
# ？ 重复0次或一次
# {n} 重复n次
# {n，}最小重复n次
# {n， m}重复n次到m次
# """

# s = "ksjdf34212uh看见防护455……&……&%……"
# print(re.findall("\d{3}", s))
# print(re.findall("[a-z0-9]?", s))

# s1 = "我的QQ号是1522988187"
# reg = "\d+"
# print(re.findall(reg, s1))

# #分组匹配
# s = "我的QQ号码是：1522988187，我的邮编是663100"
# reg = "(\d{10}).*(\d{6})"
# print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))


"""
正则表达式的高级应用：贪婪与非贪婪
非贪婪操作符 
*? 匹配0次
+？匹配1次
？？匹配0次
"""

# 分支条件匹配
# 操作符\

s = "电话号码：010-12354687 0431-25641325 0432-1562365"
reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}"
# print(re.findall(reg,s))

#零宽断言
"""
(?=reg)  匹配reg前边的位置
(?<=reg)  匹配reg后边的位置
(?!=reg)  匹配后边跟的不是reg的位置
(?<!reg)  匹配前边跟的不是reg的位置
"""
s = "hellogreedyailove"
reg = "l{2}o(?=greedyai)"
# print(re.findall(reg,s))
reg = "(?<=greedyai)[a-z]*"
print(re.findall(reg,s))

