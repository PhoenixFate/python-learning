from django.db import models


# Create your models here.

# 一类
# 图书类
class Book(models.Model):
    """图书模型类"""
    # 图书名称，CharField说明是一个字符串，max_length指定字符串的最大长度
    title = models.CharField(max_length=100)
    # DateField是一个日期类型
    publish_date = models.DateField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return str(self.title + "; " + self.author)


# 多类
class Hero(models.Model):
    """英雄人物"""
    name = models.CharField(max_length=100)
    # 性别，BooleanField类型，default指定默认值，False代表男
    gender = models.BooleanField(default=False)
    # 备注 comment
    comment = models.CharField(max_length=1024)
    # 建立book和hero 一对多的关系
    # 关系属性对应的表的字段名格式: 关系属性名_id
    book = models.ForeignKey('Book', on_delete=models.CASCADE, )

    def __str__(self):
        return self.name
