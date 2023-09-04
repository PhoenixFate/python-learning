def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元祖变量/字典变量
gl_nums = (1, 1, 2)
gl_dict = {"name": "tom", "age": 18}

# 拆包，在元祖变量前添加*
# 在字典变量前添加**
# 简化元祖，字典变量的传递
demo(*gl_nums, **gl_dict)

