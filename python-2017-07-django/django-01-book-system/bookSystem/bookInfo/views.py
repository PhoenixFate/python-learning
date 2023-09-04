from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from bookInfo.models import Book


# Create your views here.
# 1.定义视图函数，返回HttpResponse对象
# http://127.0.0.1:8000/index
# 视图函数必须有一个参数，request，然后需要返回一个HttpResponse类对象
# 2.进行url配置，建立地址和处理函数的对应关系
def index(request):
    # 和M、T进行交互
    # 给浏览器返回一个要显示的内容

    # 使用模板文件
    # 1.加载模板文件, 获得模板对象
    template_object = loader.get_template("bookInfo/index1.html")
    # 2.(定义模板上下文 django 2.0+改了，不需要传入上下文对象)：给模板文件传递数据
    # context = RequestContext(request, {"name": "tom"})
    parameters = {"name": "tom"}
    # 3.模板渲染：产生标准的html内容
    result_html = template_object.render(parameters)

    return HttpResponse(result_html)


def index2(request):
    # 和M、T进行交互
    # 给浏览器返回一个要显示的内容
    parameters = {"name": "tom2"}
    return HttpResponse(loader.get_template("bookInfo/index2.html").render(parameters))


# !!!!!!!!!!!!!!!!!!!!!!!!!简写方式：
def index3(request):
    # 和M、T进行交互
    # 给浏览器返回一个要显示的内容
    parameters = {"name": "tom3"}
    return render(request, "bookInfo/index3.html", {"name": "tom3", "my_list": list(range(0, 9))})


def show_books(request):
    book_list = Book.objects.all()
    parameters = {"book_list": book_list}
    return render(request, "bookInfo/show_books.html", parameters)


def book_detail(request, book_id):
    """
    图书的详细信息
    """
    # 1.根据id查询图书
    book = Book.objects.get(id=book_id)
    # 2.根据book_id获得所有英雄
    hero_list = book.hero_set.all()
    # 3.使用模板
    return render(request, "bookInfo/book_detail.html", {"book": book, "hero_list": hero_list})
