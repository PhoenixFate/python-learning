nameList = ["tom", "cat", "abc"]

# 使用del 关键字删除列表元素
# 建议使用列表提供的方法pop remove删除
del nameList[0]

# del 本质上把变量从内存中删除
name = "aaa"
del name

print(nameList)
