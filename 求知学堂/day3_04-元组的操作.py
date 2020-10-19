# 列表是一种不可变的序列
# 1. 使用()创建元组
# 2. 元组内容可以是任意类型
# 3. 元组只有一个元素也要加逗号

t = ("我们", "a", 34.56, 222, "还是从前一样", [1, 2, 3, 4, 5])
print(type(t))
print(t)

# 切片操作
print(t[::-1])  # 逆序
print(t[::-2])  # 步进为2的逆序

t[5][1] = 100  # 元组内部列表的元素可以修改
print(t)

# 单个元素的元素必须添加逗号
print(type((1)))
print(type((1,)))

# 常用方法
print(tuple(range(10)).index(3))
print(tuple(range(10)).count(3))
