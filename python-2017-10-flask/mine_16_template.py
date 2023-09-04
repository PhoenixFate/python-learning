from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "hello flask"


@app.route("/index")
def index():
    data = {
        "name": "abc",
        "age": 18,
        "my_list": [1, 2, 4, 5, 6, 7, 3],
        "my_dict": {"city": "beijing"}
    }
    return render_template("index.html", **data)


# 第一种自定义过滤器的方式
def list_step_2(li):
    """自定义过滤器"""
    return li[::2]


# 注册自定义过滤器
app.add_template_filter(list_step_2, "li2")


# 第二种自定义过滤器的方式
@app.template_filter("li3")
def list_step3(li):
    return li[::3]


if __name__ == "__main__":
    app.run()
