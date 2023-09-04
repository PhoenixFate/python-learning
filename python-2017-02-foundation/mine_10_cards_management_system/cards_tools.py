# 名片列表变量
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用「名片管理系统」V 1.0")
    print()
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print()
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入email：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print("添加%s到名片成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        input("按下任意键继续\n")
        return

    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t\t")
    print()
    # 打印分隔线
    print("=" * 50)
    # 遍历名片列表，依次输出字典信息
    for card in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))
    print()
    input("按下任意键继续\n")


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索到名字
    search_name = input("请输入要搜索到姓名: ")

    # 2.遍历名片列表，查询要搜索到姓名，如果没有找到，提示用户
    for card in card_list:
        if card["name"] == search_name:
            print("找到了")
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))
            # 针对找到的名片进行修改和删除操作
            deal_card(card)
            # input("按下任意键继续\n")
            break
    else:
        print("抱歉，没有找到%s对应的名片" % search_name)
        input("按下任意键继续\n")


def deal_card(find_dict):
    """
    处理查找到到名片
    @param find_dict:查找到名片
    @return:
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作\n"
                       "[1] 修改\t [2] 删除\t [0] 返回上级菜单\n")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：【回车不修改】")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：【回车不修改】")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入qq: 【回车不修改】")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入email: 【回车不修改】")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")
    else:
        return


def input_card_info(dict_value, tip_message):
    """
    输入名片信息，有输入则用输入的值，没有输入则返回原来的值
    @param dict_value:字典中原有的值
    @param tip_message:输入的提示文字
    @return:如果用户输入了内容，就返回内容，否则返回字典中原油的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回字典原有的值
    else:
        return dict_value
