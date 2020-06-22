# """
# 正则表达式是用来操作字符串的一种逻辑公式
# """

import  re
s = "贪心学院的官网是http://www.greedyai123.com"
# reg = "http://[w]{3}\.[a-z0-9]*\.com"

# result = re.findall(reg, s)
# print(result)

s = "Hello World"
reg = "Hello"
print(re.findall(reg, s))

#元字符
"""
. 代表除换行符意外的所有字符
\w 匹配字母或数字或下划线
\s 匹配任意的空白符
\d 匹配任意的数字 0-9
^匹配字符串的开头
$ 匹配字符串的结束
"""

s = "adklfjk好的kjd34$$%%__3    33cjklv"
print(re.findall("\w", s))
print(re.findall("\d", s))
print(re.findall("\s", s))
print(re.findall("^a", s))
print(re.findall("^\d", s))


#反义代码
"""
\W 不是\w匹配的东西
\S
\D
"""

# 限定符
"""
* 代表的是它前面的正则表达式重复0次和多次
+ 重复1次或多次
？ 重复0次或一次
{n} 重复n次
{n，}最小重复n次
{n， m}重复n次到m次
"""

s = "ksjdf34212uh看见防护455……&……&%……"
print(re.findall("\d{3}", s))
print(re.findall("[a-z0-9]?", s))

s1 = "我的QQ号是1522988187"
reg = "\d+"
print(re.findall(reg, s1))

#分组匹配
s = "我的QQ号码是：1522988187，我的邮编是663100"
reg = "(\d{10}).*(\d{6})"
print(re.findall(reg, s))
print(re.search(reg, s).group(1))
print(re.search(reg, s).group(2))