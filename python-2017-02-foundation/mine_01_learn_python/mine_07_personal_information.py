"""
个人信息
"""
# 在python中，定义变量不需要指定变量的类型
# str 表示字符串类型
import sys

name = "小明"
# int 整型
age = 18
# bool 布尔类型 True；False
sex = True
height = 1.75
# float 浮点型
weight = 75.0

print(type(name))
print("sys.getsizeof(name) = ", sys.getsizeof(name))
print(type(age))
print("sys.getsizeof(age) = ", sys.getsizeof(age))
print(type(sex))
print("sys.getsizeof(bool) = ", sys.getsizeof(sex))
print(type(height))
print("sys.getsizeof(float) = ", sys.getsizeof(height))
print(type(weight))

# 在python 中有 int和long 类型，在python3中只有int
intValue = 2 ** 32
print(intValue)
print(type(intValue))
print("sys.getsizeof(int) = ", sys.getsizeof(intValue))
longValue = 2 ** 64
print(longValue)
print(type(longValue))
print("sys.getsizeof(long) = ", sys.getsizeof(longValue))
longValue=2**102
print(longValue)
print(type(longValue))
print("sys.getsizeof(long) = ", sys.getsizeof(longValue))
