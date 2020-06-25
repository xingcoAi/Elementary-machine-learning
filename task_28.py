"""
多态：一类事物有多种形态
多态性
"""
#都继承了Animal类，但run有不同形式
class Animal:
    def run(self):
        raise AttributeError("子类必须实现这个方法")

class Person(Animal):
    def run(self):
        print("person run")

class Pig(Animal):
    def run(self):
        print("pig run")

class Dog(Animal):
    def run(self):
        print("dog run")


# person = Person()
# person.run()
# pig = Pig()
# pig.run()
# dog = Dog()
# dog.run()


#多态性：

def func(obj):
    obj.run()

person = Person()
func(person)
pig = Pig()
func(pig)



class Computer:
    def usb_insert(self):
        pass

def usb_run(sub_computer):
    sub_computer.usb_insert()


class Mouse(Computer):
    def usb_insert(self):
        print("插入鼠标")

class keyboard(Computer):
    def usb_insert(self):
        print("键盘插入")

m = Mouse()
usb_run(m)
k = keyboard()
usb_run(k)
