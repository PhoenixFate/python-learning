# 字典是一个无序的数据集合
people = {"name": "tom",
          "age": 18,
          "gender": "男",
          "height": 1.75,
          "weight": 75}

# 1.统计长度
print(len(people))

# 2.合并字典
# 如果被合并的字典中包含以及存在的键值对，会覆盖原有 对键值对
temp_people = {"name": "carry", "sex": 1}
people.update(temp_people)

print(people)

# 3.清空字典
people.clear()
print(people)

