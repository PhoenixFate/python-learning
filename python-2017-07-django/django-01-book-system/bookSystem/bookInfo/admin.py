from django.contrib import admin
from bookInfo.models import Book, Hero


# Register your models here.

# 自定义模型管理类
class BookAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ["id", "title", "publish_date"]


class HeroAdmin(admin.ModelAdmin):
    """英雄任务管理类"""
    list_display = ["id", "name", "gender", "comment"]


# 后台管理相关文件
# 注册模型类
admin.site.register(Book, BookAdmin)
admin.site.register(Hero)
