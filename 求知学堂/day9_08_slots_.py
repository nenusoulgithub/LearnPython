# 利用_slots_来控制类可以添加的动态属性
# 可以节约内存资源
# _slots_不可被继承，不影响子类的可添加的动态属性
class Student:
    __slots__ = ("name", "age", "school")

    def __str__(self):
        return "%s的年龄是%d，就读于%s。" % (self.name, self.age, self.school)


xm = Student()
xm.name = "小明"
xm.age = 13
xm.school = "一中"
print(xm)


class BigStudent(Student):
    pass


bs = BigStudent()
bs.sex = "男"
print(bs.sex)
