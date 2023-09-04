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


@app.route("/set_cookie")
def set_cookie():
    """添加cookie"""
    resp = make_response("success")
    # m默认有效期是临时有效，浏览器关闭生效
    resp.set_cookie("mine_cookie", "phoenix")
    # max_age 单位 秒
    resp.set_cookie("long_cookie", "long_phoenix", max_age=3600)
    return resp


@app.route("/get_cookie")
def get_cookie():
    # request.cookies是一个类似于字典的类型
    cookie1 = request.cookies.get("long_cookie")
    return cookie1


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("delete cookie success")
    # delete_cookie是设置cookie立马过期，真正的删除cookie由浏览器决定
    resp.delete_cookie("long_cookie")
    return resp


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口WEIX730d
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="127.0.0.1", port=5010)
