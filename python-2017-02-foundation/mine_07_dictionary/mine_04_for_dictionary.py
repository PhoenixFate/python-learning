# 字典是一个无序的数据集合
people = {"name": "tom",
          "age": 18,
          "gender": "男",
          "height": 1.75,
          "weight": 75}

# 迭代遍历字典
# k是每一次循环中拿到对key
for k in people:
    print("people[%s]: %s" % (k, people[k]))
    print("people[{0}]: {1}".format(k, people[k]))
