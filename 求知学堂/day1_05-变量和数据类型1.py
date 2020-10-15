# 定义变量
# a就是变量的名字 对应一个盒子 里面的数据就是10
# 变量是可以多次赋值的【在程序执行过程中 值可以改变的量】
a = 10
print(a)

a = "郭老师"
print(a)

# 数据类型的划分
# 数字（num）[int,float,complex,bool]
a = 10
print(type(a))
a = 3.1415926
print(type(a))
# 字符串（str）
a = "郭老师"
print(type(a))
# 字典（dict）
a = {}
print(type(a))
# 列表（list）
a = []
print(type(a))
# 元组（tuple）
a = ()
print(type(a))

# 变量命名规则
# 1. 必须以字母和下划线开头
# 2. 变量区分大小写
name = "guohua"
_age = 18
print(name, _age)
