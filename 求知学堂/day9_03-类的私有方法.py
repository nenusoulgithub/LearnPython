# 类的私有方法
# 类的私有方法只能在类的内部被访问
# 类的私有化方法不能被继承
# 单下划线（_）+方法名标识protect方法


class Animal:
    def __init__(self, name):
        self.name = name

    def __eat(self):
        print("%s正在吃" % self.name)

    def run(self):
        self.__eat()
        print("%s正在跑" % self.name)


dog = Animal("旺财")
# 私有方法无法直接访问，只能被类内部其他方法访问。
# dog.__eat()
dog.run()
