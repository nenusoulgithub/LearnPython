# all() 判断序列中是否有 None 0 False 如果有就是False
li = []
print(all(li))
li = [1, 2, 3]
print(all(li))
li = [1, 2, 3, 0]
print(all(li))
li = [1, 2, 3, False]
print(all(li))
li = [1, 2, 3, None]
print(all(li))
print("-----------------------------------------------")
# any() 列表中有一项不为 None 0 False 则返回True
li = []
print(any(li))
li = [1, 0, None, False]
print(any(li))
li = [0, None, False]
print(any(li))
print("-----------------------------------------------")
# sorted() 对列表(元组)进行排序，然后返回新的列表
li = ["b", "c", "d", "a"]
print(sorted(li))
li = ["b", "c", "d", "a"]
li.sort() # 直接在原来的列表基础上进行排序
print(li)
t = (4, 3, 1, 2)
print(sorted(t))
print(sorted(t, reverse=True))  # 降序排序
print("-----------------------------------------------")
# zip() 打包可迭代对象
li1 = [1, 2, 3]
print(list(zip(li1)))
li2 = ["a", "b", "c"]
print(list(zip(li1, li2)))
print("-----------------------------------------------")
# enumerate() 遍历列表
li = ["a", "b", "c"]
for index, item in enumerate(li):
    print(index, item)

d = dict(name="小明", age = 19)
for index,item in enumerate(d):
    print(index, item, d[item])
