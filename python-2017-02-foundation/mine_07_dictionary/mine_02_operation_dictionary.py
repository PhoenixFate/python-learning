# 字典是一个无序的数据集合
people = {"name": "tom",
          "age": 18,
          "gender": "男",
          "height": 1.75,
          "weight": 75}
# 1.取值
print(people["name"])

# 2.增加 修改
# 如果key不存在，会新增键值对，如果key存在，会修改
people["sex"] = 1
people["name"] = "carry"
print(people["name"])

# 3.删除
people.pop("name")
