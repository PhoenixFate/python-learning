#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import cards_tools

# 由用户决定循环什么时候退出
while True:
    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是：「%s」" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部名片
        elif action_str == "2":
            cards_tools.show_all()
        # 搜索名片
        elif action_str == "3":
            cards_tools.search_card()
    # 0 退出系统
    elif action_str == "0":
        # 如果在开发程序时，不希望立即编写分支内部的代码
        # 可以使用pass关键字，表示一个关键字，能够保证程序的代码结构正确
        break
        # pass
    # 其他内容，输入错误，需要提示用户
    else:
        print("您的输入不正确，请重新输入")
print("程序结束")
