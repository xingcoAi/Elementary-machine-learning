"""
名词：类，对象，实例，实例化
对象和实例：类代表了具有相同特征的一类事物（人）
对象和实例：具体的某一个事物（张三，李四）
实例化：将类变成对象的一个过程，new一个对象
"""

class Person:

    #类变量
    name = "女娲"
    age = 10000

    #类私有变量
    __private_args = "class private"

    #无参数的构造函数
    # def __init__(self):
    #     print("构造函数运行")

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print(self.name)
        print(self.age)
        print(self.sex)

    def get_private_args(self):#访问私有变量
        return self.__private_args

    def __my_private_method(self):
        print("私有方法")

    def _my_protect_method( self):
        print("保护方法")


    @classmethod
    def my_class_method( cls ):
        print(cls.name)
        print("类方法")

    @staticmethod
    def  my_static_method():
        print("静态方法")
    



p = Person("fx", 1200, "男")

#静态方法调用,不需要实例化
# Person.my_static_method()

#类方法调用
# Person.my_class_method()
# p._my_protect_method()

#私有方法的访问(外部实例如何访问)：以实例._类名的方式来改变权限
print(p._Person__private_args)
p._Person__my_private_method()