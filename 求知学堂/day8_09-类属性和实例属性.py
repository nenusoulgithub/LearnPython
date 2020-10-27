# 类属性和实例属性
class Student:
    school = "东北师范大学"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    def __str__(self):
        return "学生%s就读于%s" % (self.name, Student.school)


xiaoming = Student("小明")
print(xiaoming)
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))
xiaoming.school = "吉林大学"
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))
print(xiaoming)

xiaomao = Student("小毛")
print(xiaomao)
xiaomao.school = "吉林农业大学"
print(xiaomao)
print(xiaomao.school)

Student.school = "吉林大学"
print(xiaoming)
print("类属性的地址是%d，内容是%s。" % (id(xiaoming.school), xiaoming.school))
print(xiaomao)
print("类属性的地址是%d，内容是%s。" % (id(xiaomao.school), xiaomao.school))