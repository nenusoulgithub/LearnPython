# 迭代器
from collections import Iterable

l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
d = {1: 2, 3: 4}
s = {1, 2, 3, 4}

print(isinstance(l, Iterable))
print(isinstance(t, Iterable))
print(isinstance(d, Iterable))
print(isinstance(s, Iterable))

# 可迭代协议方法
print(set(dir([1, 2].__iter__())) - set(dir([1, 2])))  # 迭代器比列表多的方法
print(dir((1, 2).__iter__()))
print(dir({1: 2}.__iter__()))
print(dir({1, 2}.__iter__()))
# 列表迭代器
print([1, 2].__iter__())
# 想让一个集合可以通过for循环，需要实现一个__iter__()方法

# 列表迭代器
iter_l = l.__iter__()
# 迭代器中元素的长度
print("迭代器长度：%d" % iter_l.__length_hint__())
# 根据指定的索引位置指定从哪里开始迭代
print(iter_l.__setstate__(2))
# 一个一个取值
print(iter_l.__next__())
print(iter_l.__next__())
# 超过索引报错
# print(iter_l.__next__())

iter_l = l.__iter__()

while True:
    try:
        item = iter_l.__next__()
        print(item)
    except StopIteration as ex:
        break

# 迭代器遵循迭代协议：必须具备__iter__和__next__两个方法
# 迭代器必然可迭代，可迭代的不一定是迭代器，比如range()就不是迭代器。
print("__next__" in range(5))
print("__iter__" in range(5))


# 生成器
#
# 1. 生尘器函数
# 2. 生成器表达式

# 通过yield编写生成器函数
def product():
    """
    生产衣服：生产2000件衣服
    @return:
    """
    for i in range(2000):
        yield "生产了第{}件衣服".format(i)


# 返回一个迭代器对象
producer = product()
print(producer.__next__())
print(producer.__next__())
print(producer.__next__())

num = 0
for i in range(5):
    print(producer.__next__())

# 列表推导式
print(["鸡蛋%s" % i for i in range(10)])
# 鸡蛋篮子迭代器
egg_bucket = ["鸡蛋%s" % i for i in range(10)]
egg_iter = egg_bucket.__iter__()
while True:
    try:
        print(egg_iter.__next__())
    except StopIteration:
        break


# 面试其1
def demo():
    for i in range(4):
        yield i


g = demo()

g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g1))
print(list(g2))
