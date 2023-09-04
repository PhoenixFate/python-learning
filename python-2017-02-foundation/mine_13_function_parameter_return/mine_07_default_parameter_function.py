# 缺省参数必须在末尾
def print_info(name, gender=True):
    """
    @param name: 姓名
    @param gender: 性别，true为男生，false为女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明", True)
print_info("小王")
print_info("小美", False)
