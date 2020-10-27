# 定义类
class Persion():
    def __init__(self, name, food):
        print("--------------init-------------")
        self.name = name
        self.food = food

    def __str__(self):
        """
        打印对象内容
        @return:
        """
        return "我是%s，我喜欢吃%s" % (self.name, self.food)

    def __new__(cls, *args, **kwargs):
        """
        每调用一次都会创建一个新对象
        @param args:
        @param kwargs:
        """
        print("--------------new-------------")
        print(cls)
        return object.__new__(cls)


xiaoming = Persion("小明", "榴莲")

print(xiaoming)
