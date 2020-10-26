# 1. Python中的new方法作用是什么？
# 用来创建对象的，只有继承了Object类，才有这个方法。

# 2. 什么是单例模式，单例模式适用什么场景。
# 单例模式全局只有一个实例，提供一个全局的访问点。
# 日志类 网站计数 权限验证 数据库连接池

# 3. 私有化方法和私有化属性
# 不能被子类继承

# 4. 在python什么是异常
# 程序重现的错误

# 5. 在Python中如何处理异常的
# try:
# except:
# else:
# finally:

# 7. _slots_的作用
# 限制类动态属性的添加，节省内存空间（Python中所有的属性都放在_dict_中）。

# 8. 私有化属性的作用
# 保护类的属性，防止在类的外部直接访问。可以通过Property和装饰器来访问。

class Person:
    def __init__(self, name, age):
        print("调用__init__方法")
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, param):
        self.__name = param

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, param):
        if param <= 0 or param >= 120:
            return

        self.__age = param


p1 = Person("小明", 16)
print(p1.name)
print(p1.age)


# 实现一个单例
class Logger:
    __instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        print("调用__new__方法")
        if cls.__instance is None:
            print("调用__new__方法，新建一个对象！")
            cls.__instance = super().__new__(cls)

        return cls.__instance


logger1 = Logger()
logger2 = Logger()