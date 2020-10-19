# 列表是一种可变的序列
li = ["我们", "a", 34.56, 222, "还是从前一样"]

# 列表的操作：增删改查

# 列表的增加操作
print(li)
li.append(True)
print(li)
li.append([False, 555, "!"])
print(li)
li.extend(list(range(10)))
print(li)
li.insert(1, "的爱")
print(li)

# 列表的删除操作
del li[1]
print(li)
del li[10:12]
print(li)
li.remove(7)
print(li)
li.pop()
print(li)
li.pop(4)
print(li)

# 列表的修改
li[1] = "就是"
print(li)
li[1:2] = ["一样", "哈哈"]
print(li)

# 列表的查询
print(li.index(222))
print(li.index(222222))