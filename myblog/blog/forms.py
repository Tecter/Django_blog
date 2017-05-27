from django import forms
from .models import User


class CommentForm(forms.Form):
    name = forms.CharField(label='称呼', max_length=16, error_messages={
        'required': '请填写您的称呼',
        'maxlength': '称呼太长'
    })

    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    content = forms.CharField(label='内容', error_messages={
        'required': '请填写您的评论内容',
        'maxlength': '评论内容太长'
    })
class UserForm(forms.Form):
    username = forms.CharField(label='账号',max_length=10,error_messages={
        'required':'请填写用户名',
        'maxlength':'用户名太长',
        })
    password = forms.CharField(label='密码',max_length=16,error_messages={
        'required':'请填写密码',
        'maxlength':'密码太长',
        })

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    # username_list = User.objects.values_list('username')
    # for username_temp in username_list:
    #     if username == username_temp[0]:
    #         username = forms.CharField(label='用户名：',max_length=100)
    passworld = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')
