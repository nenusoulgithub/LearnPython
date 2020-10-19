# Python的输入与输出 %s 字符串 %d 整数 %f 浮点
# 输出
name = "郭华"
age = 15
school = "泊头市第一中学"
score = 100.0
print("我的名字是%s，今年%d岁，就读于【%s】，今年考试分数是%f。" % (name, age, school, score))

name = input("请输入姓名：")
age = int(input("请输入年龄："))
phone = input("请输入电话：")
address = input("请输入地址：")

print("-------------第一钟输出格式--------------")
print("姓名：{}".format(name))
print("年龄：{}".format(age))
print("电话：{}".format(phone))
print("地址：{}".format(address))
print("-------------第二钟输出格式--------------")
print("姓名：%s" % (name))
print("年龄：%d" % (age))
print("电话：%s" % (phone))
print("地址：%s" % (address))
