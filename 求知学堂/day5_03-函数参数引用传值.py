# 在Python中万物皆对象，函数参数传递的是对象的地址的引用。
# 对于简单数据类型，在函数内部更新变量的值会重新开辟内存空间来存储更改后的值
# 对于高级数据类型，在函数内部改变参数的值，则是直接修改原内存地址的数据


def func1(x):
    print("x的内存地址{}".format(id(x)))
    x = 10
    print("更新后x的内存地址{}".format(id(x)))


a = 5
func1(a)
print("a的内存地址{}".format(id(a)))
print("函数内部更新参数值后外部a的值{}".format(a))
print("----------------------------------------------")


def func2(x):
    print("x的内存地址{}".format(id(x)))
    x.append(10)
    print("更新后x的内存地址{}".format(id(x)))


li = []
func2(li)
print("li的内存地址{}".format(id(li)))
print("函数内部更新参数值后外部li的值{}".format(li))