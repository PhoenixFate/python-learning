name = ["tom", "cat", "abc"]

# 1.取值
print(name[0])

# 2.取索引
print(name.index("cat"))
# 如果传递的数据不在列表中，程序会报错
# print(name.index("aa"))

# 3.修改
name[1] = "carry"
print(name[1])

# 4.增加数据
name.append("append")
print(name[3])

name.insert(2, "insert")
print(name[2])

# extend 可以把其他列表中的完整内容 追加到当前列表的末尾
temp_list = ['temp1', "temp2"]
name.extend(temp_list)
print(name[5])

# 5.删除数据
name.remove("tom")
for temp in name:
    print(temp, end="\t")
print()
# pop 默认删除列表中最后一个数据
name.pop()
# 弹出 指定index的数据
name.pop(2)
for temp in name:
    print(temp, end="\t")
print()
# 清空
name.clear()
if len(name) == 0:
    print("len name is zero")
else:
    for temp in name:
        print(temp, end="\t")
    print()
