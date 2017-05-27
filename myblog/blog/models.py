from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Category(models.Model):
    name = models.CharField('目录', max_length=16)
    

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ''
        verbose_name_plural = '目录'

class Tag(models.Model):
    name = models.CharField('标签', max_length=16)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ''
        verbose_name_plural = '标签'



class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('内容', blank=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    update = models.DateTimeField('更新时间', auto_now=True)

    category = models.ForeignKey(Category, verbose_name='目录')
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = '文章'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='文章')

    name = models.CharField('姓名', max_length=16)
    email = models.EmailField('邮箱')
    content = models.TextField('内容', max_length=140)
    created = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = ''
        verbose_name_plural = '评论'


class Person(models.Model):
    first_name = models.CharField('姓',max_length=2, blank=True)
    last_name = models.CharField('名',max_length=2)
    sex = models.CharField('性别',max_length=1,default='人妖')
    age = models.CharField('年龄',max_length=3,blank=True)
    gra_sch = models.CharField('毕业学校',max_length=20,default='社会大学')

    def my_property(self):
        return self.first_name + '' + self.last_name
    my_property.short_description = "名称"

    full_name = property(my_property)
    class Meta:
        verbose_name = ''
        verbose_name_plural = '人物'


class User(models.Model):
    username = models.CharField('用户名',max_length=50)
    password = models.CharField('密码',max_length=50)
    email = models.EmailField('邮箱')
    class Meta:
        verbose_name = ''
        verbose_name_plural = '用户'
    def __str__(self):
        return self.username