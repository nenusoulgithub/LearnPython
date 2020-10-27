# 类属性和实例属性
import datetime
import time


class Student:
    school = "东北师范大学"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    def __str__(self):
        return "学生%s就读于%s" % (self.name, Student.school)

    @classmethod
    def getSchool(cls):
        return cls.school

    @classmethod
    def setSchool(cls, school):
        cls.school = school

    @staticmethod
    def getCurrentTime():
        return time.time()


# 使用类的实例调用类方法和类属性
xiaoming = Student("小明")
print(xiaoming)
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))
xiaoming.school = "吉林大学"
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))
print(xiaoming)

print("类属性的地址是%d，内容是%s。" % (id(Student.school), Student.getSchool()))

# 通过类的实例调用类方法
xiaoming.setSchool("长春中医学院")
print("类属性的地址是%d，内容是%s。" % (id(Student.school), Student.getSchool()))
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))

# 通过类调用类方法
Student.setSchool("长春大学")
print("类属性的地址是%d，内容是%s。" % (id(Student.school), Student.getSchool()))
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))

# 调用类的静态方法
print(Student.getCurrentTime())
print(xiaoming.getCurrentTime())
