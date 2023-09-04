hello = "hello python"

# 1.string.startwith()
print(hello.startswith("hello"))

# 2.string.endwith()
print(hello.endswith("python"))

# 3.string.find()
print(hello.find("python"))
print(hello.find("abc"))  # 指定字符串不存在返回-1
# print(hello.index("abc"))  # index指定字符串不存 报错


# 4.string.replace
# replace不会修改原来都字符串
print(hello.replace("python", "china"))
print(hello)
