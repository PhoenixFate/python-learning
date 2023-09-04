# python 内置方法
a = [1, 2, 3]

# 1.len()
print(len(a))

# 2.del() 内存中删除变量
del (a[1])
print(a)

# 3.min()
temp_list = [1, 5, 6, 23]
temp = "abcdefg"
temp_dictionary = {"a": "z", "b": "y", "c": "x"}

print(min(temp))
print(min(temp_list))
# 只会比较字典到keyd
print(min(temp_dictionary))

# 4.max()
print(max(temp))
print(max(temp_list))
# 只会比较字典到key
print(max(temp_dictionary))

# 5.cmp(item1,item2)
# python3取消了cmp函数
str1 = "abc"
str2 = "bcd"
# print(cmp(str1,str2))
# 可以直接使用比较字符
print(str1 > str2)
