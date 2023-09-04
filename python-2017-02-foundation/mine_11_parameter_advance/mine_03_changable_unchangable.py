# 数组
a = [1, 2, 3]
print(id(a))
a.append(999)
print(id(a))
a.clear()
print(id(a))

# 字典
d = {"name": "tom", "age": 18}
print(d)
print(id(d))
d["sex"] = "2"
print(id(d))


