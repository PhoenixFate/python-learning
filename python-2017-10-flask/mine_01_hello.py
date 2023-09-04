# coding:utf-8
# python3可以不写
from flask import Flask, current_app
import mine_02_name

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
    MINE_NAME = "phoenix"


app.config.from_object(Config)


# 3.直接修改app.config里面的参数
# app.config["DEBUG"] = True


# @app.route 视图函数的装饰器
@app.route("/")
def index():
    """定义的视图函数"""
    # 读取配置参数
    # 1.直接从全局对象app的config字典中取值
    print(app.config.get("MINE_NAME"))
    # 2.通过current_app导入参数
    print(current_app.config.get("MINE_NAME"))
    return "hello flask"


if __name__ == '__main__':
    print(__name__)
    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="0.0.0.0", port=5005)
