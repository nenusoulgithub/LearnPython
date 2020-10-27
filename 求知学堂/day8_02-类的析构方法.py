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


cat = Animal("mimi")

print(cat)

del cat

input("输入任意字符结束程序....")

exit()