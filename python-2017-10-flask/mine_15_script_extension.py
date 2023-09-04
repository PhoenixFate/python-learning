# coding:utf-8
# python3可以不写
from flask import Flask, request, abort, Response, make_response, jsonify, session, g, url_for

from flask_script import Manager

# 创建flask的应用对象
app = Flask(__name__)

# 创建Manager管理类对象
# python mine_15_script_extension.py -help
manager = Manager(app)

# flask的session需要设置密钥字符串
# flask默认把session设置到cookie，由于cookie不安全，所以flask把session的内容根据secret_key混淆处理
app.config["SECRET_KEY"] = "abc"


# @app.route 视图函数的装饰器
@app.route("/")
def index():
    """定义的视图函数"""
    return "hello flask"


@app.route("/home")
def home():
    print("home page")
    return "home page"


if __name__ == '__main__':
    # 通过管理对象来启动flask
    # 启动程序：
    # python mine_15_script_extension.py --help
    # runserver模式
    # python mine_15_script_extension.py runserver --help
    # -h HOST -p PORT, -d(enable the Werkzeug debugger )
    # python mine_15_script_extension.py runserver -h 127.0.0.1 -p 7000 -d

    # shell默认（交互默认）相当于在控制台中直接操作变量
    # python mine_15_script_extension.py shell
    # >app.url_map
    manager.run()
