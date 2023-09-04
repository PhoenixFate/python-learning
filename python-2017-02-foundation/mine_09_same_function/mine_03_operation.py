list1 = [1, 2, 3]
list2 = [3, 4]
print(list1 + list2)
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)
print(list1 * 2)
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)
print(tuple1 * 2)

str1 = "hello "
str2 = "python"
print(str1 + str2)

print("h" in str1)
print("h" not in str1)
print(1 in list1)
print(1 not in list1)

# 对于字典，只能判断key是否在字典中，而不能判断value是否在字典中
temp1 = {"name": "tom"}
print("name" in temp1)
print("tom" in temp1)
