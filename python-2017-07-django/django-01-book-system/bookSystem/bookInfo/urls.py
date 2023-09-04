from django.conf.urls import url
from bookInfo import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'index/', views.index),  # 建立/index和视图index之间的关系
    url(r'index2/', views.index2),  # 建立/index和视图index之间的关系
    url(r'index3/', views.index3),  # 建立/index和视图index之间的关系
    url(r"^books/$", views.show_books),
    url(r"^books/(\d+)/$", views.book_detail)
]
