def demo(num, num_list):
    print("函数开始")
    num += num
    # 针对列表使用+=，并不是使用+=，而是使用extend方法
    # num_list = num_list + num_list
    num_list += num_list
    print(num)
    print(num_list)
    print("函数执行结束")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
