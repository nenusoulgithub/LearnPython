# 类属性私有化
# 不让类的属性在类的外部被访问
# 不让类的属性被修改
# 不让类的属性被继承


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


# 私有化属性不能再类的外部被直接访问
xiaoming = Person("小明", 19)
print(xiaoming.getName())
print(xiaoming.age)
xiaoming.setName("小明明")
print(xiaoming.getName())


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.__school = school

    def __str__(self):
        # 不能继承父类的私有化属性
        # return "%s今年%d岁了，在%s上学。" % (self.__name, self.age, self.__school)
        return "%s今年%d岁了，在%s上学。" % (self.getName(), self.age, self.__school)


xiaohong = Student("小红", 16, "北京第一中学")

print(xiaohong)
