# 容器的公有方法
# 1. 加
# 2. 复制
# 3. in
# 4. zip

# 列表相加
strA = "人生苦短"
strB = "及时行乐"
print(strA + strB)

liA = list(range(5))
liB = list(range(5, 10))
print(liA + liB)

print(list(range(5)) * 2)  # 复制

# in操作
print(2. in (list(range(5))))

dictA = {"name": "郭华"}
print("name" in dictA)
print("age" in dictA)

# zip
print(list(zip(list(range(5)), (list(range(5, 10))))))
