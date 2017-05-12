from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=16)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('name', max_length=16)

    def __str__(self):
        return self.name


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


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='文章')

    name = models.CharField('姓名', max_length=16)
    email = models.EmailField('邮箱')
    content = models.TextField('内容', max_length=140)
    created = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.content


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"

    full_name = property(my_property)
