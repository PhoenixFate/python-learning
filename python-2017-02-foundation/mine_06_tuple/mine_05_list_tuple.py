# list tuple 之间转换
num_list = [1, 2, 3, 5]
print(type(num_list))
# 数组转元组
info_tuple = tuple(num_list)
print(type(info_tuple))
print(info_tuple)

info = ("carry", 18, 1.75)
# 元组转数组
info_list = list(info)
print(type(info_list))
print(info_list)
