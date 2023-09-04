# coding:utf-8
# python3可以不写
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

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


# 转化器
# 127.0.0.1:5005/goods/123
# 如果访问127.0.0.1:5005/goods/abc 会返回404
@app.route("/goods/<int:goods_id>")
# 也可以不加转换器，默认是string类型
# @app.route("/goods/<goods_id>")
def goods_detail(goods_id):
    print("goods_id: " + str(goods_id))
    return "goods detail page"


# 自定义转换器
# 1.自定义转换器类
class RegexConverter(BaseConverter):
    """
    自定义万能转换器
    """

    def __init__(self, url_map, rule):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = rule


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["regex_converter"] = RegexConverter


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r"1[345678]\d{9}"

    # 高级用法 正则表达式拿到匹配之后的数据，先传给to_python方法
    def to_python(self, value):
        print("可以在这里统一处理")
        value = "mobile:" + value
        return value

    # url_for 会先传给to_url
    def to_url(self, value):
        print("to_url: "+str(value))
        return "18751801511"


app.url_map.converters["mobile_converter"] = MobileConverter


@app.route("/send/<regex_converter('1[345678]\\d{9}'):mobile>")
def send_sms(mobile):
    print(mobile)
    return "send sms to %s" % mobile


@app.route("/send2/<mobile_converter():mobile>")
def send_sms2(mobile):
    print(mobile)
    # redirect("send_sms", mobile="18751801512")

    return "send2 sms to %s" % mobile


@app.route("/send/url_for")
def send_sms3():
    url = url_for("send_sms2", mobile="18751801512")
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)

    # 启动flask程序
    # 默认只绑定到127.0.0.1，
    # 默认5000端口WEIX730d
    # 0.0.0.0 代表绑定当前所有ip
    app.run(host="0.0.0.0", port=5005)
