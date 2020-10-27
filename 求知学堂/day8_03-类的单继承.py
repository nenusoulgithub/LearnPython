# 类的析构方法
class Animal:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        """
        析构方法，类在销毁的时候被调用
        @return:
        """
        print("%s被销毁" % self.name)

    def __str__(self):
        return "我是%s" % self.name


class Cat(Animal):
    def sound(self):
        print("%s在喵喵叫" % self.name)


class Dog(Animal):
    def sound(self):
        print("%s在汪汪叫" % self.name)


cat = Cat("汤姆")
print(cat)
cat.sound()

dog = Dog("旺财")
print(dog)
dog.sound()
