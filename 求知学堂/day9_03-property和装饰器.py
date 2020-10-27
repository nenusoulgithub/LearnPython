# property和装饰器的使用
class Animal:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # 使用property暴露私有属性
    name = property(getName, setName)

    # 使用装饰器暴露私有属性
    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, param):
    #     self.__name = param


dog = Animal("旺财")
print(dog.getName())
print(dog.name)
dog.name = "小白"
print(dog.name)