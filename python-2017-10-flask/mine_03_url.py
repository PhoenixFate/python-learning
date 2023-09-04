# coding:utf-8
# python3可以不写
from flask import Flask, current_app, redirect, url_for

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


#  使用methods限制post请求
@app.route("/login", methods=["POST"])
def login():
    return "login success"


# 多个相同的请求，返回先匹配到的那个
@app.route("/hello")
def hello1():
    return "hello1"


@app.route("/hello")
def hello2():
    return "hello2"


# 同一个视图函数对应多个视图路由
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi"


# 重定向
@app.route("/register")
def register():
    # 通过 url_for 反推函数对应的路由
    url = url_for("register_success")
    return redirect(url)


@app.route("/registerSuccess")
def register_success():
    return "register success"


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="0.0.0.0", port=5005)
