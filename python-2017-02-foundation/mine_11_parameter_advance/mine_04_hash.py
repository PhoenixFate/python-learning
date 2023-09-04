print(hash(1))
print(hash("hello"))
print(hash((1, 2)))
# TypeError: unhashable type: 'list'
# print(hash([2,3]))

# 字典的key只能是不可变类型的数据
