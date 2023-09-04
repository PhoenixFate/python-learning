nameList = ["tom", "cat", "abc", "tom"]

# len() 统计列表中元素的总数
print(len(nameList))

# count 统计列表中某一个数据出现的次数
print(nameList.count("tom"))

# remove 删除第一次出现的数据, 如果数据不存在报错
nameList.remove("tom2")
print(nameList.count("tom"))
