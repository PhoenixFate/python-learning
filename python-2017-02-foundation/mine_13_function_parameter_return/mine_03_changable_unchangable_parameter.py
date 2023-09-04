def demo(num, num_list, tuple_list):
    print("函数内部")
    print("num:%d" % num)
    # 在函数内部 使用赋值语句, 不会修改到外部的实参变量
    num = 100
    print("函数内部 list: %x" % id(num_list))
    num_list = [1, 2, 3]
    tuple_list = (4, 5, 6)
    print("赋值后的num:%d" % num)
    print(num_list)
    print(tuple_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
gl_tuple_list = (1, 2, 3)
demo(gl_num, gl_list, gl_tuple_list)
print("gl_num: %d" % gl_num)
print("函数外部 list: %x" % id(gl_list))
print(gl_list)
print(gl_tuple_list)
