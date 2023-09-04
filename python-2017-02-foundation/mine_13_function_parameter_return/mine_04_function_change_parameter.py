def demo(num_list):
    # 使用方法修改列表内部内容
    # 在 Python 中 函数 的 参数传递 以及 返回值 都是靠 引用 传递的
    print("函数内部")
    num_list.append(9)
    print(num_list)
    print("函数执行结束")


gl_list = [1, 2, 3]
print(gl_list)
demo(gl_list)
print(gl_list)
