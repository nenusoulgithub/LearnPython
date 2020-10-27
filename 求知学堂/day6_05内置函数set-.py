# set集合
# set内部的元素不重复，且无序
# 类似于字典 但是只有key 没有value
# 创建集合
set1 = {1, 2, 3, 1, 2}
print(type(set1))
print(set1)
print("----------------------------------")
# 添加操作
set1.add(4)
print(set1)
print("----------------------------------")
# 清空操作
set1.clear()
print(set1)
print("----------------------------------")
# 取差集
a = {32, 12, 34}
b = {12, 43, 11}
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)
print("----------------------------------")
# 交集
print(a.intersection(b))
print(a & b)
print("----------------------------------")
# 并集
print(a.union(b))
print(a | b)
print("----------------------------------")
# 弹出
set1 = {1, 2, 3, 1, 2}
print(set1.pop())
print(set1)
print("----------------------------------")
# 移除
set1 = {1, 2, 3, 1, 2}
print(set1.discard(3))
print(set1)
print("----------------------------------")
# 更新集合
set2 = {1, 3, 4, 6}
set1.update(set2)
print(set1)
