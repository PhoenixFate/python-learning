num_str = "0123456789"

# 截取2-5
print(type(num_str))
print(num_str[2:6])
print(type(num_str[2:6]))
# 截取2到末尾
print(num_str[2:])
# 开始到5
print(num_str[0:6])
print(num_str[:6])
# 截取完整到字符串
print(num_str[:])
# 每隔一个字符截取一个字符
print(num_str[::2])

# 从1开始，每隔一个字符截取一个字符
print(num_str[1::2])
# 截取从2 到 -1到字符
print(num_str[2:-1])

# 截取字符串到最后两个字符
print(num_str[-2:])

# 字符串逆序
print(num_str[-1::-1])
