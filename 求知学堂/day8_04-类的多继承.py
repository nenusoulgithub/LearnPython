# 类的多继承
class A:
    def __init__(self, name="A"):
        self.name = name

    def eat(self):
        print("%s喜欢吃苹果" % self.name)


class B:
    def __init__(self, name="B"):
        self.name = name

    def eat(self):
        print("%s喜欢吃梨" % self.name)


class C(A, B):
    def sound(self):
        print("%s 在唱歌" % self.name)

    def __str__(self):
        return "My name is %s" % self.name


c = C()
print(C.__mro__)
print(c)
c.sound()
c.eat()