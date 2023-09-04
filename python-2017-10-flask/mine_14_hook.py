# coding:utf-8
# python3可以不写
from flask import Flask, request, abort, Response, make_response, jsonify, session, g,url_for
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

# flask的session需要设置密钥字符串
# flask默认把session设置到cookie，由于cookie不安全，所以flask把session的内容根据secret_key混淆处理
app.config["SECRET_KEY"] = "abc"


# 3.直接修改app.config里面的参数
# app.config["DEBUG"] = True


# @app.route 视图函数的装饰器
@app.route("/")
def index():
    """定义的视图函数"""
    return "hello flask"


@app.route("/home")
def home():
    print("home page")
    return "home page"


# 第一次请求之前的钩子函数
@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前"""
    print("handle_before_first_request has been executed")


# 每次请求之前执行
@app.before_request
def handle_before_request():
    """在每次请求之前都会被执行"""
    print("handle_before_request has been executed")
    path = request.path
    print(path)
    if path in url_for("home"):
        print("可以通过path匹配来做特殊的处理")


@app.after_request
def handle_after_request(response):
    """每次请求之后都会执行（视图函数没有出现异常）"""
    print("handle_after_request has been executed ")
    return response


# 每次请求之后执行（调试模式下不会被执行）
@app.teardown_request
def handle_teardown_request(response):
    """每次请求之后都会执行（不管视图函数有没有异常）"""
    print("handle_teardown_request has been executed")
    return response


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口WEIX730d
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="127.0.0.1", port=5010)
