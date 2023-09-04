# coding:utf-8
# python3可以不写
from flask import Flask, request, abort, Response, make_response, jsonify
import json

# 创建flask的应用对象
# __name__ 表示当前模块的名字
#  第一次参数：模块名，flask以这个模块所在的目录为根 目录，默认以这个目录中的static为静态目录，templates为模板目录
#  如果给Flask传入一个找到不的名字，则Flask以当前文件所在的模块目录为根目录
# app=Flask("luan xie")
# 第一个参数import_name：导入路径（寻找静态目录与模板目录位置的参数）
# 第二个参数static_url_path，访问静态资源的url前缀
app = Flask(__name__,
            static_url_path="/static",  # 访问静态资源的url前缀，默认static
            static_folder="static",  # 静态文件的目录名
            template_folder="templates",  # 模板文件的目录，默认是templates
            )


# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")


# 2.使用对象配置参数
class Config(object):
    DEBUG = True


app.config.from_object(Config)


# 3.直接修改app.config里面的参数
# app.config["DEBUG"] = True


# @app.route 视图函数的装饰器
@app.route("/")
def index():
    """定义的视图函数"""
    return "hello flask"


# 返回json
# 自己手动定义
@app.route("/json")
def return_json():
    # 在python中 { } 是字典
    # json就是字符串ma
    data = {
        "name": "tom",
        "age": 20
    }
    print(type(data))
    # 在python中 需要使用json.dumps()将字典转换成json 字符串，
    json_str = json.dumps(data)
    print(type(json_str))
    # 使用json.loads()将json字符串转换成字典
    dict_data = json.loads(json_str)
    print(dict_data)
    return json.dumps(data), 200, [("Content-Type", "application/json")]


# 使用jsonify来响应json数据
# jsonify把数据转换成json字符串，把响应头设置成application/json
@app.route("/json2")
def return_json2():
    # 在python中 { } 是字典
    # json就是字符串ma
    data = {
        "name": "tom",
        "age": 20
    }
    # jsonify把数据转换成json字符串，把响应头Content-Type设置成application/json
    return jsonify(data)


@app.route("/json3")
def return_json3():
    # jsonify把数据转换成json字符串，把响应头Content-Type设置成application/json
    return jsonify(city="changhzou", country="china")


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口WEIX730d
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="0.0.0.0", port=5009)
