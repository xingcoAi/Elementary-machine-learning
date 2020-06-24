#继承减少代码冗余

class Father:
    name = "李雷"
    sex = "男"
    def __init__(self):
        print("Father构造函数运行")

    def speak_english(self):
        print("father讲英语")
    
    def __juehuo(self):
        print("老爸的绝活")


class Mother:
    name = "韩梅梅"
    sex = "女"

    def __init__(self):
        print("Mother 构造函数运行")

    def speak_chinese(self):
        print("mother讲中文")


class Child(Father, Mother):#多继承，继承顺序从左到右，可以无限多
    # name = "哈哈"
    def __init__(self):
        print("Child构造函数运行")#如果子类没有构造函数将运行父类的构造函数
   
    def speak_english(self):
        print("child speak english")#如果有同名函数将覆盖父类的同名函数
    
    def study(self):
        print("child study")



# c = Child()
# c.speak_english()
# c.speak_chinese()
# print(c.name)#继承父类变量name


"""
必须继承
"""
from abc import abstractclassmethod, ABCMeta

class Tester(metaclass = ABCMeta):
     
    @abstractclassmethod
    def test(self):
        pass

class FunctionTester(Tester):
    def test(self):
        print("功能测试")


f = FunctionTester()
# f.test()


"""
继承顺序:先深度优先查找，直至找到公共父类再按广度查找
"""

class A(object):
    def test(self):
        print("A类")

class B(A):
    pass

class C(A):
    def test(self):
        print("C类")

class D(B):
    pass

class E(C):
    def test(self):
        print("E类")

class F(D, E):
    pass

f = F()
f.test()

print(F.__mro__)#查看继承顺序：F->D->B->E->C->A
"""
<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>
"""