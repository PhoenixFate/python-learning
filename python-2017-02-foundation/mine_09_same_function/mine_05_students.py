students = [
    {
        "name": "阿土",

    },
    {
        "name": "阿美"
    }
]

find_name = "阿美"
for std_dict in students:
    print(std_dict)
    if std_dict["name"] == find_name:
        print("成功找到"+find_name+"这个人")
        break
else:
    print("未找到指定到姓名")