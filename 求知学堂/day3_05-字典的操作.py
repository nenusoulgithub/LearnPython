# 列表是一种无序的类型
# 1. 使用{}创建元组
# 2. 键不可变，键是唯一的
# 3. 不可用下标和切片

dictA = {"name": "郭华", "age": 19, "school": "东北师范大学"}
print(dictA)

# 元组的操作：增删改查

# 增加一个元素
dictA["address"] = "长春"
print(dictA)

# 删除一个元素
del dictA["age"]
print(dictA)
dictA.pop("name")
print(dictA)

# 更新字典值
dictA["address"] = "吉林省长春市"
dictA["name"] = "郭华"
dictA.update({"name": "guohua"})
print(dictA)

# 字典排序（lamda表达式）
print(sorted(dictA.items(), key=lambda d: d[0]))

