# 条件运算符 and or not
a, b, c, d = 5, 8, 2, 9
print("---------------and---------------")
print(a < b and c < d)
print(b > c and d < a)
print("---------------or---------------")
print(a < b or c < d)
print(b > c or d < a)
print(b < c or d < a)
print("---------------not---------------")
print(not a < b)

# 逻辑运算符优先级
# () > not > and > or
print(2 > 1 and 1 < 4 or 2 < 4 and 9 > 3 or 1 < 4 and 3 < 2)
