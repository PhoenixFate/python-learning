a = 6
b = 100

# 交换两个变量
# 1.使用其他变量
c = a
a = b
b = c
print("a:%d" % a)
print("b:%d" % b)

# 2.不使用其他变量
a = a + b
b = a - b
a = a - b
print("a:%d" % a)
print("b:%d" % b)

# 3.python解法
a, b = (b, a)
print("a:%d" % a)
print("b:%d" % b)
# 等号右边的元祖的括号可以省略
a, b = b, a
print("a:%d" % a)
print("b:%d" % b)
