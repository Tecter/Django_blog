from django.shortcuts import render
from blog import models, forms


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
