# abs() 绝对值
print(abs(-123))

# round() 取近似值
print(round(2.6))
print(round(3.1415926, 3))

# pow(x, y) 幂运算
print(pow(2, 3))

# divmod(x, y) 求商和余数
print(divmod(6, 5))

# max() 求最大值
print(max(range(3, 7)))

# min() 求最小值
print(min(1, 2, 3))

# sum() 迭代求和
print(sum(range(0, 10)))
print(sum(range(0, 10), 2))
print(sum([1, 2, 3], 10))

# eval() 动态执行表达式
a, b, c = 1, 2, 3
print(eval("a+b+c"))


def testFunc():
    print("我执行了吗？")


eval("testFunc()")
