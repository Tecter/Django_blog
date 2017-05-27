from django.contrib import admin
from .models import Blog, Tag, Category, Comment, Person, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'update',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','age','sex','gra_sch',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'email', 'created',)


class UserAdmin(admin.ModelAdmin):
	list_display = ('username','email',)




admin.site.register([Category, Tag])
admin.site.register(Blog, BlogAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)