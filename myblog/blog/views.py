from django.shortcuts import render
from blog import models#, forms
from . import forms

#from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User

# import pdb
 

# Create your views here.
# 获取博客列表
def get_blogs(request):
    ctx = {
        'blogs': models.Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)


# 获取一条博客，及评论
def get_detail(request, blog_id):
    try:
        blog = models.Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        # 加载评论表单
        form = forms.CommentForm()
    else:
        # 评论提交的数据
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            models.Comment.objects.create(**cleaned_data)

            form = forms.CommentForm()

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }

    return render(request, 'blog-detail.html', ctx)

# 获取博客内容
def get_content(request, blog_id):
    try:
        blog = models.Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    ctx = {
        'blog':blog,
        'content':models.Blog.objects.get(id=blog_id).content,
        'author':models.Blog.objects.get(id=blog_id).author,
        'created':models.Blog.objects.get(id=blog_id).created,
        'update':models.Blog.objects.get(id=blog_id).update,
    }
    return render(request, 'blog-content.html', ctx)





def register(request):
    if request.method == "POST":
        uf = forms.UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.passworld = passworld
            user.email = email
            user.save()
            #返回注册成功页面
            return render(request,'success.html',{'username':username})
    else:
        uf = forms.UserForm()
    return render(request,'register.html',{'uf':uf})
