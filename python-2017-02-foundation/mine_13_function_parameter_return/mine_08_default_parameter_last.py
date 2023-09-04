# 缺省参数必须在末尾
def print_info(name, title="", gender=True):
    """

    @param name: 姓名
    @param gender: 性别，true为男生，false为女生
    @param title:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s] %s 是 %s" % (title, name, gender_text))


# 调用有多个缺省参数的函数，如果需要给某一个缺省参数赋值，需要使用参数名=value的方式
print_info("小明", gender=True)
print_info("小王", "班长")
print_info("小美", gender=False)
