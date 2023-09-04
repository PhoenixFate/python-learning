# coding:utf-8
# python3可以不写
from flask import Flask, request, abort, Response, make_response

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


@app.route("/resp")
def response():
    """返回响应体"""
    # 1.使用元祖，返回自定义的响应信息
    #       响应体    状态码   响应头
    # 可以传入自定义 非http标准的状态码
    # return "response page", 400, [("name", "phoenix"), ("city", "beijing")]
    # return "response page", '666 mine status', [("name", "phoenix"), ("city", "beijing")]
    # return "response page", '666 mine status'

    # 2.使用make_response 来构造响应信息
    resp = make_response("response page")
    resp.status = "999 mine status"
    resp.headers["city"] = "beijing"
    return resp


# 统一错误页面处理
@app.errorhandler(404)
def handle_404_error(error):
    """自定义的错误处理方法"""
    # 这个函数的返回值会是前端用户看到的结果
    return "出现了404错误，错误信息%s" % error


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口WEIX730d
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="0.0.0.0", port=5009)
