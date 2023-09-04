def measure():
    """测量温度和湿度"""
    print("测量开始")
    temperature = 30
    humidity = 50
    print("测量结束")

    # 元祖可以包含多个数据，可以使用元祖返回多个变量
    # 如果函数返回的是元祖，小括号可以省略
    # return (temperature, humidity)
    return temperature, humidity


result = measure()
print("测量到的温度：%d; 湿度：%d" % (result[0], result[1]))

# 如果函数返回的类型是元祖，同时希望单独处理元祖中的元素
# 可以使用多个变量，一次接受函数的返回结果
# 注意 使用多个变量接受结果时，变量的个数应该和元祖中的元素的个数保持一致
gl_temperature, gl_humidity = measure()
print("温度:%d" % gl_temperature)
print("湿度:%d" % gl_humidity)
