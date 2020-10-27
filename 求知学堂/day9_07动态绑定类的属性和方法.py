import types


# 动态绑定类的属性和方法
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("%s正在叫..." % self.name)


def print_info(self):
    print("小狗%s的年龄是%d岁。" % (self.name, self.age))


# 动态绑定类的实例属性
dog = Animal("旺财")
dog.age = 1
print("小狗%s的年龄是%d岁。" % (dog.name, dog.age))

# 动态绑定类的实例方法
dog.printInfo = types.MethodType(print_info, dog)
dog.printInfo()

# 动态绑定类的属性
Animal.weight = 15
print("小狗%s的年龄是%d岁，体重是%d公斤。" % (dog.name, dog.age, Animal.weight))


# 动态绑定类的方法
@classmethod
def class_method(cls):
    print("这是一个类方法")


Animal.class_method = class_method
Animal.class_method()
dog.class_method()

# 动态绑定类的静态方法
@staticmethod
def static_method():
    print("这是一个静态方法")


Animal.fun1 = static_method
Animal.fun1()
dog.fun1()